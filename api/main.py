#!/usr/bin/env python3
"""
Oráculo Alucinado - Main entry point for local development
This file allows running the application locally with uvicorn or similar ASGI servers
"""

import random
from data_loader import data_loader

def gerar_alucinacao(keyword: str) -> dict:
    """
    Função heurística principal que aplica regras de decisão e transformação
    para gerar uma 'alucinação' criativa baseada na keyword de entrada
    """
    keyword_lower = keyword.lower()
    
    # Heurística 1: Identificar o tema mais próximo (Regra de Decisão)
    tema_encontrado = data_loader.find_tema_by_keyword(keyword)
    
    # Se não encontrar tema, assume um tema aleatório (Regra de Fallback)
    if tema_encontrado is None:
        tema_encontrado = random.choice(data_loader.get_tema_names())
        
    # Heurística 2: Distorção Criativa (Regras de Transformação)
    
    # 2a. Seleciona o elemento base do tema
    elemento_base = random.choice(data_loader.get_tema_keywords(tema_encontrado))
    
    # 2b. Seleciona um elemento de um TEMA ALEATÓRIO (a Alucinação Principal)
    temas_restantes = [t for t in data_loader.get_tema_names() if t != tema_encontrado]
    tema_alucinado = random.choice(temas_restantes)
    elemento_alucinado = random.choice(data_loader.get_tema_keywords(tema_alucinado))
    
    # 2c. Conector Aleatório
    conector = data_loader.get_random_conector()
    
    # Heurística 3: Estruturar a Resposta (Formato Final)
    frase_final = f"Criar uma plataforma de {elemento_base} {conector} {elemento_alucinado}."
    
    return {
        "input_solicitado": keyword,
        "tema_identificado": tema_encontrado.capitalize(),
        "ideia_alucinada": frase_final,
        "fator_distorcao": f"Combinação de {elemento_base} com o tema {tema_alucinado.capitalize()}"
    }

def main():
    """Função principal para execução local e testes"""
    print("🤖 Oráculo Alucinado - Versão 2.0")
    print("=" * 50)
    
    # Exibir estatísticas
    stats = data_loader.get_tema_stats()
    print(f"📊 Temas disponíveis: {stats['total_temas']}")
    print(f"📊 Total de conectores: {stats['total_conectores']}")
    
    # Modo interativo
    print("\n🎮 Modo interativo (digite 'sair' para finalizar):")
    while True:
        try:
            keyword = input("\n🔤 Digite uma keyword: ").strip()
            if keyword.lower() in ['sair', 'exit', 'quit', '']:
                break
                
            resultado = gerar_alucinacao(keyword)
            print(f"\n🎯 Resultado para '{keyword}':")
            print(f"📝 Tema: {resultado['tema_identificado']}")
            print(f"💡 Ideia: {resultado['ideia_alucinada']}")
            print(f"🔀 Distorção: {resultado['fator_distorcao']}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    print("\n👋 Obrigado por usar o Oráculo Alucinado!")

if __name__ == "__main__":
    main()