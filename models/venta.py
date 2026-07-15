from pydantic import BaseModel
from datetime import datetime

class Venta(BaseModel):
    id: int | None = None
    fecha: datetime | None = None
    total: float
    cliente_id: int
    usuario_id: int
    activo: bool | None = None