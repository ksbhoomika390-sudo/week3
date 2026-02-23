"""
JavaScript Basics Python Server
Demonstrates JavaScript fundamentals: Alert, Form Validation, Calculator, Text Change
Run this script and open http://localhost:8000 in your browser.
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


class ResponseHandler(SimpleHTTPRequestHandler):
    """Custom handler to serve files and display JavaScript info"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/' or self.path == '':
            self.path = '/index.html'
        return super().do_GET()

    def end_headers(self):
        """Add custom headers"""
        self.send_header('Cache-Control', 'no-cache')
        self.send_header('X-UA-Compatible', 'IE=edge')
        super().end_headers()

    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[{self.log_date_time_string()}] {format % args}")


def display_javascript_info():
    """Display JavaScript basics information in console"""
    info = """
╔═══════════════════════════════════════════════════════════════════╗
║           JAVASCRIPT BASICS TUTORIAL - INTERACTIVE DEMO             ║
╚═══════════════════════════════════════════════════════════════════╝

📚 JAVASCRIPT CONCEPTS COVERED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1️⃣  ALERT ON BUTTON CLICK
    ├─ Function: showAlert()
    ├─ Event: onclick button
    ├─ Usage: Display pop-up messages to users
    └─ Example: alert('Hello World!')

2️⃣  CHANGE TEXT ON CLICK
    ├─ Function: changeText(), resetText()
    ├─ Method: textContent property
    ├─ CSS: Dynamic style changes
    └─ Concepts: DOM manipulation, state tracking

3️⃣  FORM VALIDATION
    ├─ Function: validateForm()
    ├─ Validations:
    │   ├─ Name: Min 3 chars, letters only
    │   ├─ Email: Valid email format
    │   ├─ Phone: Exactly 10 digits
    │   ├─ Password: Min 6 characters
    │   └─ Terms: Checkbox required
    ├─ Real-time validation: blur event listeners
    ├─ Error handling: Display/clear error messages
    └─ Success feedback: Show success message

4️⃣  SIMPLE CALCULATOR
    ├─ Functions:
    │   ├─ appendNumber() - Add numbers to display
    │   ├─ appendOperator() - Add operators (+, -, *, /)
    │   ├─ appendDecimal() - Add decimal point
    │   ├─ deleteLastChar() - Delete last character
    │   ├─ clearCalculator() - Clear display
    │   └─ calculateResult() - Evaluate expression
    ├─ Features:
    │   ├─ Prevent multiple operators
    │   ├─ Prevent multiple decimals
    │   ├─ Error handling
    │   └─ Calculation history
    └─ Operators: +, -, *, / (÷)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔑 KEY JAVASCRIPT CONCEPTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✓ FUNCTIONS
  ├─ Named functions: function myFunction() { }
  ├─ Parameters & return values
  └─ Event handlers

✓ DOM MANIPULATION
  ├─ document.getElementById() - Get elements
  ├─ element.textContent - Change text
  ├─ element.style - Change CSS
  └─ innerHTML vs textContent - Security

✓ EVENT HANDLING
  ├─ onclick attribute - Click event
  ├─ addEventListener() - Add event listener
  ├─ Event object - event.preventDefault()
  └─ Multiple event types

✓ FORM VALIDATION
  ├─ Regex patterns - /pattern/
  ├─ Validation rules - Required, Format, Length
  ├─ Error display - Show/hide messages
  └─ Real-time validation

✓ CONDITIONAL LOGIC
  ├─ if / else statements
  ├─ Logical operators: &&, ||, !
  └─ Ternary operator: ? :

✓ VARIABLES & DATA TYPES
  ├─ let, const, var
  ├─ String, Number, Boolean
  └─ String methods: trim(), includes()

✓ ARRAYS & LOOPS
  ├─ Array methods: push(), slice(), map()
  ├─ forEach() loop
  └─ filter() and reduce()

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 CODE EXAMPLES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ALERT ON BUTTON CLICK:
┌─────────────────────────────────┐
│ function showAlert() {          │
│   alert('Hello World!');        │
│ }                               │
│ <button onclick="showAlert()">  │
│   Click Me                      │
│ </button>                       │
└─────────────────────────────────┘

CHANGE TEXT:
┌─────────────────────────────────┐
│ function changeText() {         │
│   const elem =                  │
│     document.getElementById(    │
│       'myText'                  │
│     );                          │
│   elem.textContent = 'New!';   │
│   elem.style.color = 'red';    │
│ }                               │
└─────────────────────────────────┘

FORM VALIDATION:
┌─────────────────────────────────┐
│ function validateForm(event) {  │
│   event.preventDefault();       │
│   const email = document        │
│     .getElementById('email')    │
│     .value;                     │
│   const valid =                 │
│     /^[^@]+@[^@]+$/.test(      │
│       email                     │
│     );                          │
│   if (valid) {                  │
│     // Form is valid           │
│   }                             │
│ }                               │
└─────────────────────────────────┘

CALCULATOR:
┌─────────────────────────────────┐
│ function calculateResult() {    │
│   const expr = display.value;  │
│   const result = eval(expr);   │
│   display.value = result;      │
│ }                               │
└─────────────────────────────────┘

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 FILES STRUCTURE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  index.html      - HTML structure (5 main sections)
  script.js       - JavaScript code (all functions)
  style.css       - Styling and responsive design
  app.py          - This Python server

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎓 LEARNING PATH:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Try each feature (Alert, Text Change, Form, Calculator)
2. Open Developer Tools (F12) and check Console
3. Check Network tab to see file requests
4. Right-click → Inspect Element to see HTML structure
5. Try modifying JS functions and refresh to see changes
6. Combine features to build more complex programs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🔍 BROWSER DEVELOPER TOOLS SHORTCUTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  F12                    - Open Developer Tools
  Ctrl+Shift+M           - Toggle Device Toolbar (Mobile View)
  Ctrl+Shift+C           - Inspect Element
  Ctrl+Shift+J           - Open Console
  Console Commands:
  ├─ console.log()       - Log messages
  ├─ console.error()     - Log errors
  ├─ document.body       - Access HTML body
  └─ debugger;           - Set breakpoint

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 PRACTICE EXERCISES:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Modify alert message from "Hello" to "Welcome!"
2. Add more cases to text change functionality
3. Add age validation to the form (18-100)
4. Add percentage button to calculator (%)
5. Create a function that counts button clicks
6. Add localStorage to save calculator history
7. Create a modal popup instead of alert()
8. Add form auto-fill functionality

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    print(info)


def main():
    """Main function to start the server"""
    # Display JavaScript basics information
    display_javascript_info()

    # Get the current directory
    current_dir = os.getcwd()
    print(f"\n✓ Working Directory: {current_dir}")
    print(f"✓ Files Found:")
    if os.path.exists('index.html'):
        print(f"  ✓ index.html")
    if os.path.exists('script.js'):
        print(f"  ✓ script.js")
    if os.path.exists('style.css'):
        print(f"  ✓ style.css")
    if os.path.exists('app.py'):
        print(f"  ✓ app.py")

    # Server configuration
    port = 8000
    host = '0.0.0.0'
    server_address = (host, port)
    
    # Create HTTP server
    httpd = HTTPServer(server_address, ResponseHandler)
    
    # Display server info
    print(f"\n" + "="*70)
    print(f"🚀 SERVER STARTING...")
    print(f"="*70)
    print(f"📍 Local URL:     http://localhost:{port}")
    print(f"📍 Network URL:   http://<YOUR_IP>:{port}")
    print(f"📍 To find IP:    Run 'ipconfig' in PowerShell (Windows)")
    print(f"🌐 Open browser:  http://localhost:{port}/index.html")
    print(f"\n💡 Press CTRL+C to stop the server")
    print(f"🧪 Open F12 to see Console logs")
    print(f"="*70 + "\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped.")
        print("Thank you for learning JavaScript!\n")
        httpd.server_close()
        sys.exit(0)


if __name__ == '__main__':
    main()
