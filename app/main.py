from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from typing import List
from app.schemas import TextInput, PredictionOutput
from app.inference import detector
from app.database import engine, get_db, Base
from app.models import Prediction
import os

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Toxic Text Detector API",
    description="API para detectar toxicidad en textos usando IA",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/", response_class=HTMLResponse)
async def root():
    return FileResponse("frontend/index.html")

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "model": "toxic-bert",
        "version": "1.0.0"
    }

@app.post("/predict", response_model=PredictionOutput)
async def predict_toxicity(input_data: TextInput, db: Session = Depends(get_db)):
    try:
        result = detector.predict(input_data.text)
        
        db_prediction = Prediction(
            text=result["text"],
            is_toxic=result["is_toxic"],
            main_category=result["main_category"],
            confidence=result["confidence"]
        )
        db_prediction.set_labels(result["labels"])
        
        db.add(db_prediction)
        db.commit()
        db.refresh(db_prediction)
        
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error interno")

@app.get("/history")
async def get_history(limit: int = 10, db: Session = Depends(get_db)):
    predictions = db.query(Prediction).order_by(Prediction.timestamp.desc()).limit(limit).all()
    
    results = []
    for pred in predictions:
        results.append({
            "id": pred.id,
            "timestamp": pred.timestamp.isoformat(),
            "text": pred.text,
            "is_toxic": pred.is_toxic,
            "main_category": pred.main_category,
            "confidence": pred.confidence,
            "labels": pred.get_labels()
        })
    
    return {
        "total": len(results),
        "predictions": results
    }
