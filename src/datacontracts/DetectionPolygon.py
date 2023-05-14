import typing
import pathlib
import uuid
from pydantic import BaseModel, ByteSize

from datacontracts.Point import Point


class DetectionPolygon(BaseModel):
    id: uuid.UUID
    points: typing.List[Point]
    title: typing.Optional[str] = None
    confidence: float
