import typing
import pathlib
import uuid
from pydantic import BaseModel, ByteSize
from datacontracts.InputFrame import InputFrame
from datacontracts.OutputFrame import OutputFrame

from datacontracts.Point import Point


class NNKernelConfiguration(BaseModel):
    title: str
    type: str
    ip: str
    port: int
