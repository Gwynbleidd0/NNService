import typing
import pathlib
import uuid
from pydantic import BaseModel, ByteSize
from datacontracts.DetectionBBox import DetectionBBox
from datacontracts.DetectionPolygon import DetectionPolygon

from datacontracts.DetectionTypes import DetectionTypes


class OutputFrame(BaseModel):
    id: uuid.UUID
    input_frame_id: uuid.UUID
    detection_types: DetectionTypes
    detections: typing.List[typing.Union[DetectionBBox, DetectionPolygon]]
    output_img_path: pathlib.Path = None
