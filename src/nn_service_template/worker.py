import time
import typing
import uuid

from datacontracts.OutputFrame import OutputFrame


class Worker:
    def __init__(self) -> None:
        pass

    def run(self, *args, **kwargs) -> OutputFrame:
        pass

    def run_pack(self, *args, **kwargs) -> typing.List[OutputFrame]:
        pass
