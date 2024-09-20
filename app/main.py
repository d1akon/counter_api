#----- IMPORTS
from fastapi import FastAPI
import os
from routers import fecha, contador
from utils.redis_client import redis_client
import asyncio
from utils.logger import logger


app = FastAPI(
    title="counter_api con Redis y Docker",
    version="1.0.3",
    description="API que muestra la fecha y un contador de llamadas usando Redis para persistencia de los counts."
)

#----- ROUTERS DEFINIDAS
app.include_router(fecha.router)
app.include_router(contador.router)

#----- INICIAR CONEXION CON SV REDIS
@app.on_event("startup")
async def startup_event():
    try:
        await redis_client.ping() #----- validando si está el sv activo
        logger.info("Conexión a sv Redis establecida correctamente.")
    except Exception as e:
        logger.error(f"Error al conectar con sv Redis: {e}")
        raise e

#----- CERRAR CONEXION CON SV REDIS
@app.on_event("shutdown")
async def shutdown_event():
    try:
        await redis_client.close() #----- cerrando conexion con sv
        logger.info("Conexión a sv Redis cerrada.")
    except Exception as e:
        logger.error(f"Error al cerrar la conexión con sv Redis: {e}")
