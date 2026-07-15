from pydantic import BaseModel

class Cliente(BaseModel):
    id: int | None = None
    nombre: str
    telefono: str | None = None
    direccion: str | None = None
    tipo_cliente: str
    created_at: str | None = None
    activo: bool | None = None