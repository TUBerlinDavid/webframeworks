document.addEventListener('DOMContentLoaded', function() {
    let deleteButtons = document.querySelectorAll('.action-delete');
    for (i = 0; i < deleteButtons.length; i++) {
        deleteButtons[i].addEventListener('click', function(e) {
            let link = e.target.closest("a[data-id]");
            if (!confirm('Are you sure to delete ToDo #' + link.dataset.id + '?')) {
                e.preventDefault();
            }
        });
    }
}, false);