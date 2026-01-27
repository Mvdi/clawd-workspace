import Link from 'next/link';

export default function HomePage() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-indigo-50 to-purple-50 flex items-center justify-center">
      <div className="max-w-4xl mx-auto px-4 text-center">
        <h1 className="text-6xl font-bold text-gray-900 mb-6">
          Sponsorship Tracker
        </h1>
        <p className="text-2xl text-gray-600 mb-12">
          Track your sponsored content deals, deadlines, and payments
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <div className="text-4xl mb-4">📋</div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">Track Deals</h3>
            <p className="text-gray-600">
              Never miss a deadline. Organize all your sponsorship deals in one place.
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <div className="text-4xl mb-4">💰</div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">Monitor Payments</h3>
            <p className="text-gray-600">
              Know exactly when to expect payment and what's still pending.
            </p>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-lg">
            <div className="text-4xl mb-4">📊</div>
            <h3 className="text-xl font-semibold text-gray-900 mb-2">Dashboard Analytics</h3>
            <p className="text-gray-600">
              See your active deals, upcoming deadlines, and monthly revenue at a glance.
            </p>
          </div>
        </div>

        <div className="flex justify-center gap-4">
          <Link
            href="/signup"
            className="bg-indigo-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-indigo-700 transition-colors"
          >
            Get Started Free
          </Link>
          <Link
            href="/login"
            className="bg-white text-indigo-600 px-8 py-4 rounded-lg text-lg font-semibold border-2 border-indigo-600 hover:bg-indigo-50 transition-colors"
          >
            Login
          </Link>
        </div>

        <p className="text-gray-500 mt-8">
          Free tier: Up to 5 active deals • Pro: Unlimited deals
        </p>
      </div>
    </div>
  );
}
