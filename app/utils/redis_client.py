#----- IMPORTS
import redis.asyncio as redis
import os
from utils.logger import logger

#----- VARIABLES
REDIS_DB = int(os.getenv("REDIS_DB", 0))
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
COUNTER_KEY = "contador_api"

#----- CLIENTE REDIS
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)
logger.info(f"Configurado sv Redis en {REDIS_HOST}:{REDIS_PORT}, DB: {REDIS_DB}")