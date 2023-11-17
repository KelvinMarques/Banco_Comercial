document.addEventListener("DOMContentLoaded", function() {
    // Use um seletor mais específico para garantir que você está capturando o botão correto.
    var cadaster = document.getElementById("create_account");

    if (cadaster) {
        cadaster.addEventListener("click", function() {
            // Use a função {% url %} do Django para construir a URL reversa.
            window.location.href = "{% url 'contas:cadastro_view' %}";
        });
    }else{
        console.error("Elemento 'create_account' não encontrado.");
    }
});

function onFormSubmit(event) {
    event.preventDefault();
    
    // Atualize os seletores para coincidir com os campos do formulário gerado por Django.
    const nome = document.querySelector('input[name="input_email"]').value;
    const senha = document.querySelector('input[name="input_password"]').value;
    
    // Use a função {% url %} do Django para construir a URL reversa.
    window.location.href = "{% url 'dashboard:dashboard_view' %}";
}

// Atualize o ID do formulário para coincidir com o gerado por Django.
document.getElementById("form").addEventListener("submit", onFormSubmit);
