import { sqliteTable, text, integer, real } from 'drizzle-orm/sqlite-core';

export const users = sqliteTable('users', {
  id: integer('id').primaryKey().autoIncrement(),
  email: text('email').notNull().unique(),
  password_hash: text('password_hash').notNull(),
  created_at: integer('created_at', { mode: 'timestamp' }).notNull().default(sql`strftime('%s', 'now')`),
});

export const deals = sqliteTable('deals', {
  id: integer('id').primaryKey().autoIncrement(),
  user_id: integer('user_id').notNull(),
  title: text('title').notNull(),
  sponsor: text('sponsor').notNull(),
  amount: real('amount').notNull(),
  deadline: integer('deadline', { mode: 'timestamp' }).notNull(),
  payment_status: text('payment_status', { enum: ['not_sent', 'partial', 'paid'] }).notNull(),
  created_at: integer('created_at', { mode: 'timestamp' }).notNull().default(sql`strftime('%s', 'now')`),
});

import { sql } from 'drizzle-orm';
