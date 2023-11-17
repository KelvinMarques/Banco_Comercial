document.addEventListener("DOMContentLoaded", function() {
    var redirectButton = document.getElementById("comece");
    var loginUrl = redirectButton.getAttribute("data-login-url");

    redirectButton.addEventListener("click", function() {
        // Use a URL da view obtida do atributo de dados
        window.location.href = loginUrl;
    });
});

document.addEventListener("DOMContentLoaded", function(){

    var button_aplique = document.getElementById("button_service1");

        button_aplique.addEventListener("click", function(){
            window.location.href = "#about_us";
        });
});

document.addEventListener("DOMContentLoaded", function(){

    var button_aplique = document.getElementById("button_service2");

        button_aplique.addEventListener("click", function(){
            window.location.href = "#about_us";
        });
});

document.addEventListener("DOMContentLoaded", function(){

    var button_aplique = document.getElementById("button_service3");

        button_aplique.addEventListener("click", function(){
            window.location.href = "#about_us";
        });
});

document.addEventListener("DOMContentLoaded", function(){

    var button_contact = document.getElementById("contato");

        button_contact.addEventListener("click", function(){
            window.location.href = "#div_contact";
        });
});

document.addEventListener("DOMContentLoaded", function(){

    var button_more = document.getElementById("more_description");

        button_more.addEventListener("click", function(){
            window.location.href = "#text_work";
        });
});