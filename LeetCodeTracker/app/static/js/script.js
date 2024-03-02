document.addEventListener("DOMContentLoaded", () => {
    // Example: Add event listeners or interactivity here
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", (e) => {
            // Perform input validation or preprocessing here
        });
    }

    // Similarly for other forms or interactive elements
});
document.addEventListener("DOMContentLoaded", function() {
    loadUserProgress();

    function loadUserProgress() {
        // Assuming user_id is available
        const userId = 1; // Example user ID
        fetch(`/api/user_progress/${userId}`)
            .then(response => response.json())
            .then(data => {
                console.log(data); // Log data or use it to update the DOM
                // Update the DOM with user progress data
            })
            .catch(error => console.error('Error fetching user progress:', error));
    }
});
