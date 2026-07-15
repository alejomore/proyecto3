from pydantic import BaseModel, EmailStr

class Proveedor(BaseModel):
    id: int | None = None
    nombre: str
    telefono: str | None = None
    correo: EmailStr | None = None
    direccion: str | None = None
    created_at: str | None = None
    activo: bool | None = None