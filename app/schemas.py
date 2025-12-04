from pydantic import BaseModel, Field
from typing import Dict

class TextInput(BaseModel):
    """Schema para entrada de texto"""
    text: str = Field(..., min_length=1, max_length=5000, 
                     description="Texto a analizar")
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "This is a sample text to analyze"
            }
        }

class PredictionOutput(BaseModel):
    """Schema para salida de prediccion"""
    text: str
    is_toxic: bool
    main_category: str
    confidence: float
    labels: Dict[str, float]
    
    class Config:
        json_schema_extra = {
            "example": {
                "text": "You are stupid",
                "is_toxic": True,
                "main_category": "insult",
                "confidence": 0.89,
                "labels": {
                    "toxic": 0.85,
                    "insult": 0.89,
                    "obscene": 0.12,
                    "threat": 0.01,
                    "severe_toxic": 0.01,
                    "identity_hate": 0.01
                }
            }
        }
