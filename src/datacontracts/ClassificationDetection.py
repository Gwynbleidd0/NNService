import pathlib
import uuid
from pydantic import BaseModel, ByteSize


class ClassificationDetection(BaseModel):
    id: uuid.UUID
    class_title: str
    confidence: float
