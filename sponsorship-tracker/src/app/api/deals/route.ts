import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { db } from '@/db/db';
import { deals } from '@/db/schema';
import { eq, and, desc, count } from 'drizzle-orm';

export async function GET() {
  const session = await getServerSession();

  if (!session?.user?.id) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const userDeals = await db
    .select()
    .from(deals)
    .where(eq(deals.user_id, parseInt(session.user.id)))
    .orderBy(desc(deals.deadline));

  return NextResponse.json(userDeals);
}

export async function POST(req: Request) {
  const session = await getServerSession();

  if (!session?.user?.id) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const body = await req.json();
  const { title, sponsor, amount, deadline } = body;

  if (!title || !sponsor || !amount || !deadline) {
    return NextResponse.json({ error: 'Missing required fields' }, { status: 400 });
  }

  const [existingDealCount] = await db
    .select({ count: count() })
    .from(deals)
    .where(eq(deals.user_id, parseInt(session.user.id)))
    .values();

  const activeDeals = existingDealCount?.[0]?.count || 0;

  if (activeDeals >= 5) {
    return NextResponse.json({ error: 'Free tier limit: Maximum 5 active deals' }, { status: 403 });
  }

  const [newDeal] = await db
    .insert(deals)
    .values({
      user_id: parseInt(session.user.id),
      title,
      sponsor,
      amount: parseFloat(amount),
      deadline: new Date(deadline),
      payment_status: 'not_sent',
    })
    .returning();

  return NextResponse.json(newDeal[0], { status: 201 });
}
