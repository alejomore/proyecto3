from pydantic import BaseModel

class DetalleVenta(BaseModel):
    id: int | None = None
    venta_id: int
    producto_id: int
    cantidad: float
    peso: float | None = None
    precio_unitario: float