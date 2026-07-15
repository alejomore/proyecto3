from pydantic import BaseModel
from datetime import datetime

class Devolucion(BaseModel):
    id: int | None = None
    fecha: datetime | None = None
    motivo: str | None = None
    cliente_id: int
    usuario_id: int
    activo: bool | None = None