from pydantic import BaseModel

class Rol(BaseModel):
    id: int | None = None
    nombre: str
    descripcion: str | None = None
    created_at: str | None = None
    activo: bool | None = None 