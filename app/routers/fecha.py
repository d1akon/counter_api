#----- IMPORTS
from fastapi import APIRouter, HTTPException
#from pydantic import BaseModel
from datetime import datetime
from utils.redis_client import redis_client, COUNTER_KEY
from models.fecha import FechaRequest, FechaResponse
from utils.logger import logger

#----- DEFINICIÓN DE ROUTER
router = APIRouter(
    prefix="/fecha",
    tags=["Fecha"]
)

@router.post("/", response_model=FechaResponse)
async def obtener_fecha(fecha_request: FechaRequest):
    try:
        #----- incremento del contador cada vez que le pegan a este endpoint
        contador = await redis_client.incr(COUNTER_KEY)
        logger.info(f"Contador incrementado a: {contador}")
    except Exception as e:
        logger.error(f"Fallo al aumentar el contador, error: {e}")
        raise HTTPException(status_code=500, detail=f"Fallo al aumentar el contador, error: {e}")
    
    #----- si está el "mostrar hora" como true, devuelve tambien la hora además dela fecha
    if fecha_request.mostrar_hora:
        fecha_formateada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        fecha_formateada = datetime.now().strftime("%Y-%m-%d")
    
    logger.info(f"Fecha devuelta: {fecha_formateada}")
    return {"fecha": fecha_formateada}
