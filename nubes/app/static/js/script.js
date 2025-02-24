document.addEventListener('DOMContentLoaded', function() {
    // Função para mostrar/ocultar a senha
    document.getElementById('mostrar-senha').addEventListener('change', function() {
        const senhaInput = document.getElementById('senha');
        if (this.checked) {
            senhaInput.type = 'text'; // Mostra a senha
        } else {
            senhaInput.type = 'password'; // Oculta a senha
        }
    });
});