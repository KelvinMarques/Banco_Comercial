function onFormSubmit(event) {
  event.preventDefault();
  
  const nome = document.querySelector('input[name="nome"]').value;
  const email = document.querySelector('input[name="email"]').value;
  const telefone = document.querySelector('input[name="tel"]').value;
  const senha = document.querySelector('input[name="senha"]').value;
  const confirmarSenha = document.querySelector('input[name="confirmar_senha"]').value;
  const rg = document.querySelector('input[name="rg"]').value;
  const cpf = document.querySelector('input[name="cpf"]').value;
  const data = document.querySelector('input[name="data"]').value;
  const cep = document.querySelector('input[name="cep"]').value;

  if (!nome || !email || !senha || !confirmarSenha || !cpf) {
      alert("Por favor, preencha todos os campos obrigatórios.");
      return;
  }

  if (senha !== confirmarSenha) {
      alert("As senhas não correspondem. Por favor, verifique.");
      return;
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!email.match(emailRegex)) {
      alert("Por favor, insira um endereço de e-mail válido.");
      return;
  }

  const cpfRegex = /^\d{11}$/;
  if (!cpf.match(cpfRegex)) {
      alert("Por favor, insira um CPF válido (apenas números).");
      return;
  }

  window.location.href = "../poscadastro/poscadastro.html";
}

document.getElementById("form").addEventListener("submit", onFormSubmit);
