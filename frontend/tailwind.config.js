/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  content: [],
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      'white':'#ffffff',
      'purple': '#722CE0',
      'light-purple': '#BD77FF',
      'dark-purple': '#3908A7',
      'button-hover': '#4F09BD',
      'reviews': "#130C2F"
    },
    screens: {

      'lg': {'max': '992px'},
      'md': {'max': '670px'},
    },
    extend: {},
  },

  plugins: [],
}

