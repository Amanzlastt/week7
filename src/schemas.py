from pydantic import BaseModel
from datetime import datetime

class DetectionResultSchema(BaseModel):
    id: int
    image_name: str
    class_label: str
    confidence: int
    timestamp: datetime

    class Config:
        orm_mode = True
