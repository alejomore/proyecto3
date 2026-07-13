from pydantic import BaseModel, EmailStr

class Usuario(BaseModel):
    id: int | None = None
    nombre: str
    correo: EmailStr
    password: str
    rol_id: int
    created_at: str | None = None