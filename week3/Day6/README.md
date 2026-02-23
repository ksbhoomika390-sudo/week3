# JavaScript Basics Tutorial - Day 6

Learn JavaScript fundamentals with interactive examples: **Alert**, **Form Validation**, **Calculator**, and **Text Change**.

## 📚 What You'll Learn

### 1️⃣ Alert on Button Click
- Display pop-up messages to users
- Use `alert()` function
- Handle button click events with `onclick`

### 2️⃣ Change Text on Click
- Manipulate DOM with `textContent`
- Change CSS styles dynamically with `.style`
- Track state with variables
- Create interactive text elements

### 3️⃣ Form Validation
- Validate user input before submission
- Regular expressions (Regex) for pattern matching
- Real-time validation on blur events
- Display error messages
- Show success messages

**Validations included:**
- ✓ Name: Min 3 characters, letters only
- ✓ Email: Valid email format
- ✓ Phone: Exactly 10 digits
- ✓ Password: Min 6 characters
- ✓ Terms: Checkbox must be checked

### 4️⃣ Simple Calculator
- Perform basic math operations (+, -, *, /)
- Prevent invalid inputs (multiple operators, decimals)
- Display calculation history
- Handle errors gracefully

## 📁 Files Included

```
Day6/
├── index.html       # HTML structure
├── script.js        # All JavaScript code
├── style.css        # Styling & responsive design
├── app.py           # Python HTTP server
└── README.md        # This file
```

## 🚀 Quick Start

### Step 1: Navigate to Day6
```bash
cd e:\internshipbhoomi\week3\Day6
```

### Step 2: Start the Server
```bash
python app.py
```

### Step 3: Open in Browser
- Local: `http://localhost:8000`
- Or: `http://localhost:8000/index.html`

## 💻 Code Examples

### Alert on Button Click
```javascript
function showAlert() {
    alert('Hello! This is an alert message!');
}
```

```html
<button onclick="showAlert()">Click Me</button>
```

### Change Text
```javascript
function changeText() {
    const element = document.getElementById('myText');
    element.textContent = 'Text has been changed!';
    element.style.color = 'red';
}
```

### Form Validation
```javascript
function validateForm(event) {
    event.preventDefault(); // Stop form submission
    
    const email = document.getElementById('email').value;
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    
    if (!emailRegex.test(email)) {
        alert('Invalid email!');
        return false;
    }
    
    // Form is valid
    alert('Form submitted successfully!');
}
```

```html
<form onsubmit="validateForm(event)">
    <input type="email" id="email" required>
    <button type="submit">Submit</button>
</form>
```

### Simple Calculator
```javascript
let display = '';

function appendNumber(num) {
    display += num;
    document.getElementById('calc').value = display;
}

function calculateResult() {
    const result = eval(display);
    display = result.toString();
    document.getElementById('calc').value = display;
}

function clearCalculator() {
    display = '';
    document.getElementById('calc').value = '0';
}
```

## 🔑 Key JavaScript Concepts

### 1. Functions
```javascript
function myFunction() {
    // Code here
}

// With parameters
function greet(name) {
    console.log('Hello ' + name);
}

// With return value
function add(a, b) {
    return a + b;
}
```

### 2. DOM Manipulation
```javascript
// Get elements
const elem = document.getElementById('myId');
const elems = document.querySelectorAll('.className');

// Change content
elem.textContent = 'New text';
elem.innerHTML = '<b>Bold text</b>';

// Change styles
elem.style.color = 'red';
elem.style.fontSize = '20px';

// Add/Remove classes
elem.classList.add('active');
elem.classList.remove('hidden');
```

### 3. Events
```javascript
// Using onclick attribute
<button onclick="myFunction()">Click</button>

// Using addEventListener
const btn = document.getElementById('myBtn');
btn.addEventListener('click', function() {
    alert('Button clicked!');
});

// Event types: click, blur, focus, submit, change, etc.
```

### 4. Conditional Logic
```javascript
// if/else
if (age >= 18) {
    console.log('Adult');
} else {
    console.log('Minor');
}

// Ternary operator
const status = age >= 18 ? 'Adult' : 'Minor';

// Logical operators
if (age >= 18 && hasLicense) {
    // Can drive
}
```

### 5. Regular Expressions (Regex)
```javascript
// Email validation
const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
if (emailRegex.test(email)) {
    console.log('Valid email');
}

// Phone validation (10 digits)
const phoneRegex = /^[0-9]{10}$/;
if (phoneRegex.test(phone)) {
    console.log('Valid phone');
}

// Name validation (letters and spaces only)
const nameRegex = /^[a-zA-Z\s]+$/;
```

### 6. String Methods
```javascript
const str = '  Hello World  ';
str.trim();              // Remove spaces
str.toLowerCase();       // Convert to lowercase
str.includes('Hello');   // Check if contains
str.replace('World', 'JavaScript'); // Replace
str.substring(0, 5);     // Get substring
```

## 🎯 Features Demonstrated

### Alert Section
- Single button click event
- Alert dialog box
- User interaction

### Text Change Section
- DOM element selection
- textContent property
- Dynamic CSS changes
- State tracking with variables

### Form Validation Section
- Form submission event
- Input field access
- Form reset functionality
- Error message display
- Real-time validation (blur events)
- Multiple validation rules
- Success message feedback

### Calculator Section
- Number input
- Operator handling
- Mathematical evaluation
- Expression history tracking
- Error handling
- Decimal point management

## 🧪 Testing Tips

1. **Browser Console (F12)**
   - Check for errors
   - See console logs
   - Debug functions
   - Test code snippets

2. **Mobile Testing**
   - Press F12 → Toggle Device Toolbar (Ctrl+Shift+M)
   - Test on iPhone, iPad, Android devices
   - Check touch interactions

3. **Form Testing**
   - Try invalid inputs (short names, wrong email format)
   - See real-time validation messages
   - Submit valid form to see success message

4. **Calculator Testing**
   - Try different calculations
   - Check error handling (multiple operators)
   - View calculation history

## 📋 Common JavaScript Mistakes to Avoid

1. **Forgetting `event.preventDefault()`**
   ```javascript
   // Wrong - form will submit normally
   function validateForm(event) {
       // validation code
   }
   
   // Correct
   function validateForm(event) {
       event.preventDefault(); // Stop default behavior
       // validation code
   }
   ```

2. **Using `innerHTML` with user input** (Security risk)
   ```javascript
   // Avoid
   elem.innerHTML = userInput; // Can execute scripts
   
   // Better
   elem.textContent = userInput; // Safe, just text
   ```

3. **Forgetting `.trim()` on input**
   ```javascript
   // Avoid
   const name = document.getElementById('name').value;
   if (name.length < 3) { } // Won't work if spaces at start/end
   
   // Better
   const name = document.getElementById('name').value.trim();
   ```

4. **Using `var` instead of `let/const`**
   ```javascript
   // Avoid (old way)
   var x = 10;
   
   // Prefer (modern way)
   let y = 10;    // Can be reassigned
   const z = 10;  // Cannot be reassigned
   ```

5. **Not handling async operations**
   ```javascript
   // Will fail - result not ready yet
   const data = fetch(url);
   console.log(data);
   
   // Correct - use async/await
   async function getData() {
       const data = await fetch(url);
       console.log(data);
   }
   ```

## 🎓 Next Steps

### Enhance the Project
1. Add more operators to calculator (%, square root, etc.)
2. Add username validation (alphanumeric + underscore)
3. Create a login/logout system with form validation
4. Build a to-do list with local storage
5. Create a quiz application with scoring
6. Add dark mode toggle
7. Implement keyboard support for calculator

### Learn More JavaScript
1. Async/Await & Promises
2. API calls with fetch()
3. Array methods (map, filter, reduce)
4. ES6 Classes & OOP
5. Closures & Scope
6. Hoisting & Temporal Dead Zone
7. Prototypes & Inheritance

## 🐛 Debug Common Issues

**Alert not showing?**
- Check if function name matches in HTML
- Verify browser allows popups
- Check browser console for errors (F12)

**Form validation not working?**
- Ensure `event.preventDefault()` is called
- Check regex patterns are correct
- Verify element IDs match in HTML and JS

**Calculator giving wrong results?**
- Check for extra spaces in expression
- Ensure operators are valid (+, -, *, /)
- Look for JavaScript errors in console

**Text not changing?**
- Confirm element ID exists in HTML
- Check if element is loaded before script runs
- Verify `.textContent` or `.innerHTML` is used

## 📞 Quick Reference

### DOM Methods
```javascript
document.getElementById('id')              // Get by ID
document.querySelector('.class')           // Get by selector
document.querySelectorAll('.class')        // Get all matching
document.getElementsByTagName('div')       // Get by tag
```

### Event Listeners
```javascript
addEventListener('click', callback)
addEventListener('submit', callback)
addEventListener('blur', callback)
addEventListener('focus', callback)
addEventListener('change', callback)
addEventListener('keyup', callback)
addEventListener('mouseenter', callback)
addEventListener('mouseleave', callback)
```

### String Methods
```javascript
trim(), toLowerCase(), toUpperCase()
includes(), startsWith(), endsWith()
replace(), split(), substring()
charAt(), indexOf(), lastIndexOf()
```

### Array Methods
```javascript
push(), pop(), shift(), unshift()
map(), filter(), reduce()
forEach(), find(), findIndex()
slice(), splice(), concat()
includes(), some(), every()
```

## 🎉 Congratulations!

You now understand the fundamentals of JavaScript:
- ✅ Functions and event handling
- ✅ DOM manipulation
- ✅ Form validation with regex
- ✅ Building interactive components
- ✅ Error handling and user feedback

Keep practicing and building more JavaScript projects! 🚀

---

**Created:** February 23, 2026
**Purpose:** JavaScript Basics Tutorial
**Status:** Ready to learn and practice
