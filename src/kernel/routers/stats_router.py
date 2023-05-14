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

stats_router = APIRouter(prefix="/stats", tags=["Stats"])


@stats_router.get("/kernels")
async def get_kernels():
    return config_provider.NNKernels


@stats_router.get("/kernels/types")
async def get_kernels():
    return list(set([i.type for i in config_provider.NNKernels]))


@stats_router.get("/kernels/ips")
async def get_kernels():
    return list(set([f"{i.ip}:{i.port}" for i in config_provider.NNKernels]))


@stats_router.get("/kernels/titles")
async def get_kernels():
    return list(set([i.title for i in config_provider.NNKernels]))
