#----- IMPORTS
from pydantic import BaseModel, Field
from typing import Optional

#----- DEFINICIONES DE MODELOS
class FechaRequest(BaseModel):
    mostrar_hora: bool = Field(
        ...,
        title="Mostrar Hora",
        description="Informa si se debe mostrar la hora en la respuesta. true: se muestra; false: no se muestra"
    )

class FechaResponse(BaseModel):
    fecha: str = Field(
        ...,
        title="Fecha",
        description="Fecha actual en formato YYYY-MM-DD o YYYY-MM-DD HH:MM:SS."
    )
