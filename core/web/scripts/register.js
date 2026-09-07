
const form = document.querySelector('.register-form');
const password = document.getElementById('password');
const passwordConfirm = document.getElementById('password_confirm');

function showToast(message) {
    const container = document.getElementById('toast-container');

    const toast = document.createElement('div');
    toast.className = 'toast';

    toast.innerHTML = `
        <div class="toast-icon">!</div>
        <div class="toast-message">${message}</div>
    `;

    container.appendChild(toast);

    setTimeout(() => {
        toast.remove();
    }, 5000);
}

async function send_register() {
    let response = await fetch("/auth/register", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            first_name: document.querySelector('#first_name').value,
            last_name: document.querySelector('#last_name').value,
            username: document.querySelector('#username').value,
            email: document.querySelector('#email').value,
            password: document.querySelector('#password').value,
        }),
    }).then(response => response.json());

    if (response.status == true) {
        window.location.href = "/home";
    } else {
        showToast(response.message);
    }
}

form.addEventListener('submit', function (event) {
    event.preventDefault();
    if (password.value !== passwordConfirm.value) {

        passwordConfirm.setCustomValidity('Passwords do not match.');
        passwordConfirm.reportValidity();
    } else {
        passwordConfirm.setCustomValidity('');
        send_register();
    }
});

passwordConfirm.addEventListener('input', function () {
    if (password.value !== passwordConfirm.value) {
        passwordConfirm.setCustomValidity('Passwords do not match.');
    } else {
        passwordConfirm.setCustomValidity('');
    }
});
