from pydantic import BaseModel, Field

class CrearUsuario(BaseModel):
    nombre: str = Field(..., min_length=3, max_length=50, example="Juanito Doe")
    edad: int = Field(..., ge=1, le=125, description="Edad válida entre 1 y 125")