document.addEventListener("DOMContentLoaded", function() {

    var cadaster = document.getElementById("create_account");

        cadaster.addEventListener("click", function() {
            window.location.href = "/tela de cadastro/cadastro.html";
    });
});

function onFormSubmit(event) {
    event.preventDefault();
    
    const nome = document.querySelector('input[name="input_email"]').value;
    const email = document.querySelector('input[name="input_password"]').value;
    window.location.href = "../dashboard/dashboard.html";
  }
  document.getElementById("form").addEventListener("submit", onFormSubmit);