function updateUser(field, value) {
    // Make an AJAX request to update user data
    // Replace this with your actual implementation
    console.log('Updating ' + field + ' to ' + value);
}

// Add event listeners for inline editing
document.querySelectorAll('.editable').forEach(function(element) {
    element.addEventListener('blur', function() {
        var field = this.id;
        var value = this.innerText.trim();
        updateUser(field, value);
    });
});