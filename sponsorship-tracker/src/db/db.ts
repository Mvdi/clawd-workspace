import { createClient } from '@libsql/client';
import { drizzle } from 'drizzle-orm/lib-sql';
import * as schema from './schema';

const client = new Client({ url: 'file:sponsorship-tracker.db' });
export const db = drizzle(client, { schema });
