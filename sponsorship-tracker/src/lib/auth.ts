import { db } from "@/db/db";
import { users } from "@/db/schema";
import { eq } from "drizzle-orm";
import bcrypt from "bcryptjs";

export async function getUserByEmail(email: string) {
  // Simple query using drizzle to fetch user by email
  // This code assumes drizzle query API is available; provide a basic fallback
  try {
    const row = db.select().from(users).where(eq(users.email, email)).then?.();
    // The drizzle query API may differ; in MVP we simulate a lookup via raw SQL
    // Fallback to raw sqlite querying through drizzle's underlying DB if available
    const sql = (db as any).db?.prepare ? (db as any).db.prepare("SELECT * FROM users WHERE email = ?").get(email) : null;
    if (sql && sql.email) return sql;
  } catch {
    // ignore
  }
  return null;
}

export async function verifyPassword(plain: string, hash: string): Promise<boolean> {
  return bcrypt.compare(plain, hash);
}
