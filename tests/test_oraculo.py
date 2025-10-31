#!/usr/bin/env python3
"""
Test script para o Oráculo Alucinado
Executa testes locais das funções principais antes do deploy
"""

import random
import sys
import os

# Adiciona o diretório raiz ao path para importar o módulo
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Conhecimento Básico (A 'Memória' do Oráculo)
temas = {
    "tecnologia": ["microchip", "blockchain", "metaverso", "computação quântica", "big data"],
    "saúde": ["nutrição", "sono", "imunidade", "exercício", "microbioma"],
    "viagem": ["espaço", "oceano", "montanha", "deserto", "floresta tropical"],
    "comida": ["vegetariana", "fermentada", "molecular", "sustentável", "sabor umami"],
}

# Distorções Heurísticas
conectores_alucinados = [
    "alimentado por cristais de",
    "usando a energia cinética de",
    "escondido no espectro de",
    "com a única finalidade de treinar",
    "que na verdade é um disfarce para",
]

def gerar_alucinacao(keyword: str) -> dict:
    """
    Função heurística principal que aplica regras de decisão e transformação
    para gerar uma 'alucinação' criativa baseada na keyword de entrada
    """
    keyword_lower = keyword.lower()
    
    # Heurística 1: Identificar o tema mais próximo (Regra de Decisão)
    tema_encontrado = None
    for tema, palavras in temas.items():
        if any(kw in keyword_lower for kw in palavras) or tema in keyword_lower:
            tema_encontrado = tema
            break
            
    # Se não encontrar tema, assume um tema aleatório (Regra de Fallback)
    if tema_encontrado is None:
        tema_encontrado = random.choice(list(temas.keys()))
        
    # Heurística 2: Distorção Criativa (Regras de Transformação)
    
    # 2a. Seleciona o elemento base do tema
    elemento_base = random.choice(temas[tema_encontrado])
    
    # 2b. Seleciona um elemento de um TEMA ALEATÓRIO (a Alucinação Principal)
    temas_restantes = [t for t in temas if t != tema_encontrado]
    tema_alucinado = random.choice(temas_restantes)
    elemento_alucinado = random.choice(temas[tema_alucinado])
    
    # 2c. Conector Aleatório
    conector = random.choice(conectores_alucinados)
    
    # Heurística 3: Estruturar a Resposta (Formato Final)
    frase_final = f"Criar uma plataforma de {elemento_base} {conector} {elemento_alucinado}."
    
    return {
        "input_solicitado": keyword,
        "tema_identificado": tema_encontrado.capitalize(),
        "ideia_alucinada": frase_final,
        "fator_distorcao": f"Combinação de {elemento_base} com o tema {tema_alucinado.capitalize()}"
    }

def test_oraculo():
    """Executa testes das funcionalidades principais"""
    print("🤖 Testando o Oráculo Alucinado...")
    print("=" * 50)
    
    # Lista de keywords para teste
    test_keywords = [
        "viagem rápida",
        "blockchain",
        "nutrição",
        "espaço",
        "inovação",
        "sustentabilidade",
        "tecnologia quântica"
    ]
    
    for i, keyword in enumerate(test_keywords, 1):
        print(f"\n🔮 Teste {i}: '{keyword}'")
        print("-" * 30)
        
        try:
            resultado = gerar_alucinacao(keyword)
            print(f"📝 Input: {resultado['input_solicitado']}")
            print(f"🎯 Tema: {resultado['tema_identificado']}")
            print(f"💡 Ideia: {resultado['ideia_alucinada']}")
            print(f"🔀 Distorção: {resultado['fator_distorcao']}")
            
        except Exception as e:
            print(f"❌ Erro no teste: {e}")
    
    print("\n" + "=" * 50)
    print("✅ Testes concluídos!")
    
    # Teste interativo
    print("\n🎮 Teste interativo (digite 'sair' para finalizar):")
    while True:
        keyword = input("\n🔤 Digite uma keyword: ").strip()
        if keyword.lower() in ['sair', 'exit', 'quit', '']:
            break
            
        try:
            resultado = gerar_alucinacao(keyword)
            print(f"\n🎯 Resultado para '{keyword}':")
            print(f"💡 {resultado['ideia_alucinada']}")
            print(f"🔀 {resultado['fator_distorcao']}")
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    print("\n👋 Obrigado por testar o Oráculo Alucinado!")

if __name__ == "__main__":
    test_oraculo()