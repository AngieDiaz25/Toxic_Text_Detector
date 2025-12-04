from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List
from app.schemas import TextInput, PredictionOutput
from app.inference import detector
from app.database import engine, get_db, Base
from app.models import Prediction

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

@app.get("/", response_class=HTMLResponse)
async def root():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Toxic Text Detector API</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background-color: #f5f5f5;
            }
            .container {
                background-color: white;
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            }
            h1 { color: #2c3e50; }
            .endpoint {
                background-color: #ecf0f1;
                padding: 15px;
                margin: 15px 0;
                border-radius: 5px;
                border-left: 4px solid #3498db;
            }
            .method {
                color: white;
                padding: 5px 10px;
                border-radius: 3px;
                font-weight: bold;
                display: inline-block;
            }
            .get { background-color: #27ae60; }
            .post { background-color: #e67e22; }
            code {
                background-color: #34495e;
                color: #ecf0f1;
                padding: 2px 6px;
                border-radius: 3px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Toxic Text Detector API</h1>
            <p>API REST para detectar toxicidad en textos</p>
            
            <h2>Endpoints Disponibles</h2>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/</code>
                <p>Muestra esta pagina</p>
            </div>
            
            <div class="endpoint">
                <span class="method post">POST</span>
                <code>/predict</code>
                <p>Analiza un texto y guarda en BD</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/history</code>
                <p>Muestra historial de predicciones</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/health</code>
                <p>Estado del servicio</p>
            </div>
            
            <div class="endpoint">
                <span class="method get">GET</span>
                <code>/docs</code>
                <p>Documentacion Swagger</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html_content

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
