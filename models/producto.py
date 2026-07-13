from pydantic import BaseModel, EmailStr

class Producto(BaseModel):
    id: int | None = None
    nombre: str
    precio: float
    stock: int
    created_at: str | None = None