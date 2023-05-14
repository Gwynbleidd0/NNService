import json
import pathlib
import uuid
import aiofiles
import aiohttp
from fastapi import APIRouter, UploadFile
from typing import List, Optional, Union
import os
from datacontracts.InputFrame import InputFrame
from kernel.mics import config_provider

main_router = APIRouter(prefix="/process", tags=["Process"])


@main_router.post("/run")
async def upload_file(file: UploadFile):
    input_id = uuid.uuid4()
    img_path = os.path.join(config_provider.temp_folder, str(input_id) + file.filename)
    async with aiofiles.open(img_path, "wb") as out_file:
        content = await file.read()
        await out_file.write(content)
    nn_kernel = config_provider.NNKernels[0]
    input_json = InputFrame(id=input_id, path_to_frame=img_path).json()
    print(json.loads(input_json))
    async with aiohttp.ClientSession() as session:
        async with session.post(
            f"http://{nn_kernel.ip}:{nn_kernel.port}/process/process-image",
            data=input_json,
            headers={"Content-Type": "application/json"},
        ) as response:
            resp = await response.json()
    return resp
