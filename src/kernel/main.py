from fastapi import FastAPI
from starlette import status
from starlette.responses import Response

from kernel.routers.NN_process_router import main_router
from kernel.routers.stats_router import stats_router

app = FastAPI()

app.include_router(main_router)
app.include_router(stats_router)
