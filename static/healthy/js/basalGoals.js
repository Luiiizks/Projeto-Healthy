function calcularTMB() {
    // Obter os valores dos inputs
    var genero = document.getElementById("genero").value;
    var idade = parseInt(document.getElementById("idade").value);
    var peso = parseFloat(document.getElementById("peso").value);
    var altura = parseInt(document.getElementById("altura").value);

    // Fazer o cálculo da TMB (exemplo usando a fórmula de Harris-Benedict para homens e mulheres)
    var tmb;

    if (genero === "homem") {
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade);
    } else if (genero === "mulher") {
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade);
    }

    // Exibir a TMB calculada
    document.getElementById("exibicaoTMB").textContent = tmb.toFixed(2);

    // Exibir a mensagem TMB
    document.getElementById("mensagemTMB").style.display = "block";
}
