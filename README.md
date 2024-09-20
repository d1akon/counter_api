# 🔢 counter_api 

### 🔹 **Descripción**
API creada con FastAPI que proporciona dos funciones principales:

* **Recibir la fecha actual:** Devuelve la fecha del dia actual, y tiene la opción de poder recibir tambien la hora.
* **Contador de Llamadas a api:** Mantiene un contador de cuántas veces se ha realizado solicitudes al endpoint /fecha de la API.

La persistencia del contador se maneja utilizando Redis, garantizando que los datos se mantengan incluso si la aplicación se reinicia. Además, la API está containerizada con Docker para facilitar su deployment y testing.

### 🔹 Requisitos Previos
* Docker & docker-compose.

### 🔹 Instalacion y uso

1. Clonar el repo a tu máquina local.
2. [OPCIONAL] Cambiar variables de entorno si es que querés cambiar los puertos de redis.
3. Ejecutar la API con docker-compose up --build 

    Esto levantará dos servicios:
    * api: La API corriendo en localhost:8000
    * redis: Servidor redis corriendo en el puerto 6379 (o el que se defina).
4. Una vez levantados los servicios, se puede acceder a la documentacion de la api entrando a http://localhost:8000/docs y probar los endpoints definidos.

    Los endpoints definidos son:
    * /contador (método GET): Devuelve el valor actual del contador.
    Respuesta:
    {
    "contador": 5
    }

    * /fecha (método POST): 
    Cuerpo de la solicitud: Devuelve la fecha actual (y la hora, segun se desee). Cada llamado aumentará en 1 el contador. El body que debe enviarse en la solicitud es el siguiente:
    {
    "mostrar_hora": true
    }

    Respuesta con hora:
    {
    "fecha": "2024-09-20 18:30:20"
    }

    Respuesta sin hora:
    {
    "fecha": "2024-09-20"
    }



