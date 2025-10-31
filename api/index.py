import random
import json
import os
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from data_loader import data_loader

# Use data loader for themes and connectors
def get_temas():
    """Get all themes and their keywords"""
    return data_loader.get_all_keywords()

def get_tema_names():
    """Get list of theme names"""
    return data_loader.get_tema_names()

def get_random_conector():
    """Get a random connector"""
    return data_loader.get_random_conector()

def load_static_file(filename):
    """Load static files (HTML, CSS, JS) from the api directory"""
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return None

def get_content_type(filename):
    """Get the appropriate content type for static files"""
    if filename.endswith('.html'):
        return 'text/html; charset=utf-8'
    elif filename.endswith('.css'):
        return 'text/css; charset=utf-8'
    elif filename.endswith('.js'):
        return 'application/javascript; charset=utf-8'
    else:
        return 'text/plain; charset=utf-8'

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

def gerar_alucinacao(keyword: str) -> dict:

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Serve HTML interface for root path
        if path == "/" or path == "/api" or path == "/index.html":
            html_content = load_static_file('index.html')
            if html_content:
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(html_content.encode('utf-8'))
            else:
                self.send_response(404)
                self.send_header('Content-type', 'text/plain')
                self.end_headers()
                self.wfile.write(b'HTML file not found')
                
        # Serve static files (CSS, JS)
        elif path == "/api/styles.css":
            css_content = load_static_file('styles.css')
            if css_content:
                self.send_response(200)
                self.send_header('Content-type', 'text/css; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(css_content.encode('utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
                
        elif path == "/api/script.js":
            js_content = load_static_file('script.js')
            if js_content:
                self.send_response(200)
                self.send_header('Content-type', 'application/javascript; charset=utf-8')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(js_content.encode('utf-8'))
            else:
                self.send_response(404)
                self.end_headers()
                
        elif path == "/api/info":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "message": "🤖 Bem-vindo ao Oráculo Alucinado!",
                "description": "API que gera ideias alucinadas usando heurísticas",
                "version": "2.0 - Enriched Data",
                "endpoints": {
                    "GET /": "Interface web interativa",
                    "POST /api/gerar-ideia": "Gera uma ideia alucinada baseada em keyword",
                    "GET /api/temas": "Lista todos os temas disponíveis com estatísticas",
                    "GET /api/stats": "Estatísticas detalhadas do banco de dados",
                    "GET /api/exemplo": "Mostra um exemplo de uso",
                    "GET /api/info": "Informações da API (JSON)"
                },
                "exemplo_uso": "POST /api/gerar-ideia com body: {\"keyword\": \"viagem rápida\"}",
                "features": [
                    "🎯 8 temas expandidos com 20+ keywords cada",
                    "🔮 7 categorias de conectores alucinados",
                    "🧠 Algoritmo heurístico aprimorado",
                    "📊 Estatísticas e métricas detalhadas"
                ],
                "status": "✅ Funcionando!"
            }
            
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        elif path == "/api/temas":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            response = {
                "temas_disponiveis": data_loader.get_tema_names(),
                "total_temas": len(data_loader.get_tema_names()),
                "estatisticas": data_loader.get_tema_stats()
            }
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        elif path == "/api/stats":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            stats = data_loader.get_tema_stats()
            response = {
                "database_stats": stats,
                "version": "2.0 - Enriched Data",
                "data_source": "JSON files with expanded themes and connectors"
            }
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        elif path == "/api/exemplo":
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            
            exemplo_resultado = gerar_alucinacao("viagem rápida")
            response = {
                "exemplo_input": "viagem rápida",
                "exemplo_output": exemplo_resultado
            }
            self.wfile.write(json.dumps(response, ensure_ascii=False).encode('utf-8'))
            
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode('utf-8'))

    def do_POST(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        if path == "/api/gerar-ideia":
            try:
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length).decode('utf-8')
                data = json.loads(post_data)
                
                keyword = data.get('keyword', '').strip()
                
                if not keyword:
                    self.send_response(400)
                    self.send_header('Content-type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    
                    error_response = {"error": "Keyword não pode estar vazia"}
                    self.wfile.write(json.dumps(error_response).encode('utf-8'))
                    return
                
                resultado = gerar_alucinacao(keyword)
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                self.wfile.write(json.dumps(resultado, ensure_ascii=False).encode('utf-8'))
                
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                error_response = {"error": "JSON inválido"}
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                
                error_response = {"error": f"Erro interno: {str(e)}"}
                self.wfile.write(json.dumps(error_response).encode('utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"error": "Endpoint não encontrado"}).encode('utf-8'))

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()