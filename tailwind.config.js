/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './product/templates/product/*.html', // Adjust this to your template location
    './product/static/js/**/*.js', // Leave this path even if the folder doesn't exist yet
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
