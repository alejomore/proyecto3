from pydantic import BaseModel

class Devolucion(BaseModel):
    id: int | None = None
    fecha: str | None = None
    motivo: str | None = None
    cliente_id: int
    usuario_id: int