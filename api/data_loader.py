"""
Data loader module for Oráculo Alucinado
Handles loading and processing of themes and connectors data
"""

import json
import random
from typing import Dict, List, Any
import os

class DataLoader:
    """Handles loading and accessing themes and connectors data"""
    
    def __init__(self, data_dir: str = None):
        if data_dir is None:
            # Get the data directory relative to this file
            current_dir = os.path.dirname(os.path.abspath(__file__))
            self.data_dir = os.path.join(os.path.dirname(current_dir), 'data')
        else:
            self.data_dir = data_dir
            
        self.temas = {}
        self.conectores = {}
        self._load_data()
    
    def _load_data(self):
        """Load themes and connectors from JSON files"""
        try:
            # Load themes
            temas_path = os.path.join(self.data_dir, 'temas.json')
            with open(temas_path, 'r', encoding='utf-8') as f:
                self.temas = json.load(f)
            
            # Load connectors
            conectores_path = os.path.join(self.data_dir, 'conectores.json')
            with open(conectores_path, 'r', encoding='utf-8') as f:
                self.conectores = json.load(f)
                
        except FileNotFoundError as e:
            # Fallback to hardcoded data if files not found
            print(f"Warning: Could not load data files ({e}), using fallback data")
            self._load_fallback_data()
        except json.JSONDecodeError as e:
            print(f"Warning: Invalid JSON in data files ({e}), using fallback data")
            self._load_fallback_data()
    
    def _load_fallback_data(self):
        """Fallback data in case files can't be loaded"""
        self.temas = {
            "tecnologia": {
                "keywords": ["microchip", "blockchain", "metaverso", "computação quântica", "big data"],
                "description": "Temas relacionados à tecnologia",
                "weight": 1.0
            },
            "saúde": {
                "keywords": ["nutrição", "sono", "imunidade", "exercício", "microbioma"],
                "description": "Temas relacionados à saúde",
                "weight": 1.0
            },
            "viagem": {
                "keywords": ["espaço", "oceano", "montanha", "deserto", "floresta tropical"],
                "description": "Temas relacionados a viagens",
                "weight": 1.0
            },
            "comida": {
                "keywords": ["vegetariana", "fermentada", "molecular", "sustentável", "sabor umami"],
                "description": "Temas relacionados à alimentação",
                "weight": 1.0
            }
        }
        
        self.conectores = {
            "conectores_energia": [
                "alimentado por cristais de",
                "usando a energia cinética de",
                "escondido no espectro de",
                "com a única finalidade de treinar",
                "que na verdade é um disfarce para"
            ]
        }
    
    def get_tema_names(self) -> List[str]:
        """Get list of all theme names"""
        return list(self.temas.keys())
    
    def get_tema_keywords(self, tema: str) -> List[str]:
        """Get keywords for a specific theme"""
        return self.temas.get(tema, {}).get('keywords', [])
    
    def get_all_keywords(self) -> Dict[str, List[str]]:
        """Get all keywords organized by theme"""
        return {tema: data['keywords'] for tema, data in self.temas.items()}
    
    def get_random_conector(self) -> str:
        """Get a random connector from all categories"""
        all_conectores = []
        for categoria, conectores_list in self.conectores.items():
            all_conectores.extend(conectores_list)
        return random.choice(all_conectores)
    
    def get_conectores_by_category(self, categoria: str) -> List[str]:
        """Get connectors from a specific category"""
        return self.conectores.get(categoria, [])
    
    def get_random_conector_from_category(self, categoria: str) -> str:
        """Get a random connector from a specific category"""
        conectores_list = self.get_conectores_by_category(categoria)
        return random.choice(conectores_list) if conectores_list else self.get_random_conector()
    
    def find_tema_by_keyword(self, keyword: str) -> str:
        """Find the theme that matches the given keyword"""
        keyword_lower = keyword.lower()
        
        # Direct theme name match
        for tema in self.temas.keys():
            if tema in keyword_lower:
                return tema
        
        # Keyword match within themes
        for tema, data in self.temas.items():
            keywords = data.get('keywords', [])
            if any(kw.lower() in keyword_lower for kw in keywords):
                return tema
        
        # No match found
        return None
    
    def get_tema_stats(self) -> Dict[str, Any]:
        """Get statistics about themes and connectors"""
        tema_stats = {}
        for tema, data in self.temas.items():
            tema_stats[tema] = {
                'keyword_count': len(data.get('keywords', [])),
                'description': data.get('description', ''),
                'weight': data.get('weight', 1.0)
            }
        
        conector_stats = {}
        total_conectores = 0
        for categoria, conectores_list in self.conectores.items():
            count = len(conectores_list)
            conector_stats[categoria] = count
            total_conectores += count
        
        return {
            'temas': tema_stats,
            'conectores': conector_stats,
            'total_temas': len(self.temas),
            'total_conectores': total_conectores
        }

# Global instance for easy access
data_loader = DataLoader()