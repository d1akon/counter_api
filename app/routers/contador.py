#----- IMPORTS
from fastapi import APIRouter, HTTPException
from utils.redis_client import redis_client, COUNTER_KEY
from models.contador import ContadorResponse
from utils.logger import logger

#----- DEFINICIÓN DE ROUTER
router = APIRouter(
    prefix="/contador",
    tags=["Contador"]
)

@router.get("/", response_model=ContadorResponse)
async def obtener_contador():
    try:
        valor_contador = await redis_client.get(COUNTER_KEY)
        if valor_contador is None:
            valor_contador = 0 #----- si el contador no existe, inicializarlo en 0
        logger.info(f"valor contador: {valor_contador}")
    except Exception as e:
        logger.error(f"Fallo al querer obtener el contador: {e}")
        raise HTTPException(status_code=500, detail=f"Fallo al querer obtener el contador: {e}")
    
    return {"contador": int(valor_contador)}
