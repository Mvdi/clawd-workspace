'use client';

import { useState, useEffect } from 'react';
import { useRouter, useParams } from 'next/navigation';
import { useSession } from 'next-auth/react';
import { Card } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';

interface Deal {
  id: number;
  title: string;
  sponsor: string;
  amount: number;
  deadline: string;
  payment_status: 'not_sent' | 'partial' | 'paid';
  notes: string;
}

export default function DealDetailPage() {
  const router = useRouter();
  const params = useParams();
  const { data: session } = useSession();
  const [deal, setDeal] = useState<Deal | null>(null);
  const [loading, setLoading] = useState(true);
  const [updating, setUpdating] = useState(false);

  useEffect(() => {
    if (params.id) {
      fetch(`/api/deals`)
        .then((res) => res.json())
        .then((deals) => {
          const found = deals.find((d: Deal) => d.id === parseInt(params.id as string));
          setDeal(found || null);
          setLoading(false);
        })
        .catch(console.error);
    }
  }, [params.id]);

  const updatePaymentStatus = async (status: 'not_sent' | 'partial' | 'paid') => {
    setUpdating(true);
    try {
      await fetch(`/api/deals/${params.id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ payment_status: status }),
      });
      setDeal(deal ? { ...deal, payment_status: status } : null);
    } catch (err) {
      console.error(err);
    } finally {
      setUpdating(false);
    }
  };

  if (loading) {
    return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  }

  if (!deal) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <Card className="p-8">
          <h1 className="text-2xl font-bold text-red-600">Deal Not Found</h1>
          <Button onClick={() => router.push('/dashboard')} className="mt-4">
            Back to Dashboard
          </Button>
        </Card>
      </div>
    );
  }

  const deadline = new Date(deal.deadline);
  const now = new Date();
  const daysUntil = Math.ceil((deadline.getTime() - now.getTime()) / (1000 * 60 * 60 * 24));

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-3xl mx-auto px-4">
        <Button
          onClick={() => router.push('/dashboard')}
          variant="ghost"
          className="mb-6"
        >
          ← Back to Dashboard
        </Button>

        <Card className="p-8">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">{deal.title}</h1>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
            <div>
              <h2 className="text-lg font-semibold text-gray-700 mb-4">Deal Details</h2>
              <div className="space-y-3">
                <div>
                  <span className="text-sm text-gray-500">Sponsor/Brand:</span>
                  <p className="font-semibold text-gray-900">{deal.sponsor}</p>
                </div>
                <div>
                  <span className="text-sm text-gray-500">Compensation:</span>
                  <p className="text-2xl font-bold text-green-600">${deal.amount.toFixed(2)}</p>
                </div>
                <div>
                  <span className="text-sm text-gray-500">Deadline:</span>
                  <p className="font-semibold">
                    {deadline.toLocaleDateString()} (
                    {daysUntil < 0 ? (
                      <span className="text-red-600">OVERDUE</span>
                    ) : (
                      <span className="text-gray-900">{daysUntil} days left</span>
                    )}
                    )
                  </p>
                </div>
              </div>
            </div>

            <div>
              <h2 className="text-lg font-semibold text-gray-700 mb-4">Payment Status</h2>
              <div className="space-y-4">
                <div>
                  <span className="text-sm text-gray-500">Current Status:</span>
                  <div className="mt-2">
                    {deal.payment_status === 'paid' ? (
                      <Badge className="bg-green-500">Paid</Badge>
                    ) : deal.payment_status === 'partial' ? (
                      <Badge className="bg-blue-500">Partial Payment</Badge>
                    ) : (
                      <Badge variant="outline">Not Sent</Badge>
                    )}
                  </div>
                </div>

                {deal.payment_status !== 'paid' && (
                  <div className="space-y-2">
                    <p className="text-sm text-gray-600">Update status:</p>
                    <div className="flex flex-wrap gap-2">
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => updatePaymentStatus('partial')}
                        disabled={updating}
                      >
                        Mark as Partial
                      </Button>
                      <Button
                        size="sm"
                        onClick={() => updatePaymentStatus('paid')}
                        disabled={updating}
                      >
                        {updating ? 'Marking...' : 'Mark as Paid'}
                      </Button>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>

          {deal.notes && (
            <div className="mt-6 pt-6 border-t border-gray-200">
              <h2 className="text-lg font-semibold text-gray-700 mb-2">Notes</h2>
              <p className="text-gray-600">{deal.notes}</p>
            </div>
          )}

          <div className="mt-8 pt-6 border-t border-gray-200 flex justify-between">
            <Button variant="destructive" onClick={() => router.push(`/deals/${deal.id}/edit`)}>
              Edit Deal
            </Button>
            <Button variant="outline" onClick={() => router.push('/dashboard')}>
              Close
            </Button>
          </div>
        </Card>
      </div>
    </div>
  );
}
