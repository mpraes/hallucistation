import random
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Oráculo Alucinado", description="API que gera ideias alucinadas baseadas em heurísticas")

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

class KeywordRequest(BaseModel):
    keyword: str

class IdeiaResponse(BaseModel):
    input_solicitado: str
    tema_identificado: str
    ideia_alucinada: str
    fator_distorcao: str

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

@app.get("/")
async def root():
    """Endpoint raiz com informações sobre a API"""
    return {
        "message": "Bem-vindo ao Oráculo Alucinado!",
        "description": "Envie uma keyword para /gerar-ideia e receba uma ideia alucinada",
        "exemplo": "POST /gerar-ideia com {'keyword': 'viagem rápida'}"
    }

@app.post("/gerar-ideia", response_model=IdeiaResponse)
async def gerar_ideia(request: KeywordRequest):
    """
    Endpoint principal que recebe uma keyword e retorna uma ideia alucinada
    """
    if not request.keyword.strip():
        raise HTTPException(status_code=400, detail="Keyword não pode estar vazia")
    
    try:
        resultado = gerar_alucinacao(request.keyword)
        return IdeiaResponse(**resultado)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/temas")
async def listar_temas():
    """Endpoint para listar todos os temas disponíveis"""
    return {"temas_disponiveis": list(temas.keys())}

@app.get("/exemplo")
async def exemplo_uso():
    """Endpoint que demonstra um exemplo de uso"""
    exemplo_resultado = gerar_alucinacao("viagem rápida")
    return {
        "exemplo_input": "viagem rápida",
        "exemplo_output": exemplo_resultado
    }

# Para desenvolvimento local
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)