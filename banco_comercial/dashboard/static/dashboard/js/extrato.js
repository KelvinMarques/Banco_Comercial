// Função para redirecionar para a view de dados
function dados() {
  window.location.href = "/client/dados/";
}

// Função para redirecionar para a view de extrato
function extrato() {
  window.location.href = "/client/extrato/";
}

// Função para redirecionar para a view de pagar
function pagar() {
  window.location.href = "/client/pagar/";
}

// Função para redirecionar para a view de transferir
function transferir() {
  window.location.href = "/client/transferir/";
}

// Função para redirecionar para a view de investir
function investir() {
  window.location.href = "/client/investir/";
}

// Função para redirecionar para a view de empréstimo
function emprestimo() {
  window.location.href = "/client/emprestimo/";
}

// Função para redirecionar para a view de saldo
function saldo() {
  window.location.href = "/client/saldo/";
}

// Função para redirecionar para a view de notificações
function notificacoes() {
  window.location.href = "/client/notificacoes/";
}

// Função para redirecionar para a view de configurações
function configuracoes() {
  window.location.href = "/client/configuracoes/";
}

// Função para redirecionar para a view de cartões
function cartoes() {
  window.location.href = "/client/cartoes/";
}

document.addEventListener("DOMContentLoaded", function() {
  var trocar = document.getElementById("btn_access");

  trocar.addEventListener("click", function() {
      window.location.href = "/user/login/";
  });
});
