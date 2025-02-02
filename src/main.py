from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.database import engine, Base, get_db
from src import models, schemas, crud

app = FastAPI()


# Create tables
Base.metadata.create_all(bind=engine)

@app.post("/detections/", response_model=schemas.DetectionResultSchema)
def create_detection(detection: schemas.DetectionResultSchema, db: Session = Depends(get_db)):
    return crud.create_detection(db=db, detection=detection)

@app.get("/detections/", response_model=list[schemas.DetectionResultSchema])
def read_detections(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_detections(db, skip=skip, limit=limit)
