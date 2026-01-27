'use client';

import { useState, useEffect } from 'react';
import { useRouter, useParams } from 'next/navigation';
import { useSession } from 'next-auth/react';
import { Card } from '@/components/ui/card';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';

interface Deal {
  id: number;
  title: string;
  sponsor: string;
  amount: number;
  deadline: string;
  payment_status: 'not_sent' | 'partial' | 'paid';
  notes: string;
}

export default function EditDealPage() {
  const router = useRouter();
  const params = useParams();
  const { data: session } = useSession();
  const [formData, setFormData] = useState({
    title: '',
    sponsor: '',
    amount: '',
    deadline: '',
    notes: '',
  });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const [fetching, setFetching] = useState(true);

  useEffect(() => {
    if (params.id) {
      fetch(`/api/deals`)
        .then((res) => res.json())
        .then((deals) => {
          const found = deals.find((d: Deal) => d.id === parseInt(params.id as string));
          if (found) {
            setFormData({
              title: found.title,
              sponsor: found.sponsor,
              amount: found.amount.toString(),
              deadline: found.deadline?.split('T')[0] || '',
              notes: found.notes || '',
            });
          }
          setFetching(false);
        })
        .catch(console.error);
    }
  }, [params.id]);

  if (!session) {
    router.push('/login');
    return null;
  }

  if (fetching) {
    return <div className="min-h-screen flex items-center justify-center">Loading...</div>;
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      const res = await fetch(`/api/deals/${params.id}`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...formData,
          amount: parseFloat(formData.amount),
        }),
      });

      if (res.ok) {
        router.push(`/deals/${params.id}`);
      } else {
        const data = await res.json();
        setError(data.error || 'Failed to update deal');
      }
    } catch (err) {
      setError('Something went wrong');
    } finally {
      setLoading(false);
    }
  };

  const deleteDeal = async () => {
    if (!confirm('Are you sure you want to delete this deal?')) {
      return;
    }

    try {
      const res = await fetch(`/api/deals/${params.id}`, {
        method: 'DELETE',
      });

      if (res.ok) {
        router.push('/dashboard');
      } else {
        const data = await res.json();
        setError(data.error || 'Failed to delete deal');
      }
    } catch (err) {
      setError('Something went wrong');
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-2xl mx-auto px-4">
        <Card className="p-8">
          <h1 className="text-2xl font-bold text-gray-900 mb-6">Edit Deal</h1>

            {error && (
              <div className="bg-red-50 text-red-700 p-4 rounded-md mb-4">
                {error}
              </div>
            )}

            <form onSubmit={handleSubmit} className="space-y-6">
              <div>
                <label htmlFor="title" className="block text-sm font-medium text-gray-700 mb-2">
                  Deal Title
                </label>
                <Input
                  id="title"
                  type="text"
                  required
                  value={formData.title}
                  onChange={(e) => setFormData({ ...formData, title: e.target.value })}
                />
              </div>

              <div>
                <label htmlFor="sponsor" className="block text-sm font-medium text-gray-700 mb-2">
                  Sponsor/Brand
                </label>
                <Input
                  id="sponsor"
                  type="text"
                  required
                  value={formData.sponsor}
                  onChange={(e) => setFormData({ ...formData, sponsor: e.target.value })}
                />
              </div>

              <div>
                <label htmlFor="amount" className="block text-sm font-medium text-gray-700 mb-2">
                  Compensation Amount ($)
                </label>
                <Input
                  id="amount"
                  type="number"
                  step="0.01"
                  required
                  value={formData.amount}
                  onChange={(e) => setFormData({ ...formData, amount: e.target.value })}
                />
              </div>

              <div>
                <label htmlFor="deadline" className="block text-sm font-medium text-gray-700 mb-2">
                  Deadline
                </label>
                <Input
                  id="deadline"
                  type="date"
                  required
                  value={formData.deadline}
                  onChange={(e) => setFormData({ ...formData, deadline: e.target.value })}
                />
              </div>

              <div>
                <label htmlFor="notes" className="block text-sm font-medium text-gray-700 mb-2">
                  Notes (optional)
                </label>
                <textarea
                  id="notes"
                  value={formData.notes}
                  onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-indigo-500"
                  rows={4}
                  placeholder="Any additional notes..."
                />
              </div>

              <div className="flex gap-4">
                <Button
                  type="submit"
                  disabled={loading}
                  className="flex-1"
                >
                  {loading ? 'Saving...' : 'Save Changes'}
                </Button>
                <Button
                  type="button"
                  variant="outline"
                  onClick={() => router.push(`/deals/${params.id}`)}
                  className="flex-1"
                >
                  Cancel
                </Button>
              </div>
            </form>

            <div className="mt-6 pt-6 border-t border-gray-200">
              <Button
                type="button"
                variant="destructive"
                onClick={deleteDeal}
                className="w-full"
              >
                Delete Deal
              </Button>
            </div>
        </Card>
      </div>
    </div>
  );
}
