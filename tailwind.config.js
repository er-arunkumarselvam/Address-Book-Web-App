/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*"],
  theme: {
    colors: {
      violet: "#971FE0",
      medium_violet: "#9333ea",
      darkgrey: "#282828",
      silver: "#6b7280",
      palegrey: "#F3F3F3",
      axlegrey: "#FDF8FF",
      darkmintgreen: "#16A34A",
      mintgreen: "#22C55E",
      lightgreen: "#00E676",
      strawberry: "#F8163E",
      rose_medium: "#f43f5e",
      white: "#ffffff",
      emerald: "#139647",
      ice: "#D6F0E0",
      rose_red: "#D62E4A",
      light_pink: "#F9E1E5",
      pale_purple: "#ECDCF9",
      blue: "#0668E1 ",
      light_blue: "#0080FB",
    },
    fontFamily: {
      poppins: ["Poppins"],
      roboto: ["Roboto"],
    },
    extend: {
      spacing: {
        160: "40rem",
        101: "28rem",
      },
    },
  },
  plugins: [],
};
