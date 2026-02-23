/* ===== JAVASCRIPT BASICS ===== */

// ============================================
// 1. ALERT ON BUTTON CLICK
// ============================================
function showAlert() {
    alert('🎉 Hello! This is an alert message!\n\nAlerts are used to display important information to users.');
}

// ============================================
// 2. CHANGE TEXT ON CLICK
// ============================================
let textState = false; // Track whether text has been changed

function changeText() {
    const textElement = document.getElementById('changeText');
    
    if (!textState) {
        textElement.textContent = '✨ Text has been changed! Click again to change it more.';
        textElement.style.color = '#e74c3c';
        textElement.style.fontWeight = 'bold';
        textState = true;
    } else {
        textElement.textContent = '🔄 Changed again! JavaScript is powerful!';
        textElement.style.color = '#2ecc71';
        textState = true;
    }
}

function resetText() {
    const textElement = document.getElementById('changeText');
    textElement.textContent = 'Original Text - Click Me to Change!';
    textElement.style.color = '#333';
    textElement.style.fontWeight = 'normal';
    textState = false;
}

// ============================================
// 3. FORM VALIDATION
// ============================================

function validateForm(event) {
    event.preventDefault(); // Prevent form submission

    // Get form values
    const fullname = document.getElementById('fullname').value.trim();
    const email = document.getElementById('email').value.trim();
    const phone = document.getElementById('phone').value.trim();
    const password = document.getElementById('password').value;
    const terms = document.getElementById('terms').checked;

    // Clear all error messages
    clearErrorMessages();

    // Validation flags
    let isValid = true;

    // Validate Full Name (at least 3 characters, only letters and spaces)
    if (fullname.length < 3) {
        showError('nameError', 'Name must be at least 3 characters long');
        isValid = false;
    } else if (!/^[a-zA-Z\s]+$/.test(fullname)) {
        showError('nameError', 'Name can only contain letters and spaces');
        isValid = false;
    }

    // Validate Email
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        showError('emailError', 'Please enter a valid email address');
        isValid = false;
    }

    // Validate Phone (10 digits)
    const phoneRegex = /^[0-9]{10}$/;
    if (!phoneRegex.test(phone)) {
        showError('phoneError', 'Phone number must be exactly 10 digits');
        isValid = false;
    }

    // Validate Password (minimum 6 characters)
    if (password.length < 6) {
        showError('passwordError', 'Password must be at least 6 characters long');
        isValid = false;
    }

    // Validate Terms & Conditions
    if (!terms) {
        showError('termsError', 'You must agree to Terms & Conditions');
        isValid = false;
    }

    // If all validations pass
    if (isValid) {
        showFormSuccess(fullname);
        document.getElementById('validationForm').reset();
    }
}

// Helper function to show error messages
function showError(elementId, message) {
    const errorElement = document.getElementById(elementId);
    errorElement.textContent = '❌ ' + message;
    errorElement.style.display = 'block';
}

// Helper function to clear all error messages
function clearErrorMessages() {
    const errorElements = document.querySelectorAll('.error-msg');
    errorElements.forEach(element => {
        element.textContent = '';
        element.style.display = 'none';
    });
}

// Helper function to show success message
function showFormSuccess(name) {
    const successElement = document.getElementById('formSuccess');
    successElement.textContent = `✅ Success! Welcome, ${name}! Your form has been submitted successfully.`;
    successElement.style.display = 'block';

    // Hide success message after 5 seconds
    setTimeout(() => {
        successElement.style.display = 'none';
        successElement.textContent = '';
    }, 5000);
}

// Real-time validation on input
document.addEventListener('DOMContentLoaded', function() {
    // Name validation
    const nameInput = document.getElementById('fullname');
    if (nameInput) {
        nameInput.addEventListener('blur', function() {
            const value = this.value.trim();
            if (value && (value.length < 3 || !/^[a-zA-Z\s]+$/.test(value))) {
                showError('nameError', 'Name must be at least 3 characters (letters only)');
            } else {
                document.getElementById('nameError').textContent = '';
            }
        });
    }

    // Email validation
    const emailInput = document.getElementById('email');
    if (emailInput) {
        emailInput.addEventListener('blur', function() {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (this.value && !emailRegex.test(this.value)) {
                showError('emailError', 'Invalid email format');
            } else {
                document.getElementById('emailError').textContent = '';
            }
        });
    }

    // Phone validation
    const phoneInput = document.getElementById('phone');
    if (phoneInput) {
        phoneInput.addEventListener('blur', function() {
            const phoneRegex = /^[0-9]{10}$/;
            if (this.value && !phoneRegex.test(this.value)) {
                showError('phoneError', 'Phone must be 10 digits');
            } else {
                document.getElementById('phoneError').textContent = '';
            }
        });
    }

    // Password validation
    const passwordInput = document.getElementById('password');
    if (passwordInput) {
        passwordInput.addEventListener('blur', function() {
            if (this.value && this.value.length < 6) {
                showError('passwordError', 'Password must be at least 6 characters');
            } else {
                document.getElementById('passwordError').textContent = '';
            }
        });
    }
});

// ============================================
// 4. SIMPLE CALCULATOR
// ============================================

let calculatorDisplay = '';
let calculatorHistory = [];

function appendNumber(num) {
    const display = document.getElementById('calculatorDisplay');
    calculatorDisplay += num;
    display.value = calculatorDisplay;
}

function appendOperator(op) {
    const display = document.getElementById('calculatorDisplay');
    
    // Prevent multiple operators in a row
    if (calculatorDisplay && !calculatorDisplay.endsWith('+') && 
        !calculatorDisplay.endsWith('-') && !calculatorDisplay.endsWith('*') && 
        !calculatorDisplay.endsWith('/')) {
        calculatorDisplay += op;
        display.value = calculatorDisplay;
    }
}

function appendDecimal(decimal) {
    const display = document.getElementById('calculatorDisplay');
    
    // Prevent multiple decimals in one number
    const lastOperatorIndex = Math.max(
        calculatorDisplay.lastIndexOf('+'),
        calculatorDisplay.lastIndexOf('-'),
        calculatorDisplay.lastIndexOf('*'),
        calculatorDisplay.lastIndexOf('/')
    );
    
    const currentNumber = calculatorDisplay.substring(lastOperatorIndex + 1);
    
    if (!currentNumber.includes(decimal)) {
        calculatorDisplay += decimal;
        display.value = calculatorDisplay;
    }
}

function deleteLastChar() {
    const display = document.getElementById('calculatorDisplay');
    calculatorDisplay = calculatorDisplay.slice(0, -1);
    display.value = calculatorDisplay;
}

function clearCalculator() {
    calculatorDisplay = '';
    document.getElementById('calculatorDisplay').value = '0';
}

function calculateResult() {
    const display = document.getElementById('calculatorDisplay');
    
    try {
        // Evaluate the expression
        const result = eval(calculatorDisplay);
        
        if (isFinite(result)) {
            // Store in history
            calculatorHistory.push(`${calculatorDisplay} = ${result}`);
            
            // Show in display
            calculatorDisplay = result.toString();
            display.value = calculatorDisplay;
            
            // Update history (show last 5 calculations)
            updateCalculatorHistory();
        } else {
            display.value = 'Error';
            calculatorDisplay = '';
        }
    } catch (error) {
        display.value = 'Error';
        calculatorDisplay = '';
    }
}

function updateCalculatorHistory() {
    const historyElement = document.getElementById('calcResult');
    const recentHistory = calculatorHistory.slice(-5).reverse();
    
    historyElement.innerHTML = '<strong>Last 5 Calculations:</strong><br>' + 
                              recentHistory.map((calc, index) => 
                                   `<div class="history-item">${index + 1}. ${calc}</div>`
                              ).join('');
}

// ============================================
// 5. INTERACTIVE DEMO
// ============================================

let demoCount = 0;
const demoMessages = [
    '👋 Hello! I\'m a button!',
    '🎯 You clicked me once!',
    '😊 Great job! Clicking again?',
    '🚀 You\'re getting the hang of this!',
    '💡 JavaScript makes things interactive!',
    '⭐ You\'re awesome! Keep learning!',
    '🎓 Master JavaScript and build amazing things!'
];

function interactiveDemo() {
    demoCount++;
    const demoMessage = document.getElementById('demoMessage');
    const demoBtn = document.querySelector('.btn-demo');
    
    // Show message
    const messageIndex = (demoCount - 1) % demoMessages.length;
    demoMessage.textContent = demoMessages[messageIndex];
    
    // Add animation effect
    demoBtn.style.transform = 'scale(0.95)';
    setTimeout(() => {
        demoBtn.style.transform = 'scale(1)';
    }, 100);
    
    // Change button color based on clicks
    const colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12', '#9b59b6', '#1abc9c'];
    const colorIndex = (demoCount - 1) % colors.length;
    demoBtn.style.backgroundColor = colors[colorIndex];
    demoBtn.style.boxShadow = `0 4px 15px ${colors[colorIndex]}80`;
    
    // Update button text
    document.getElementById('demoText').textContent = `Clicked ${demoCount} times!`;
}

// ============================================
// INITIALIZATION
// ============================================

console.log('%c=== JavaScript Basics ===', 'color: #3498db; font-size: 16px; font-weight: bold;');
console.log('%cAlert, Form Validation, Calculator, Text Change', 'color: #e74c3c; font-size: 12px;');
console.log('%cAll four concepts demonstrated in this page!', 'color: #2ecc71; font-size: 11px;');
