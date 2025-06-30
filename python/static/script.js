// Validar e-mail (exemplo simples)
document.querySelector("form").addEventListener("submit", function(e) {
    const email = document.querySelector("input[name='email']").value;
    if (!email.includes("@")) {
        alert("Por favor, insira um e-mail válido.");
        e.preventDefault();
    }
});
