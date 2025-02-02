from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class DetectionResult(Base):
    __tablename__ = "detection_results"

    id = Column(Integer, primary_key=True, index=True)
    image_name = Column(String, index=True)
    class_label = Column(String)
    confidence = Column(Integer)
    timestamp = Column(DateTime)
