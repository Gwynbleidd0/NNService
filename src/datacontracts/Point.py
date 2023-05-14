from pydantic import BaseModel, ByteSize


class Point(BaseModel):
    x: float
    y: float
