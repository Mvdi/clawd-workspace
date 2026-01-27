/** Tailwind configuration for Sponsorship Tracker MVP */
module.exports = {
  content: ["./src/**/*.{ts,tsx}", "./app/**/*.{ts,tsx}", "./pages/**/*.{ts,tsx}", "./src/**/!*{.test}.tsx"],
  theme: {
    extend: {
      colors: {
        brand: {
          50: '#f5fee9',
          100: '#e2fbd7',
          200: '#c2f3c9',
          300: '#94e6ad',
          400: '#68d597',
          500: '#3ac07e',
          600: '#2a9f63',
          700: '#1f7f4d',
          800: '#165c3b',
          900: '#0f432f'
        }
      }
    }
  },
  plugins: [],
};
