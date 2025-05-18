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