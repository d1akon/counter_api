#----- IMPORTS
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
from utils.redis_client import redis_client, COUNTER_KEY

#----- DEFINICIÓN DE ROUTER
router = APIRouter(
    prefix="/fecha",
    tags=["Fecha"]
)

class FechaRequest(BaseModel):
    mostrar_hora: bool

@router.post("/", response_model=dict)
async def obtener_fecha(fecha_request: FechaRequest):
    try:
        #----- incremento del contador cada vez que le pegan a este endpoint
        contador = await redis_client.incr(COUNTER_KEY)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Fallo al aumentar el contador, error: {e}")
    
    #----- si está el "mostrar hora" como true, devuelve tambien la hora además dela fecha
    if fecha_request.mostrar_hora:
        fecha_formateada = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    else:
        fecha_formateada = datetime.now().strftime("%Y-%m-%d")
    
    return {"fecha": fecha_formateada, "contador": contador}
