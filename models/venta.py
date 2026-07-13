from pydantic import BaseModel

class Venta(BaseModel):
    id: int | None = None
    fecha: str | None = None
    total: float
    cliente_id: int
    usuario_id: int