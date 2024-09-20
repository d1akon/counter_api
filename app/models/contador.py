#----- IMPORTS
from pydantic import BaseModel, Field

#----- DEFINICIONES DE MODELOS
class ContadorResponse(BaseModel):
    contador: int = Field(
        ...,
        title="Contador",
        description="Cant total de llamadas al endpoint /fecha."
    )
