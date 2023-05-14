from fastapi import FastAPI


from nn_service_template.routers.NN_process_router import router_process
from nn_service_template.routers.stats_router import router_stats


app = FastAPI()

app.include_router(router_process)
app.include_router(router_stats)
