// Check if the user is not logged in
if (!userIsLoggedIn()) {
    window.location.href = "login.html"; // Redirect to the login page
}

function userIsLoggedIn() {
    // Implement your authentication check logic here
    // For example, check if the user has a valid session, token, or cookie
    // Return true if the user is logged in, otherwise false
}
