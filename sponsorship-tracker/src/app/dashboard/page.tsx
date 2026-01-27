'use client';

import { useSession } from 'next-auth/react';
import { useRouter } from 'next/navigation';
import { useState, useEffect } from 'react';
import { Badge } from '@/components/ui/badge';
import { Card } from '@/components/ui/card';

interface Deal {
  id: number;
  title: string;
  sponsor: string;
  amount: number;
  deadline: string;
  payment_status: 'not_sent' | 'partial' | 'paid';
  created_at: string;
}

export default function DashboardPage() {
  const { data: session, status } = useSession();
  const router = useRouter();
  const [deals, setDeals] = useState<Deal[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (status === 'authenticated') {
      fetch('/api/deals')
        .then((res) => res.json())
        .then((data) => {
          setDeals(data);
          setLoading(false);
        })
        .catch(console.error);
    }
  }, [status]);

  if (status === 'loading') {
    return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  }

  if (!session) {
    router.push('/login');
    return null;
  }

  const activeDeals = deals.filter((d) => d.payment_status !== 'paid');
  const now = new Date();
  const upcomingDeadlines = activeDeals.filter((d) => {
    const deadline = new Date(d.deadline);
    const daysUntil = Math.ceil((deadline.getTime() - now.getTime()) / (1000 * 60 * 60 * 24));
    return daysUntil <= 7 && daysUntil >= 0;
  });
  const pendingPayments = activeDeals.filter((d) => d.payment_status === 'not_sent');

  const thisMonth = new Date().getMonth();
  const thisYear = new Date().getFullYear();
  const monthlyRevenue = deals
    .filter((d) => {
      const dealDate = new Date(d.created_at);
      return (
        d.payment_status === 'paid' &&
        dealDate.getMonth() === thisMonth &&
        dealDate.getFullYear() === thisYear
      );
    })
    .reduce((sum, d) => sum + d.amount, 0);

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="max-w-7xl mx-auto py-8 px-4">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Dashboard</h1>

        <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
          <Card className="p-6">
            <h3 className="text-sm font-medium text-gray-500">Active Deals</h3>
            <p className="text-3xl font-bold text-indigo-600 mt-2">{activeDeals.length}</p>
          </Card>
          <Card className="p-6">
            <h3 className="text-sm font-medium text-gray-500">Upcoming Deadlines</h3>
            <p className="text-3xl font-bold text-orange-600 mt-2">{upcomingDeadlines.length}</p>
          </Card>
          <Card className="p-6">
            <h3 className="text-sm font-medium text-gray-500">Pending Payments</h3>
            <p className="text-3xl font-bold text-yellow-600 mt-2">{pendingPayments.length}</p>
          </Card>
          <Card className="p-6">
            <h3 className="text-sm font-medium text-gray-500">Monthly Revenue</h3>
            <p className="text-3xl font-bold text-green-600 mt-2">${monthlyRevenue.toFixed(2)}</p>
          </Card>
        </div>

        <Card className="p-6">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-xl font-bold text-gray-900">Your Deals</h2>
            <button
              onClick={() => router.push('/deals/new')}
              className="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700"
            >
              + New Deal
            </button>
          </div>

          {loading ? (
            <div className="text-center py-12">Loading deals...</div>
          ) : deals.length === 0 ? (
            <p className="text-gray-500 text-center py-12">
              No deals yet. Create your first sponsorship deal!
            </p>
          ) : (
            <div className="space-y-4">
              {deals.map((deal) => {
                const deadline = new Date(deal.deadline);
                const now = new Date();
                const daysUntil = Math.ceil((deadline.getTime() - now.getTime()) / (1000 * 60 * 60 * 24));

                let statusBadge: React.ReactNode;
                if (daysUntil < 0) {
                  statusBadge = <Badge variant="destructive">Overdue</Badge>;
                } else if (daysUntil <= 3) {
                  statusBadge = <Badge variant="destructive">Due Soon</Badge>;
                } else if (daysUntil <= 7) {
                  statusBadge = <Badge className="bg-orange-500">Due Soon</Badge>;
                } else {
                  statusBadge = <Badge className="bg-green-500">On Track</Badge>;
                }

                return (
                  <div
                    key={deal.id}
                    onClick={() => router.push(`/deals/${deal.id}`)}
                    className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer"
                  >
                    <div className="flex justify-between items-start mb-2">
                      <div>
                        <h3 className="text-lg font-semibold text-gray-900">{deal.title}</h3>
                        <p className="text-sm text-gray-600">{deal.sponsor}</p>
                      </div>
                      {statusBadge}
                    </div>
                    <div className="flex justify-between items-center text-sm text-gray-600 mt-2">
                      <span>📅 {deadline.toLocaleDateString()}</span>
                      <span className="font-semibold">
                        ${deal.amount.toFixed(2)}
                      </span>
                    </div>
                    <div className="mt-2">
                      {deal.payment_status === 'paid' ? (
                        <Badge className="bg-green-500">Paid</Badge>
                      ) : deal.payment_status === 'partial' ? (
                        <Badge className="bg-blue-500">Partial</Badge>
                      ) : (
                        <Badge variant="outline">Not Sent</Badge>
                      )}
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </Card>
      </div>
    </div>
  );
}
