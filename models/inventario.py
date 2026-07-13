from pydantic import BaseModel

class Inventario(BaseModel):
    id: int | None = None
    producto_id: int
    tipo_movimiento: str
    cantidad: float
    fecha: str | None = None