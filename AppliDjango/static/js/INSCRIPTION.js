
document.addEventListener('DOMContentLoaded', function() {
    var formulaire = document.querySelector('.for');
    var passwordInput = formulaire.elements['password1'];
    var confirmPasswordInput = formulaire.elements['password2'];
    var errorMessage = document.querySelector('.err');
  
    formulaire.addEventListener('submit', function(event) {
      event.preventDefault();
  
      var password = passwordInput.value;
      var confirmPassword = confirmPasswordInput.value;
  
      if (password !== confirmPassword) {
        errorMessage.style.display = 'block';
      } else {
        // Soumettre le formulaire ou effectuer toute autre action souhaitée
        formulaire.submit();
        console.log('Formulaire soumis');
      }
    });
  });



