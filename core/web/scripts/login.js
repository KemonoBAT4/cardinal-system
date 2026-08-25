
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

// dashboard base page script
document.addEventListener('DOMContentLoaded', () => {
    console.log('Web application initialized');

    const form = document.querySelector('.login-form');

    form.addEventListener('submit', async (event) => {
        event.preventDefault();

        let response = await fetch("/auth/login", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body : JSON.stringify({
                username: document.querySelector('#username').value,
                password: document.querySelector('#password').value
            })
        }).then(response => response.json());

        if (response.status == true) {
            window.location.href = "/home";
        } else {
            showToast(response.message);
        }
    });
});
