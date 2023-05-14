import typing
import pathlib
import uuid
from pydantic import BaseModel, ByteSize
from datacontracts.InputFrame import InputFrame
from datacontracts.OutputFrame import OutputFrame

from datacontracts.Point import Point


class NNTask(BaseModel):
    id: uuid.UUID
    input_frame_list: typing.List[InputFrame]
    output_frame_list: typing.List[OutputFrame]
