"""
Week 3 - Mini Frontend Project
A complete web application with Home, Login, Registration, and Contact pages
Location: Day7
Run: python app.py
"""

from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import re
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'week3_secret_key_12345'

# In-memory database (for demo purposes)
users_database = {
    'demo': {
        'password': 'demo123',
        'email': 'demo@example.com',
        'full_name': 'Demo User'
    }
}

contact_messages = []

# ===== HELPER FUNCTIONS =====
def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number (10 digits)"""
    return re.match(r'^[0-9]{10}$', phone.replace('-', '').replace(' ', '')) is not None

def validate_password(password):
    """Validate password strength"""
    if len(password) < 6:
        return False, "Password must be at least 6 characters"
    if not re.search(r'[A-Z]', password):
        return False, "Password must contain uppercase letter"
    if not re.search(r'[0-9]', password):
        return False, "Password must contain number"
    return True, "Valid"

# ===== ROUTES =====

@app.route('/')
def index():
    """Home page"""
    is_logged_in = 'username' in session
    username = session.get('username', None)
    return render_template('index.html', is_logged_in=is_logged_in, username=username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Registration page"""
    if request.method == 'POST':
        data = request.get_json()
        
        # Validate input
        full_name = data.get('full_name', '').strip()
        username = data.get('username', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '')
        confirm_password = data.get('confirm_password', '')
        
        errors = {}
        
        # Full name validation
        if not full_name:
            errors['full_name'] = 'Full name is required'
        elif len(full_name) < 3:
            errors['full_name'] = 'Name must be at least 3 characters'
        
        # Username validation
        if not username:
            errors['username'] = 'Username is required'
        elif len(username) < 3:
            errors['username'] = 'Username must be at least 3 characters'
        elif username in users_database:
            errors['username'] = 'Username already exists'
        
        # Email validation
        if not email:
            errors['email'] = 'Email is required'
        elif not validate_email(email):
            errors['email'] = 'Invalid email format'
        
        # Password validation
        if not password:
            errors['password'] = 'Password is required'
        else:
            is_valid, msg = validate_password(password)
            if not is_valid:
                errors['password'] = msg
        
        # Confirm password
        if password != confirm_password:
            errors['confirm_password'] = 'Passwords do not match'
        
        if errors:
            return jsonify({'success': False, 'errors': errors})
        
        # Register user
        users_database[username] = {
            'password': password,
            'email': email,
            'full_name': full_name
        }
        
        return jsonify({
            'success': True,
            'message': 'Registration successful! Please log in.'
        })
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login page"""
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '')
        
        errors = {}
        
        if not username:
            errors['username'] = 'Username is required'
        if not password:
            errors['password'] = 'Password is required'
        
        if errors:
            return jsonify({'success': False, 'errors': errors})
        
        # Check credentials
        if username in users_database:
            user = users_database[username]
            if user['password'] == password:
                session['username'] = username
                session['full_name'] = user['full_name']
                session['email'] = user['email']
                return jsonify({
                    'success': True,
                    'message': 'Login successful!',
                    'redirect': '/'
                })
            else:
                return jsonify({
                    'success': False,
                    'errors': {'password': 'Invalid password'}
                })
        else:
            return jsonify({
                'success': False,
                'errors': {'username': 'Username not found'}
            })
    
    is_logged_in = 'username' in session
    if is_logged_in:
        return redirect(url_for('index'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout"""
    session.clear()
    return redirect(url_for('index'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page"""
    if request.method == 'POST':
        data = request.get_json()
        
        full_name = data.get('full_name', '').strip()
        email = data.get('email', '').strip()
        phone = data.get('phone', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()
        
        errors = {}
        
        # Validation
        if not full_name:
            errors['full_name'] = 'Full name is required'
        elif len(full_name) < 3:
            errors['full_name'] = 'Name must be at least 3 characters'
        
        if not email:
            errors['email'] = 'Email is required'
        elif not validate_email(email):
            errors['email'] = 'Invalid email format'
        
        if not phone:
            errors['phone'] = 'Phone is required'
        elif not validate_phone(phone):
            errors['phone'] = 'Phone must be 10 digits'
        
        if not subject:
            errors['subject'] = 'Subject is required'
        
        if not message:
            errors['message'] = 'Message is required'
        elif len(message) < 10:
            errors['message'] = 'Message must be at least 10 characters'
        
        if errors:
            return jsonify({'success': False, 'errors': errors})
        
        # Save message
        contact_messages.append({
            'id': len(contact_messages) + 1,
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'subject': subject,
            'message': message,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })
        
        return jsonify({
            'success': True,
            'message': 'Thank you! We will contact you soon.'
        })
    
    is_logged_in = 'username' in session
    username = session.get('username', None)
    email = session.get('email', None) if is_logged_in else None
    full_name = session.get('full_name', None) if is_logged_in else None
    
    return render_template('contact.html', 
                         is_logged_in=is_logged_in, 
                         username=username,
                         email=email,
                         full_name=full_name)

# ===== ERROR HANDLERS =====

@app.errorhandler(404)
def page_not_found(error):
    """404 error handler"""
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """500 error handler"""
    return render_template('500.html'), 500

# ===== MAIN =====

if __name__ == '__main__':
    print("\n" + "="*70)
    print("🚀 WEEK 3 - MINI FRONTEND PROJECT")
    print("="*70)
    print("\n📚 Features:")
    print("  ✓ Home Page (index.html)")
    print("  ✓ Registration (register.html)")
    print("  ✓ Login (login.html)")
    print("  ✓ Contact (contact.html)")
    print("\n📊 Pages Available:")
    print("  • Home:     http://localhost:5000/")
    print("  • Register: http://localhost:5000/register")
    print("  • Login:    http://localhost:5000/login")
    print("  • Contact:  http://localhost:5000/contact")
    print("\n🔐 Demo Account:")
    print("  Username: demo")
    print("  Password: demo123")
    print("\n💡 Press CTRL+C to stop the server")
    print("="*70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
