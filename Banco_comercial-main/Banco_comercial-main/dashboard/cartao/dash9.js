function dados() {
    window.location.href = '/dashboard/dashboard2/dashboard2.html';
  }
  
  function extrato() {
    window.location.href = '/dashboard/extrato/dashboard4.html';
  }
  
  function pagar() {
    window.location.href = '/dashboard/pagar/dashboard5.html';
  }
  
  function transferir() {
    window.location.href = '/dashboard/transferir/dashboard6.html';
  }
  
  function investir() {
    window.location.href = '/dashboard/investir/dashboard8.html';
  }
  
  function emprestimo() {
    window.location.href = '/dashboard/emprestimo/dashboard7.html';
  }
  
  function saldo() {
    window.location.href = '/dashboard/principal/dashboard1.html';
  }
  
  function notificacoes() {
    window.location.href = '/dashboard/notificacoes/dashboard10.html';
  }
  
  function configuracoes() {
    window.location.href = '/dashboard/configurar/dashboard3.html';
  }
  
  function cartoes() {
    window.location.href = '/dashboard/cartao/dashboard9.html';
  }

  document.addEventListener("DOMContentLoaded", function() {

    var trocar = document.getElementById("btn_access");
  
        trocar.addEventListener("click", function() {
            window.location.href = "/tela de login/login.html";
    });
  });