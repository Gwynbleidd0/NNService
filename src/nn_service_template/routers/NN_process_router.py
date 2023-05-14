import pathlib
import typing
import uuid
import aiofiles
from fastapi import APIRouter, BackgroundTasks
from typing import List, Optional, Union
import os

from datacontracts.InputFrame import InputFrame
from nn_service_template.mics import worker


router_process = APIRouter(prefix="/process", tags=["Process"])


@router_process.post("/process-image")
async def process_file(input_file: InputFrame):
    print(input_file)
    worker.run(input_file)
    return True


@router_process.post("/process-pack")
async def process_file(input_files: typing.List[InputFrame], background_tasks: BackgroundTasks):
    background_tasks.add_task(worker.run_pack, input_files)
    return len(background_tasks.tasks)
