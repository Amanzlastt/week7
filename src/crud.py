from sqlalchemy.orm import Session
from . import models, schemas

def create_detection(db: Session, detection: schemas.DetectionResultSchema):
    db_detection = models.DetectionResult(
        image_name=detection.image_name,
        class_label=detection.class_label,
        confidence=detection.confidence,
        timestamp=detection.timestamp
    )
    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)
    return db_detection

def get_detections(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.DetectionResult).offset(skip).limit(limit).all()
