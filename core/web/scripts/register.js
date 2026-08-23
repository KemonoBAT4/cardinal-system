
const form = document.querySelector('.register-form');
const password = document.getElementById('password');
const passwordConfirm = document.getElementById('password_confirm');

form.addEventListener('submit', function (event) {
    if (password.value !== passwordConfirm.value) {
        event.preventDefault();

        passwordConfirm.setCustomValidity('Passwords do not match.');
        passwordConfirm.reportValidity();
    } else {
        passwordConfirm.setCustomValidity('');
    }
});

passwordConfirm.addEventListener('input', function () {
    if (password.value !== passwordConfirm.value) {
        passwordConfirm.setCustomValidity('Passwords do not match.');
    } else {
        passwordConfirm.setCustomValidity('');
    }
});