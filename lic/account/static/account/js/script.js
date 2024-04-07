document.addEventListener('DOMContentLoaded', function() {
    let closeButtons = document.querySelectorAll('.close-btn');
    closeButtons.forEach(function(button) {
        button.addEventListener('click', function(e) {
            e.preventDefault();
            let li = this.closest('li');
            if (li) {
                li.remove();
            }
        });
    });
});