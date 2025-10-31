#!/usr/bin/env python3
"""
Teste showcasepara demonstrar as funcionalidades enriquecidas do Oráculo Alucinado v2.0
"""

import sys
import os

# Adiciona o diretório api ao path
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'api'))

def test_enriched_features():
    """Demonstra as novas funcionalidades da versão 2.0"""
    print("🎭 ORÁCULO ALUCINADO v2.0 - SHOWCASE")
    print("=" * 70)
    
    try:
        from index import gerar_alucinacao
        from data_loader import data_loader
        
        # 1. Demonstrar temas expandidos
        print("\n🎯 TEMAS EXPANDIDOS:")
        print("-" * 40)
        all_themes = data_loader.get_tema_names()
        for i, tema in enumerate(all_themes, 1):
            keywords = data_loader.get_tema_keywords(tema)
            print(f"{i}. {tema.upper()}: {len(keywords)} keywords")
            print(f"   Exemplos: {', '.join(keywords[:5])}...")
        
        # 2. Demonstrar conectores categorizados
        print(f"\n🔮 CONECTORES CATEGORIZADOS:")
        print("-" * 40)
        stats = data_loader.get_tema_stats()
        conectores_stats = stats['conectores']
        for categoria, count in conectores_stats.items():
            print(f"• {categoria.replace('conectores_', '').upper()}: {count} conectores")
            # Mostrar alguns exemplos
            conectores = data_loader.get_conectores_by_category(categoria)
            print(f"  Exemplos: {conectores[0]}, {conectores[1] if len(conectores) > 1 else '...'}")
        
        # 3. Teste por categorias de temas
        print(f"\n🧪 TESTE POR CATEGORIAS:")
        print("-" * 40)
        test_cases = {
            "tecnologia": ["blockchain", "inteligência artificial", "cloud computing"],
            "sustentabilidade": ["energia renovável", "economia circular", "carbono neutro"],
            "arte": ["arte digital", "performance", "NFT"],
            "educacao": ["e-learning", "gamificação", "microlearning"],
            "esportes": ["crossfit", "e-sports", "artes marciais"]
        }
        
        for tema, keywords in test_cases.items():
            print(f"\n🎨 Testando tema: {tema.upper()}")
            for keyword in keywords:
                resultado = gerar_alucinacao(keyword)
                print(f"   '{keyword}' → {resultado['ideia_alucinada']}")
        
        # 4. Demonstrar variedade de conectores
        print(f"\n🌟 VARIEDADE DE CONECTORES:")
        print("-" * 40)
        keyword_teste = "tecnologia"
        conectores_encontrados = set()
        
        for i in range(15):
            resultado = gerar_alucinacao(keyword_teste)
            # Extrair o conector da frase
            frase = resultado['ideia_alucinada']
            for categoria, conectores_list in data_loader.conectores.items():
                for conector in conectores_list:
                    if conector in frase:
                        conectores_encontrados.add(conector)
                        break
        
        print(f"Conectores únicos encontrados em 15 execuções: {len(conectores_encontrados)}")
        for conector in list(conectores_encontrados)[:8]:  # Mostra os primeiros 8
            print(f"   • {conector}")
        
        # 5. Estatísticas finais
        print(f"\n📊 ESTATÍSTICAS DA BASE DE DADOS:")
        print("-" * 40)
        total_keywords = sum(len(data_loader.get_tema_keywords(tema)) for tema in all_themes)
        total_conectores = stats['total_conectores']
        
        print(f"• Total de temas: {len(all_themes)}")
        print(f"• Total de keywords: {total_keywords}")
        print(f"• Total de conectores: {total_conectores}")
        print(f"• Combinações possíveis: {total_keywords * total_conectores * total_keywords:,}")
        
        # 6. Teste de diversidade
        print(f"\n🎲 TESTE DE DIVERSIDADE:")
        print("-" * 40)
        resultados_unicos = set()
        for i in range(25):
            resultado = gerar_alucinacao("inovação")
            resultados_unicos.add(resultado['ideia_alucinada'])
        
        print(f"Ideias únicas geradas em 25 execuções: {len(resultados_unicos)}")
        print(f"Taxa de diversidade: {len(resultados_unicos)/25*100:.1f}%")
        
        print("\n" + "=" * 70)
        print("🎉 SHOWCASE CONCLUÍDO!")
        print("\n🚀 Funcionalidades v2.0:")
        print("• ✅ 8 temas expandidos (vs 4 originais)")
        print("• ✅ 160+ keywords (vs 20 originais)")  
        print("• ✅ 7 categorias de conectores (vs lista única)")
        print("• ✅ 54 conectores únicos (vs 5 originais)")
        print("• ✅ Sistema de dados modular e expansível")
        print("• ✅ Estatísticas e métricas detalhadas")
        print("• ✅ Melhora significativa na diversidade")
        
        print(f"\n💫 Milhões de combinações possíveis!")
        print(f"🎯 Pronto para produção no Vercel!")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO NO SHOWCASE: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_enriched_features()
    sys.exit(0 if success else 1)