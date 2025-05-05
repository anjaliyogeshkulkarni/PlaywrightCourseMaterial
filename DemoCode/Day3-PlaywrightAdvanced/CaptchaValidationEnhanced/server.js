const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const app = express();
const port = 3000;

// Middleware to log incoming requests
app.use((req, res, next) => {
  console.log(`Incoming Request: ${req.method} ${req.url}`);
  next();
});

// Parse incoming JSON
app.use(bodyParser.json());

// Serve static HTML and other files from "public" directory
app.use(express.static(path.join(__dirname, 'public')));

// Mock CAPTCHA verification endpoint
app.post('/verify-captcha', (req, res) => {
  const { captchaToken } = req.body;
  if (captchaToken === 'solved' || captchaToken === '12345') {
    return res.json({ success: true });
  }
  res.status(401).json({ success: false });
});

// Start server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
