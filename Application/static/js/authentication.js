document.addEventListener('DOMContentLoaded', function() {
    const signUpForm = document.querySelector('form');

    signUpForm.addEventListener('submit', (event) => {
        const password = document.getElementById('password');
        const confirmPassword = document.getElementById('confirmPassword');
        const warningDiv = document.querySelector('.warning');
        const warningList = document.querySelector('.warning ul');

        warningList.innerHTML = '';

        if (password.value.length < 8) {
            warningDiv.classList.remove('d-none');
            let listItem = document.createElement('li');
            listItem.textContent = 'Password must be longer than 8 characters';
            warningList.appendChild(listItem);
            event.preventDefault();
        }

        if ( confirmPassword.value !== password.value) {
            warningDiv.classList.remove('d-none');
            let listItem = document.createElement('li');
            listItem.textContent = 'Password mismatch';
            warningList.appendChild(listItem);
            event.preventDefault();
        }
    });
});