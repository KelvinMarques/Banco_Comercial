function dados() {
  window.location.href = "{% url 'dados_view' %}";
}

// Função para redirecionar para a view de extrato
function extrato() {
  window.location.href = "{% url 'extrato_view' %}";
}

// Função para redirecionar para a view de pagar
function pagar() {
  window.location.href = "{% url 'pagar_view' %}";
}

// Função para redirecionar para a view de transferir
function transferir() {
  window.location.href = "{% url 'transferir_view' %}";
}

// Função para redirecionar para a view de investir
function investir() {
  window.location.href = "{% url 'investir_view' %}";
}

// Função para redirecionar para a view de empréstimo
function emprestimo() {
  window.location.href = "{% url 'emprestimo_view' %}";
}

// Função para redirecionar para a view de saldo
function saldo() {
  window.location.href = "{% url 'saldo_view' %}";
}

// Função para redirecionar para a view de notificações
function notificacoes() {
  window.location.href = "{% url 'notificacoes_view' %}";
}

// Função para redirecionar para a view de configurações
function configuracoes() {
  window.location.href = "{% url 'configuracoes_view' %}";
}

// Função para redirecionar para a view de cartões
function cartoes() {
  window.location.href = "{% url 'cartoes_view' %}";
}

  document.addEventListener("DOMContentLoaded", function() {

    var trocar = document.getElementById("btn_access");
  
        trocar.addEventListener("click", function() {
            window.location.href = "{% url 'login_view' %}";
    });
  });