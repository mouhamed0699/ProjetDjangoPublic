document.addEventListener("DOMContentLoaded", function() {
    var reservationButtons = document.querySelectorAll(".btn");
    var cancelButtons = document.querySelectorAll(".annuler");

    for (var i = 0; i < reservationButtons.length; i++) {
        reservationButtons[i].addEventListener("click", function(event) {
            var formId = this.getAttribute("data-form-id");
            var form = document.getElementById(formId);

            if (form) {
                form.style.display = "block";
            }
        });
    }

    for (var i = 0; i < cancelButtons.length; i++) {
        cancelButtons[i].addEventListener("click", function(event) {
            event.preventDefault();

            var form = this.closest("form");
            form.style.display = "none";
        });
    }
});



// function(event, uri, storage_url, token) {
//     if (uri == null) {
//       uri = null
//     }
//     if (storage_url == null) {
//       storage_url = null
//     }
//     if (token == null) {
//       token = null
//     }
//     return StudentNotes.prototype.onInitNotes.apply(_this, arguments)
//   }