import typing
import pathlib
import uuid
from pydantic import BaseModel, ByteSize

from datacontracts.Point import Point


class DetectionBBox(BaseModel):
    id: uuid.UUID
    point1: Point
    point2: Point
    title: typing.Optional[str] = None
    confidence: float
