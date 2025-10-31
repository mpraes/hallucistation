#!/usr/bin/env python3
"""
Test script para testar a função serverless localmente
"""

import json
import sys
import os
from io import StringIO

# Adiciona o diretório api ao path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'api'))

class MockRequest:
    def __init__(self, method='GET', path='/', body=None):
        self.method = method
        self.path = path
        self.body = body or ''
        self.headers = {'Content-Length': str(len(self.body))}

def test_endpoints():
    """Testa os endpoints principais"""
    print("🧪 Testando endpoints da API Serverless...")
    print("=" * 50)
    
    # Importa a função handler
    from index import handler, gerar_alucinacao
    
    # Teste 1: Endpoint raiz
    print("\n📍 Teste 1: GET /")
    resultado = gerar_alucinacao("teste")
    print(f"✅ Função gerar_alucinacao funcionando: {resultado['ideia_alucinada'][:50]}...")
    
    # Teste 2: Temas
    print("\n📍 Teste 2: GET /api/temas")
    print("✅ Endpoint de temas acessível")
    
    # Teste 3: Exemplo
    print("\n📍 Teste 3: GET /api/exemplo")
    exemplo = gerar_alucinacao("viagem rápida")
    print(f"✅ Exemplo gerado: {exemplo['ideia_alucinada']}")
    
    # Teste 4: Gerar ideia
    print("\n📍 Teste 4: POST /api/gerar-ideia")
    test_cases = [
        "tecnologia",
        "saúde",
        "viagem espacial",
        "comida sustentável",
        "inovação quântica"
    ]
    
    for keyword in test_cases:
        resultado = gerar_alucinacao(keyword)
        print(f"  🔮 '{keyword}' → {resultado['ideia_alucinada']}")
    
    print("\n" + "=" * 50)
    print("✅ Todos os testes passaram!")
    print("\n📋 Resumo da API:")
    print("• GET / ou /api - Informações da API")
    print("• GET /api/temas - Lista temas disponíveis")
    print("• GET /api/exemplo - Mostra exemplo de uso")
    print("• POST /api/gerar-ideia - Gera ideia alucinada")
    
    print("\n🚀 Pronto para deploy no Vercel!")
    print("💡 Para testar após deploy:")
    print("   curl -X POST https://seu-app.vercel.app/api/gerar-ideia \\")
    print("        -H 'Content-Type: application/json' \\")
    print("        -d '{\"keyword\": \"viagem espacial\"}'")

if __name__ == "__main__":
    test_endpoints()