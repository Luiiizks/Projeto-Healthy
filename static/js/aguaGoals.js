var metaAguaLitros = 0;
var quantidadeBebidaML = 0;

function definirAgua() {
    // Obtém o valor do input com id "metaAgua" e converte para litros
    metaAguaLitros = parseFloat(document.getElementById("metaAgua").value);
    atualizarExibicaoMeta();
    atualizarProgresso(); // Atualiza o progresso ao definir a meta
}

function atualizarExibicaoMeta() {
    // Exibe o valor da meta em litros no elemento com id "exibicaoMeta"
    document.getElementById("exibicaoMeta").textContent = metaAguaLitros + " L";
}

function adicionarQuantidadeBebida() {
    // Obtém o valor do input com id "quantidadeBebida" em mililitros
    var quantidadeBebidaAdicionada = parseFloat(document.getElementById("quantidadeBebida").value);
    
    // Adiciona a quantidade bebida ao progresso em mililitros
    quantidadeBebidaML += quantidadeBebidaAdicionada;

    // Exibe o progresso no formato (0ml/2000ml)
    document.getElementById("exibicaoProgresso").textContent = "(" + quantidadeBebidaML + "ml/" + (metaAguaLitros * 1000) + "ml)";
}
