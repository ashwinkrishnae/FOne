document.addEventListener("DOMContentLoaded", function () {
    const passwordToggles = document.querySelectorAll('[data-toggle-password]');

    passwordToggles.forEach(function (toggle) {
        const toggleHandler = function (event) {
            event.preventDefault();
            event.stopPropagation();

            const wrapper = this.closest('.password-wrapper');
            const input = wrapper ? wrapper.querySelector('input[type="password"], input[type="text"]') : null;
            const icon = this.querySelector('.eye-icon');

            if (!input || !icon) {
                return;
            }

            const isPassword = input.type === "password";
            input.type = isPassword ? "text" : "password";
            this.setAttribute("aria-label", isPassword ? "Hide password" : "Show password");
            icon.textContent = isPassword ? "🙈" : "👁";
        };

        toggle.addEventListener("click", toggleHandler);
        toggle.addEventListener("keydown", function (event) {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                toggleHandler.call(this, event);
            }
        });
    });
});
