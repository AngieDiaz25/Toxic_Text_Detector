from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base
import json

class Prediction(Base):
    __tablename__ = "predictions"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    text = Column(String, nullable=False)
    is_toxic = Column(Boolean, nullable=False)
    main_category = Column(String)
    confidence = Column(Float)
    labels = Column(String)
    
    def set_labels(self, labels_dict):
        self.labels = json.dumps(labels_dict)
    
    def get_labels(self):
        return json.loads(self.labels) if self.labels else {}
