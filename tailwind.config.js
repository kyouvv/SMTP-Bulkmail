/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {},
  },
  daisyui: {
    themes: [
      {
        mytheme: {
        
        "primary": "#ff009f",
        
        "secondary": "#8b5cf6",
        
        "accent": "#885c00",
                
        "neutral": "#202c3a",
                
        "base-100": "#2f2a40",
                
        "info": "#1c80ff",
                
        "success": "#00a45a",
                
        "warning": "#ff8008",
                
        "error": "#e20648",
        },
      },
    ],
  },
  plugins: [require('daisyui')],
}

