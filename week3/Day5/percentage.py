"""
Responsive Design Python Server
Demonstrates percentage-based widths and media queries for responsive design.
Run this script and open http://localhost:8000 in your browser.
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path


class ResponseHandler(SimpleHTTPRequestHandler):
    """Custom handler to serve files and display responsive design info"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/':
            self.path = '/responsive.html'
        return super().do_GET()

    def end_headers(self):
        """Add custom headers for responsive design"""
        # Cache control
        self.send_header('Cache-Control', 'no-cache')
        # Viewport for responsive design
        self.send_header('X-UA-Compatible', 'IE=edge')
        super().end_headers()

    def log_message(self, format, *args):
        """Custom logging"""
        print(f"[{self.log_date_time_string()}] {format % args}")


def display_responsive_info():
    """Display responsive design information in console"""
    info = """
╔═══════════════════════════════════════════════════════════════════╗
║           RESPONSIVE DESIGN - PERCENTAGE WIDTH SERVER              ║
╚═══════════════════════════════════════════════════════════════════╝

📱 RESPONSIVE BREAKPOINTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  MOBILE (< 768px):
  ├─ Single column layout
  ├─ Hamburger menu navigation
  ├─ Full-width buttons and forms
  └─ Percentage widths: 95%, 90%, 100%

  TABLET (768px - 1023px):
  ├─ 2-column feature grid
  ├─ Horizontal navigation menu
  ├─ Main content + sidebar layout
  └─ Percentage widths: 95%, 90%, 70%/30% split

  DESKTOP (≥ 1024px):
  ├─ 4-column feature grid
  ├─ Full navigation bar
  ├─ Multi-column layouts
  └─ Percentage widths: 90%, max-width constraints

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 PERCENTAGE WIDTH USAGE:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Element               Mobile    Tablet    Desktop
  ────────────────────────────────────────────────────
  Header/Footer        100%      100%      100%
  Main Container        95%       95%        90%
  Feature Cards        100%      50%        25%
  Sidebar              100%      30%        30%
  Padding/Margins       5%        5%         5%
  Gap between elements  1.5rem    2rem       2rem

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 KEY RESPONSIVE CONCEPTS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✓ Mobile-First Approach
    - Start with mobile styles (< 768px)
    - Add media queries for larger screens

  ✓ Percentage-Based Widths
    - width: 90%, 95%, 100% for flexibility
    - Padding: 5%, margins: 2% for scaling
    - No fixed pixel widths

  ✓ Media Queries
    - @media (min-width: 768px) - Tablet
    - @media (min-width: 1024px) - Desktop
    - @media (min-width: 1440px) - Large Desktop

  ✓ Flexible Components
    - CSS Grid: grid-template-columns changes with breakpoints
    - 100% → 2 columns → 4 columns progression
    - Hamburger menu for mobile, nav bar for desktop

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧪 TESTING ON MOBILE VIEW:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  METHOD 1: Chrome DevTools (Recommended)
  ├─ Press F12 to open Developer Tools
  ├─ Click device icon (Ctrl+Shift+M) to toggle device toolbar
  ├─ Select devices: iPhone SE, iPad, Pixel 5, etc.
  └─ Resize viewport to test responsive behavior

  METHOD 2: Physical Mobile Device
  ├─ Find your computer IP: ipconfig (Windows)
  ├─ Note IPv4 Address (e.g., 192.168.x.x)
  ├─ On mobile: http://YOUR_IP:8000
  └─ Test layout and touch interactions

  METHOD 3: Manual Resize
  ├─ Open browser window
  ├─ Drag window edge to simulate different widths
  └─ Test breakpoints: 768px, 1024px, 1440px

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📁 FILES USED:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  responsive.html   - HTML structure with all responsive elements
  style.css         - CSS with percentage widths & media queries
  percentage.py     - This Python server script

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    print(info)


def main():
    """Main function to start the server"""
    # Display responsive design information
    display_responsive_info()

    # Get the current directory
    current_dir = os.getcwd()
    print(f"\n✓ Working Directory: {current_dir}")
    print(f"✓ Files Found:")
    if os.path.exists('responsive.html'):
        print(f"  ✓ responsive.html")
    if os.path.exists('style.css'):
        print(f"  ✓ style.css")
    if os.path.exists('percentage.py'):
        print(f"  ✓ percentage.py")

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
    print(f"📍 To find IP:    Run 'ipconfig' in PowerShell")
    print(f"🌐 Open browser:  http://localhost:{port}/responsive.html")
    print(f"\n💡 Press CTRL+C to stop the server")
    print(f"="*70 + "\n")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n🛑 Server stopped.")
        print("Thank you for testing responsive design!\n")
        httpd.server_close()
        sys.exit(0)


if __name__ == '__main__':
    main()
