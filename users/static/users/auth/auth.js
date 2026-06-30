// -------------------- LOGIN --------------------

function togglePassword() {
    const pwd = document.getElementById("id_password");

    if (!pwd) return;

    const btn = document.querySelector(".eye-btn");
    const showing = pwd.type === "text";

    pwd.type = showing ? "password" : "text";
    btn.classList.toggle("shown", !showing);
}


// -------------------- REGISTER --------------------

document.addEventListener("DOMContentLoaded", function () {

    const form = document.getElementById("registerForm");

    // Stop here if we're not on the register page
    if (!form) return;

    const passwordInputs = document.querySelectorAll('input[type="password"]');

    passwordInputs.forEach(function (input) {

        const wrap = document.createElement('div');
        wrap.className = 'password-wrap';

        input.parentNode.insertBefore(wrap, input);
        wrap.appendChild(input);

        input.classList.add('pw-input');

        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'eye-btn';
        btn.setAttribute('aria-label', 'Show password');

        btn.innerHTML =
            '<svg class="eye-on" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7Z"/><circle cx="12" cy="12" r="3"/></svg>' +
            '<svg class="eye-off" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M3 3l18 18M10.6 10.6a2 2 0 0 0 2.8 2.8M9.9 5.1A10.6 10.6 0 0 1 12 5c7 0 11 7 11 7a13.2 13.2 0 0 1-3 3.4M6.1 6.6C3.6 8.3 1 12 1 12s4 7 11 7c1.2 0 2.3-.2 3.4-.5"/></svg>';

        btn.addEventListener('click', function () {
            const showing = input.type === 'text';
            input.type = showing ? 'password' : 'text';
            btn.classList.toggle('shown', !showing);
        });

        wrap.appendChild(btn);
    });

    const mismatchMsg = document.getElementById('mismatchMsg');

    form.addEventListener('submit', function (e) {

        if (passwordInputs[0].value !== passwordInputs[1].value) {
            e.preventDefault();
            mismatchMsg.style.display = 'block';
        } else {
            mismatchMsg.style.display = 'none';
        }

    });

});