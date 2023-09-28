
// Password visibility toggle
const passwordInput = document.getElementById("password");
const confirmPasswordInput = document.getElementById("confirmPassword");
const showPasswordCheckbox = document.getElementById("showPassword");
const errorMessage = document.getElementById("error-message");

showPasswordCheckbox.addEventListener("change", function () {
    if (showPasswordCheckbox.checked) {
        passwordInput.type = "text";
        confirmPasswordInput.type = "text";
    } else {
        passwordInput.type = "password";
        confirmPasswordInput.type = "password";
    }
});

function validateForm() {
    const password = passwordInput.value;
    const confirmPassword = confirmPasswordInput.value;

    if (password !== confirmPassword) {
        errorMessage.textContent = "Passwords do not match!";
        return false; // Prevent form submission
    } else {
        errorMessage.textContent = "";
        return true; // Allow form submission
    }
}