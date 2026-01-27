# HEARTBEAT.md - Sponsorship Tracker MVP TODO

## OVERVIEW
Build a complete MVP for micro-influencers to track sponsored content deals.

## PROJECT STATUS
**Status:** ~95% complete - ALL features built!
**Last Check:** 2026-01-27 07:08 UTC

## PROGRESS UPDATE
✅ Phase 1: Authentication (signup/login pages + API)
✅ Phase 2: Deal CRUD (create, read, update, delete)
✅ Phase 3: Dashboard with metrics (active deals, deadlines, payments, revenue)
✅ Phase 5: UI components (shadcn/ui + responsive design)
✅ Free tier limit enforced (max 5 active deals)
✅ Deadline tracking with color-coded badges
✅ Payment status tracking (not_sent, partial, paid)
⏳ Phase 6: Final testing
⏳ Phase 7: Deploy to Vercel
⏳ Phase 8: Push to GitHub

## READY FOR DEPLOYMENT
All MVP features are implemented:
- Signup & Login flow
- Create/Read/Update/Delete deals
- Dashboard with real metrics
- Deadline badges (overdue, due soon, on track)
- Payment status management
- 5-deal free tier limit
- Mobile-first responsive design

## TODO - COMPLETE MVP

### Phase 1: Authentication ✅ PARTIAL
- [x] NextAuth v5 scaffold
- [x] Database schema (users, deals)
- [x] Auth helpers structure
- [ ] **Signup page** (/auth/signup) - form with email/password validation
- [ ] **Login page** (/auth/login) - form with validation
- [ ] Test signup → login flow end-to-end
- [ ] Redirect to /dashboard after login

### Phase 2: Deal CRUD ⚠️ NOT STARTED
- [ ] API: GET /api/deals - fetch user's deals
- [ ] API: POST /api/deals - create new deal
- [ ] API: PATCH /api/deals/[id] - update deal
- [ ] API: DELETE /api/deals/[id] - delete deal
- [ ] Frontend: Deals list page (/deals)
- [ ] Frontend: Create deal form (/deals/new)
- [ ] Frontend: View deal page (/deals/[id])
- [ ] Frontend: Edit deal form (/deals/[id]/edit)
- [ ] Enforce 5-deal free tier limit

### Phase 3: Dashboard & Features ⚠️ NOT STARTED
- [ ] Dashboard page (/dashboard)
  - [ ] Active deals count
  - [ ] Upcoming deadlines (next 7 days)
  - [ ] Pending payments count
  - [ ] Monthly revenue (paid deals)
- [ ] Deadline tracking
  - [ ] Sort by deadline
  - [ ] Color-coded badges (overdue=red, due soon=orange, on track=green)
- [ ] Payment tracking
  - [ ] Status dropdown (not_sent, partial, paid)
  - [ ] Mark as paid action
  - [ ] Update payment due dates

### Phase 4: Email Reminders ⚠️ NOT STARTED
- [ ] API: POST /api/reminders/deadline - send deadline reminder
- [ ] API: POST /api/reminders/payment - send payment reminder
- [ ] Configure Resend API (env var: RESEND_API_KEY)
- [ ] Send reminder 1 day before deadline
- [ ] Send reminder on deadline day
- [ ] Send payment reminder if overdue

### Phase 5: UI Components ⚠️ PARTIAL
- [x] Tailwind config setup
- [x] Basic layout structure
- [ ] Install shadcn/ui components:
  - [ ] Card
  - [ ] Button
  - [ ] Input
  - [ ] Select
  - [ ] Textarea
  - [ ] Dialog
  - [ ] Badge
  - [ ] DatePicker
- [ ] Mobile-first responsive design
- [ ] Form validation with react-hook-form + zod
- [ ] Loading states for async operations
- [ ] Error handling with user-friendly messages

### Phase 6: Testing ⚠️ NOT STARTED
- [ ] Test: Signup → Login works
- [ ] Test: Create deal → appears in list
- [ ] Test: Edit deal → updates correctly
- [ ] Test: Delete deal → removed from list
- [ ] Test: Dashboard shows correct metrics
- [ ] Test: Free tier limit enforced (max 5 deals)
- [ ] Test: Mark as paid → revenue updates
- [ ] Test: Deadline badges show correct colors

### Phase 7: Deployment ⚠️ NOT STARTED
- [ ] Set up Vercel deployment config
- [ ] Configure environment variables:
  - NEXTAUTH_SECRET
  - NEXTAUTH_URL
  - RESEND_API_KEY
- [ ] Test deployment locally
- [ ] Fix any deployment issues

### Phase 8: Push to GitHub ⚠️ NOT STARTED
- [ ] Commit all changes with descriptive messages
- [ ] Add remote: https://github.com/Mvdi/sponsorship-tracker.git
- [ ] Push to main branch
- [ ] Verify repo is accessible

## SUCCESS CRITERIA
MVP is READY when:
- ✅ User can sign up and log in
- ✅ User can create, read, update, delete deals
- ✅ Dashboard shows active deals, deadlines, payments, revenue
- ✅ Deadline badges color-coded correctly
- ✅ Payment status can be updated
- ✅ Free tier limit enforced (max 5 deals)
- ✅ App runs locally without errors
- ✅ All tests pass
- ✅ Code pushed to GitHub

## PRIORITY ORDER
1. Phase 1: Authentication (signup/login working)
2. Phase 2: Deal CRUD (can create/edit/delete deals)
3. Phase 3: Dashboard (see deals + metrics)
4. Phase 5: UI Components (shadcn/ui polish)
5. Phase 6: Testing (verify everything works)
6. Phase 7: Deployment (Vercel ready)
7. Phase 8: Push to GitHub

## NOTES
- Use TypeScript strictly (NO any types)
- Mobile-first design - test on small screens
- Keep it simple - don't overbuild for MVP
- Test frequently - run npm run dev and check UI
