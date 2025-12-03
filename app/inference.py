from transformers import pipeline
import torch
from typing import Dict

class ToxicityDetector:
    """Detector de toxicidad usando el modelo toxic-bert"""
    
    def __init__(self):
        """Inicializa el modelo"""
        print("Cargando modelo toxic-bert...")
        self.classifier = pipeline(
            "text-classification",
            model="unitary/toxic-bert",
            top_k=None,
            device=0 if torch.cuda.is_available() else -1
        )
        print("Modelo cargado correctamente")
    
    def predict(self, text: str) -> Dict:
        """
        Analiza un texto y devuelve prediccion de toxicidad
        
        Args:
            text: Texto a analizar
            
        Returns:
            Dict con resultados de la prediccion
        """
        if not text or len(text.strip()) == 0:
            raise ValueError("El texto no puede estar vacio")
        
        # Obtener predicciones del modelo
        results = self.classifier(text)[0]
        
        # Organizar resultados
        predictions = {
            "text": text,
            "labels": {},
            "is_toxic": False,
            "main_category": "non-toxic",
            "confidence": 0.0
        }
        
        # Umbral para considerar algo como toxico
        toxic_threshold = 0.5
        max_score = 0.0
        
        # Procesar cada categoria
        for result in results:
            label = result['label']
            score = result['score']
            predictions["labels"][label] = round(score, 4)
            
            # Encontrar la categoria con mayor score
            if score > max_score:
                max_score = score
                predictions["main_category"] = label
                predictions["confidence"] = round(score, 4)
        
        # Determinar si es toxico
        predictions["is_toxic"] = max_score >= toxic_threshold
        
        return predictions


# Instancia global del detector
detector = ToxicityDetector()
