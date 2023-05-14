import typing
import pathlib
import uuid
from pydantic import BaseModel, ByteSize


class InputFrame(BaseModel):
    id: uuid.UUID
    path_to_frame: pathlib.Path
