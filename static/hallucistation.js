// Hallucistation Frontend - JavaScript Implementation
// ================================================

// Data from JSON files (embedded for frontend-only version)
const temas = {
    "tecnologia": ["microchip", "blockchain", "metaverso", "computação quântica", "big data", "inteligência artificial", "IoT", "realidade virtual", "robótica", "cloud computing", "cibersegurança", "machine learning"],
    "saúde": ["nutrição", "sono", "imunidade", "exercício", "microbioma", "meditação", "terapia genética", "medicina personalizada", "biotecnologia", "longevidade"],
    "viagem": ["espaço", "oceano", "montanha", "deserto", "floresta tropical", "turismo sustentável", "ecoturismo", "aventura extrema", "intercâmbio cultural"],
    "comida": ["vegetariana", "fermentada", "molecular", "sustentável", "sabor umami", "culinária étnica", "ingredientes exóticos", "fermentação", "superalimentos"],
    "educacao": ["e-learning", "gamificação", "realidade aumentada na educação", "ensino adaptativo", "microlearning", "educação personalizada"],
    "sustentabilidade": ["energia renovável", "economia circular", "agricultura vertical", "biomateriais", "tecnologia limpa", "carbono neutro"],
    "arte": ["arte digital", "NFT", "instalações interativas", "arte generativa", "realidade virtual artística", "performance digital"],
    "fitness": ["crossfit", "yoga", "HIIT", "pilates", "treino funcional", "corrida", "natação", "artes marciais", "dança fitness"]
};

const conectores_alucinados = [
    "alimentado por cristais de",
    "usando a energia cinética de",
    "escondido no espectro de",
    "com a única finalidade de treinar",
    "que na verdade é um disfarce para",
    "baseado na frequência vibracional de",
    "inspirado nos padrões neurais de"
];

// Utility functions
function getRandomElement(array) {
    return array[Math.floor(Math.random() * array.length)];
}

function findTemaByKeyword(keyword) {
    const keywordLower = keyword.toLowerCase();
    
    for (const [tema, palavras] of Object.entries(temas)) {
        if (tema.includes(keywordLower) || 
            palavras.some(palavra => keywordLower.includes(palavra) || palavra.includes(keywordLower))) {
            return tema;
        }
    }
    
    return null;
}

// Main hallucination generation function
function gerarAlucinacao(keyword) {
    const keywordLower = keyword.toLowerCase();
    
    // Heurística 1: Identificar o tema mais próximo (Regra de Decisão)
    let temaEncontrado = findTemaByKeyword(keyword);
    
    // Se não encontrar tema, assume um tema aleatório (Regra de Fallback)
    if (temaEncontrado === null) {
        temaEncontrado = getRandomElement(Object.keys(temas));
    }
    
    // Heurística 2: Distorção Criativa (Regras de Transformação)
    
    // 2a. Seleciona o elemento base do tema
    const elementoBase = getRandomElement(temas[temaEncontrado]);
    
    // 2b. Seleciona um elemento de um TEMA ALEATÓRIO (a Alucinação Principal)
    const temasRestantes = Object.keys(temas).filter(t => t !== temaEncontrado);
    const temaAlucinado = getRandomElement(temasRestantes);
    const elementoAlucinado = getRandomElement(temas[temaAlucinado]);
    
    // 2c. Aplica um Conector Criativo (a Ponte da Alucinação)
    const conector = getRandomElement(conectores_alucinados);
    
    // Heurística 3: Montagem Final (Regra de Síntese)
    const ideiaAlucinada = `${elementoBase} ${conector} ${elementoAlucinado}`;
    const fatorDistorcao = `Combinou ${temaEncontrado} com ${temaAlucinado} usando "${conector}"`;
    
    return {
        input_solicitado: keyword,
        tema_identificado: temaEncontrado,
        ideia_alucinada: ideiaAlucinada,
        fator_distorcao: fatorDistorcao
    };
}

// Frontend interaction functions
function preencherKeyword(keyword) {
    document.getElementById('keyword').value = keyword;
}

function gerarIdeia() {
    const keyword = document.getElementById('keyword').value.trim();
    const resultadoDiv = document.getElementById('resultado');
    const btn = document.getElementById('gerarBtn');
    
    if (!keyword) {
        alert('Por favor, digite uma palavra-chave!');
        return;
    }
    
    // Mostrar loading
    btn.disabled = true;
    btn.textContent = '🔄 Gerando...';
    resultadoDiv.style.display = 'block';
    resultadoDiv.innerHTML = '<div class="loading">🤖 O Oráculo está pensando...</div>';
    
    // Simulate some processing time for better UX
    setTimeout(() => {
        try {
            const data = gerarAlucinacao(keyword);
            
            resultadoDiv.innerHTML = `
                <div class="result">
                    <h3>🎯 Resultado para "${data.input_solicitado}"</h3>
                    <p><strong>Tema identificado:</strong> ${data.tema_identificado}</p>
                    <p><strong>💡 Ideia gerada:</strong></p>
                    <p style="font-size: 1.1em; font-weight: bold; color: #feca57;">${data.ideia_alucinada}</p>
                    <p><strong>🔀 Fator de distorção:</strong> ${data.fator_distorcao}</p>
                </div>
            `;
        } catch (error) {
            resultadoDiv.innerHTML = `
                <div class="result error">
                    <h3>❌ Erro</h3>
                    <p>Ocorreu um erro ao gerar a ideia: ${error.message}</p>
                </div>
            `;
        } finally {
            // Restaurar botão
            btn.disabled = false;
            btn.textContent = '🔮 Gerar Ideia Alucinada';
        }
    }, 800); // 800ms delay for better UX
}

// Allow Enter key to trigger idea generation
document.addEventListener('DOMContentLoaded', function() {
    const keywordInput = document.getElementById('keyword');
    keywordInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            gerarIdeia();
        }
    });
    
    // Focus on input when page loads
    keywordInput.focus();
});

// Export functions for potential future use
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        gerarAlucinacao,
        temas,
        conectores_alucinados
    };
}