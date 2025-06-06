document.addEventListener('DOMContentLoaded', () => {
    // Hamburger menu logic
    const hamburger = document.getElementById('hamburger');
    const mobileMenu = document.getElementById('mobileMenu');
    const closeMenu = document.getElementById('closeMenu');

    if (hamburger && mobileMenu && closeMenu) {
        hamburger.addEventListener('click', () => {
            mobileMenu.classList.add('open');
        });
        closeMenu.addEventListener('click', () => {
            mobileMenu.classList.remove('open');
        });
        // Optional: close menu if clicking outside menu content
        mobileMenu.addEventListener('click', (e) => {
            if (e.target === mobileMenu) {
                mobileMenu.classList.remove('open');
            }
        });
    }

    // Waitlist form logic (existing)
    const form = document.getElementById('waitlist-form');
    const emailInput = document.getElementById('email');
    const formMessage = document.getElementById('form-message');
    const SHEETDB_API_URL = 'https://sheetdb.io/api/v1/ozh2aa4b5rh9f';

    if (form) {
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const email = emailInput.value.trim();
            if (!email) {
                showMessage('Please enter your email address.', 'error');
                return;
            }
            if (!isValidEmail(email)) {
                showMessage('Please enter a valid email address.', 'error');
                return;
            }
            try {
                const response = await fetch(SHEETDB_API_URL, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        data: [{ email: email }]
                    })
                });
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const result = await response.json();
                if (result.created === 1) {
                    showMessage('Thanks for joining! We\'ll keep you updated.', 'success');
                    form.reset();
                } else {
                    throw new Error('Failed to add email to waitlist');
                }
            } catch (error) {
                console.error('Error:', error);
                showMessage('Something went wrong. Please try again.', 'error');
            }
        });
    }

    function showMessage(message, type) {
        if (formMessage) {
            formMessage.textContent = message;
            formMessage.style.color = type === 'error' ? '#ef4444' : '#10b981';
        }
    }

    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }
}); 