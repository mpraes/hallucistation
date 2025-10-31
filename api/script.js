function preencherKeyword(keyword) {
    document.getElementById('keyword').value = keyword;
}

async function gerarIdeia() {
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
    
    try {
        const response = await fetch('/api/gerar-ideia', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ keyword: keyword })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            resultadoDiv.innerHTML = `
                <div class="result">
                    <h3>🎯 Resultado para "${data.input_solicitado}"</h3>
                    <p><strong>Tema identificado:</strong> ${data.tema_identificado}</p>
                    <p><strong>💡 Ideia gerada:</strong></p>
                    <p style="font-size: 1.1em; font-weight: bold; color: #feca57;">${data.ideia_alucinada}</p>
                    <p><strong>🔀 Fator de distorção:</strong> ${data.fator_distorcao}</p>
                </div>
            `;
        } else {
            resultadoDiv.innerHTML = `
                <div class="result error">
                    <h3>❌ Erro</h3>
                    <p>${data.error || 'Erro desconhecido'}</p>
                </div>
            `;
        }
    } catch (error) {
        resultadoDiv.innerHTML = `
            <div class="result error">
                <h3>❌ Erro de conexão</h3>
                <p>Não foi possível conectar com a API: ${error.message}</p>
            </div>
        `;
    } finally {
        btn.disabled = false;
        btn.textContent = '🔮 Gerar Ideia Alucinada';
    }
}

async function carregarTemas() {
    try {
        const response = await fetch('/api/temas');
        const data = await response.json();
        
        if (response.ok && data.temas_disponiveis) {
            const temasContainer = document.getElementById('temas-info');
            if (temasContainer) {
                temasContainer.innerHTML = `
                    <p><strong>Temas disponíveis:</strong> ${data.temas_disponiveis.join(', ')}</p>
                    <p><strong>Total:</strong> ${data.total_temas} temas</p>
                `;
            }
        }
    } catch (error) {
        console.error('Erro ao carregar temas:', error);
    }
}

// Inicialização quando a página carrega
document.addEventListener('DOMContentLoaded', function() {
    // Enter para gerar ideia
    const keywordInput = document.getElementById('keyword');
    if (keywordInput) {
        keywordInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                gerarIdeia();
            }
        });
    }
    
    // Carregar informações dos temas
    carregarTemas();
});

// Função para mostrar/ocultar informações extras
function toggleInfo() {
    const infoDiv = document.getElementById('extra-info');
    if (infoDiv) {
        infoDiv.style.display = infoDiv.style.display === 'none' ? 'block' : 'none';
    }
}