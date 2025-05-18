<<<<<<< HEAD
This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
=======
# Roamio Waitlist Landing Page

A modern, responsive landing page for Roamio - your campus companion app. This single-page application collects waitlist signups and stores them in a Google Sheet via SheetDB.

## Features

- 🎨 Clean, modern design with soft gradients
- 📱 Fully responsive layout
- ✉️ Email collection form with validation
- 🔄 Real-time form submission to Google Sheets
- 🎯 Student-friendly UI/UX

## Tech Stack

- HTML5
- CSS3 (with modern features like CSS variables and flexbox)
- Vanilla JavaScript
- SheetDB API for Google Sheets integration
- Inter font family for typography

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/roamio-waitlist.git
```

2. Open `index.html` in your browser to view the page locally.

## Development

The project consists of three main files:
- `index.html` - Main page structure
- `styles.css` - Styling and responsive design
- `script.js` - Form handling and SheetDB integration

## SheetDB Integration

The waitlist form is connected to a Google Sheet via SheetDB API. When users submit their email:
1. The form validates the email format
2. The email is sent to the SheetDB API
3. SheetDB adds the email to the connected Google Sheet
4. Users receive a success/error message accordingly

## License

MIT License - feel free to use this template for your own projects! 
>>>>>>> 9f36302cb7f5ed856ed02565695082040dc34d64
