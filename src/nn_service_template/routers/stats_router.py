import pathlib
import uuid
import aiofiles
from fastapi import APIRouter, UploadFile
from typing import List, Optional, Union
import os

router_stats = APIRouter(prefix="/stats", tags=["Statistics"])


@router_stats.get("/main")
async def process_file():
    return True
