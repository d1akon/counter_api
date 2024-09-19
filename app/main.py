from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import redis.asyncio as redis
import os

app = FastAPI(title="API de Fecha y Contador con Redis en Docker", version="1.0.2")

class FechaRequest(BaseModel):
    mostrar_hora: bool

REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
REDIS_DB = int(os.getenv("REDIS_DB", 0))
COUNTER_KEY = "contador_api"

redis_client: redis.Redis = None

@app.on_event("startup")
async def startup_event():
    global redis_client
    try:
        redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
        await redis_client.ping()
        print("Conexión a Redis establecida correctamente.")
    except Exception as e:
        print(f"Error al conectar con Redis: {e}")
        raise e

@app.on_event("shutdown")
async def shutdown_event():
    global redis_client
    if redis_client:
        await redis_client.close()
        print("Conexión a Redis cerrada.")

@app.post("/fecha", response_model=dict)
async def obtener_fecha(fecha_request: FechaRequest):
    global redis_client
    try:
        # Incrementa el contador de manera atómica
        contador = await redis_client.incr(COUNTER_KEY)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al incrementar el contador: {e}")
    
    ahora = datetime.now()
    if fecha_request.mostrar_hora:
        fecha_formateada = ahora.strftime("%Y-%m-%d %H:%M:%S")
    else:
        fecha_formateada = ahora.strftime("%Y-%d-%m")
    
    return {"fecha": fecha_formateada}

@app.get("/contador", response_model=dict)
async def obtener_contador():
    global redis_client
    try:
        valor_contador = await redis_client.get(COUNTER_KEY)
        # Si el contador no existe, inicialízalo en 0
        if valor_contador is None:
            valor_contador = 0
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener el contador: {e}")
    
    return {"contador": int(valor_contador)}
