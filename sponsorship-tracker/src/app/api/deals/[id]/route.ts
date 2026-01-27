import { NextResponse } from 'next/server';
import { getServerSession } from 'next-auth';
import { db } from '@/db/db';
import { deals } from '@/db/schema';
import { eq } from 'drizzle-orm';

export async function PATCH(req: Request, { params }: { params: { id: string } }) {
  const session = await getServerSession();

  if (!session?.user?.id) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const dealId = parseInt(params.id);
  const body = await req.json();

  const deal = await db
    .select()
    .from(deals)
    .where(eq(deals.id, dealId))
    .get();

  if (!deal) {
    return NextResponse.json({ error: 'Deal not found' }, { status: 404 });
  }

  if (deal.user_id !== parseInt(session.user.id)) {
    return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
  }

  const [updatedDeal] = await db
    .update(deals)
    .set({
      ...body,
      updated_at: new Date(),
    })
    .where(eq(deals.id, dealId))
    .returning();

  return NextResponse.json(updatedDeal[0]);
}

export async function DELETE(req: Request, { params }: { params: { id: string } }) {
  const session = await getServerSession();

  if (!session?.user?.id) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  const dealId = parseInt(params.id);

  const deal = await db
    .select()
    .from(deals)
    .where(eq(deals.id, dealId))
    .get();

  if (!deal) {
    return NextResponse.json({ error: 'Deal not found' }, { status: 404 });
  }

  if (deal.user_id !== parseInt(session.user.id)) {
    return NextResponse.json({ error: 'Forbidden' }, { status: 403 });
  }

  await db.delete(deals).where(eq(deals.id, dealId));

  return NextResponse.json({ success: true });
}
