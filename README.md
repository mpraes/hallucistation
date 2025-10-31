# 🤖 Oráculo Alucinado (HalluciStation)

Uma API que gera ideias criativas e "alucinadas" usando heurísticas em Python. O sistema recebe uma palavra-chave e aplica regras de decisão e transformação para criar ideias factualmente distorcidas de propósito.

## 🚀 Como Funciona

A API usa um conjunto de **heurísticas** para:
1. **Identificar** o tema mais próximo da keyword recebida
2. **Distorcer** criativamente combinando elementos de temas diferentes
3. **Gerar** uma ideia que parece relacionada mas é criativamente alucinada

## 🛠️ Instalação

```bash
# Clone o repositório
git clone <seu-repo>
cd hallucistation

# Instale as dependências
pip install -r requirements.txt

# Execute localmente
python main.py
```

## 📡 Endpoints da API

### `GET /`
Informações básicas sobre a API

### `POST /gerar-ideia`
Endpoint principal que recebe uma keyword e retorna uma ideia alucinada

**Exemplo de Request:**
```json
{
  "keyword": "viagem rápida"
}
```

**Exemplo de Response:**
```json
{
  "input_solicitado": "viagem rápida",
  "tema_identificado": "Viagem",
  "ideia_alucinada": "Criar uma plataforma de oceano alimentado por cristais de microchip.",
  "fator_distorcao": "Combinação de oceano com o tema Tecnologia"
}
```

### `GET /temas`
Lista todos os temas disponíveis no sistema

### `GET /exemplo`
Demonstra um exemplo de uso da API

## 🌍 Deploy na Vercel

Este projeto está configurado para deploy automático na Vercel:

1. Conecte seu repositório GitHub à Vercel
2. A Vercel detecta automaticamente o `vercel.json` e faz o deploy
3. Sua API estará disponível em segundos!

## 🎯 Temas Disponíveis

- **Tecnologia**: microchip, blockchain, metaverso, computação quântica, big data
- **Saúde**: nutrição, sono, imunidade, exercício, microbioma  
- **Viagem**: espaço, oceano, montanha, deserto, floresta tropical
- **Comida**: vegetariana, fermentada, molecular, sustentável, sabor umami

## 🔮 Conectores Alucinados

O sistema usa conectores criativos como:
- "alimentado por cristais de"
- "usando a energia cinética de"
- "escondido no espectro de"
- "com a única finalidade de treinar"
- "que na verdade é um disfarce para"

## 🧠 Algoritmo Heurístico

1. **Regra de Decisão**: Identifica o tema mais próximo da keyword
2. **Regra de Fallback**: Se não encontrar tema, escolhe um aleatório  
3. **Regra de Transformação**: Combina elemento do tema identificado com elemento de tema diferente
4. **Formatação Final**: Estrutura a resposta usando conectores alucinados

## 📈 Performance

- ⚡ **Super rápido**: Puramente computacional (sem LLMs)
- 🗄️ **Sem banco**: Conhecimento armazenado em listas Python
- ☁️ **Serverless**: Otimizado para Vercel Functions