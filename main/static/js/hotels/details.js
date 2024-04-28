function clearFilters() {
    // Set the value of all form fields to an empty string
    document.getElementById('start_date').value = '';
    document.getElementById('end_date').value = '';

    // Submit the form to apply the changes
    document.forms[0].submit();
}