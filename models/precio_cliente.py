from pydantic import BaseModel

class PrecioCliente(BaseModel):
    id: int | None = None
    producto_id: int
    tipo_cliente: str
    cantidad_minima: float
    precio: float
    created_at: str | None = None
    activo: bool | None = None