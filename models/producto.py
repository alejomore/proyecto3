from datetime import date
from pydantic import BaseModel

class Producto(BaseModel):
    id: int | None = None
    nombre: str
    precio_base: float
    peso: float | None = None
    stock: float
    fecha_vencimiento: date | None = None
    created_at: str | None = None
    activo: bool | None = None