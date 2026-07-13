from pydantic import BaseModel

class DetalleDevolucion(BaseModel):
    id: int | None = None
    devolucion_id: int
    producto_id: int
    cantidad: float