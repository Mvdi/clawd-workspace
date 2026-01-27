# Sponsorship Tracker for Influencers - Product Spec

## Mission
Build a lightweight CRM for micro-influencers (5K-50K followers) to track sponsored content deals, deadlines, and payments.

## Core Problem
Micro-influencers constantly complain about missing deadlines for sponsored posts. They manage deals across multiple platforms (DMs, email, WhatsApp) and lose track of deliverables and payments.

## Target Market
- **Primary:** Micro-influencers with 5,000-50,000 followers
- **Secondary:** Content creators with brand deals
- **Tertiary:** Creator managers handling multiple clients

## MVP Features (Phase 1 - Tonight)

### 1. Deal Management
- Add new sponsorship deals
- Store deal details:
  - Brand/Company name
  - Platform (Instagram, TikTok, YouTube, etc.)
  - Deliverables (posts, stories, etc.)
  - Compensation amount
  - Currency
  - Start date
  - Deadline date
  - Status (pending, in progress, completed, cancelled)
  - Notes

### 2. Deadline Tracking
- View all upcoming deadlines
- Sort by deadline date
- Deadline countdown
- Status badges (overdue, due soon, on track)

### 3. Payment Tracking
- Payment status tracking (not sent, partial, paid)
- Payment due date
- Payment amount
- Payment method notes
- Mark as paid when received

### 4. Reminders (Simple)
- Deadline reminders (1 day before, day of)
- Payment reminders (if not received by due date)
- Email notifications

### 5. Dashboard
- Summary view:
  - Active deals count
  - Upcoming deadlines (next 7 days)
  - Pending payments
  - Total revenue (current month)

### 6. Simple Authentication
- Email + password signup/login
- No social auth in MVP (can add later)

## Tech Stack

### Frontend
- **Framework:** Next.js 14 (App Router)
- **Language:** TypeScript
- **UI Components:** shadcn/ui (modern, accessible)
- **Styling:** Tailwind CSS

### Backend
- **API:** Next.js API routes
- **Database:** SQLite (for MVP - easy deployment, no external DB needed)
- **ORM:** Drizzle ORM (lightweight, type-safe)

### Authentication
- **Provider:** NextAuth.js (v5)
- **Database auth** (SQLite)

### Deployment
- **Platform:** Vercel (free tier sufficient for MVP)
- **Database:** SQLite file (deploy with app for now)

## Data Model

```sql
-- Users
CREATE TABLE users (
  id TEXT PRIMARY KEY,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  created_at INTEGER DEFAULT (strftime('%s', 'now'))
);

-- Deals
CREATE TABLE deals (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  brand_name TEXT NOT NULL,
  platform TEXT NOT NULL,
  deliverables TEXT, -- JSON array
  compensation REAL NOT NULL,
  currency TEXT DEFAULT 'USD',
  start_date INTEGER,
  deadline INTEGER NOT NULL,
  payment_due_date INTEGER,
  payment_status TEXT DEFAULT 'not_sent', -- not_sent, partial, paid
  payment_amount REAL,
  payment_method TEXT,
  payment_notes TEXT,
  status TEXT DEFAULT 'pending', -- pending, in_progress, completed, cancelled
  notes TEXT,
  created_at INTEGER DEFAULT (strftime('%s', 'now')),
  updated_at INTEGER DEFAULT (strftime('%s', 'now')),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Monetization Model

### Pricing
- **Free Tier:** $0 (limit to 5 active deals)
- **Pro Tier:** $10-15/month (unlimited deals, email reminders, export)
- **Launch Special:** $7/month lifetime for first 100 users

### Stripe Integration (Post-MVP)
- Checkout page for Pro upgrade
- Subscription management
- Webhooks for subscription status

## Design Aesthetic

### Visual Identity
- **Primary Color:** #6366f1 (Indigo - creator-friendly)
- **Secondary Color:** #8b5cf6 (Purple - creative vibes)
- **Background:** Clean white/light gray
- **Font:** Inter (body), Space Grotesk (headings)

### Vibe
- Clean, minimal, fast
- Mobile-first design (influencers on phones)
- Delightful micro-interactions
- Professional but not corporate

## Roadmap

### Phase 1 - MVP (Tonight)
- [x] Project spec (this file)
- [ ] Initialize Next.js project with TypeScript
- [ ] Set up shadcn/ui
- [ ] Configure Drizzle ORM + SQLite
- [ ] Implement authentication (NextAuth.js)
- [ ] Build deal CRUD operations
- [ ] Create dashboard view
- [ ] Implement deadline tracking
- [ ] Add payment tracking
- [ ] Implement basic email reminders
- [ ] Deploy to Vercel

### Phase 2 - Polish
- [ ] Add deal filtering and search
- [ ] Export to CSV/Excel
- [ ] Add platform-specific deliverable templates
- [ ] Implement social auth (Google, Apple)
- [ ] Add mobile app (React Native)
- [ ] Implement Stripe payments

### Phase 3 - Growth
- [ ] Analytics dashboard (revenue trends, brand insights)
- [ ] Integration with DM platforms (Instagram API, etc.)
- [ ] Team accounts for creator managers
- [ ] Affiliate program
- [ ] Content marketplace (connect influencers with brands)

## Success Metrics

### MVP Success
- 10 signups in first week
- 50% signups convert to at least 1 deal created
- 20% of active deals complete successfully
- 2+ users upgrade to Pro tier

### Product-Market Fit
- 100+ active users
- 10+ Pro subscribers
- 70% retention after 30 days
- Word-of-mouth growth (users recommending to other creators)

## Competition

### Direct Competitors
- **Creator.co** - Full creator platform ($49+)
- **AspireIQ** - Enterprise influencer CRM
- **Grin** - Brand-side tool (not influencer-focused)

### Competitive Advantage
- **Simplicity:** Lightweight, focused on ONE thing
- **Price:** 1/5th the cost of competitors
- **Ease of use:** Setup in 2 minutes, no learning curve
- **Mobile-first:** Designed for phone use

## Risk Mitigation

### Technical Risks
- **DB scaling:** Start with SQLite, migrate to PostgreSQL when needed
- **Email delivery:** Use Resend or SendGrid for reliable emails

### Market Risks
- **Adoption:** Market where creators are already active (Reddit, TikTok creator groups)
- **Competition:** Differentiate on simplicity and price

### Legal Risks
- **Data privacy:** Clear privacy policy, secure authentication
- **Terms of service:** Standard SaaS terms, no unusual restrictions

## Notes for Coding Agent

1. **Keep it simple:** Don't overbuild features. MVP is about core functionality.
2. **Mobile-first:** Test on mobile viewport throughout development.
3. **Type safety:** Use TypeScript strictly - no `any` types.
4. **UI/UX:** Use shadcn/ui components consistently. Make it look polished.
5. **Authentication:** Implement early - don't leave it for later.
6. **Email:** Use a simple email service (Resend recommended for ease).
7. **Testing:** Basic smoke tests for critical flows (signup, add deal, mark paid).

## Next Steps

1. **Create GitHub repository**
2. **Initialize Next.js project**
3. **Set up Drizzle + SQLite**
4. **Start coding** - follow Phase 1 checklist above
5. **Deploy to Vercel**
6. **Launch** - share with creator communities

---

*Created: 2026-01-27 05:42 UTC*
*Ready for coding agent execution*
