from fastapi import APIRouter, HTTPException, status
from database import supabase
from models.usuario import Usuario

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

# ==============================
# Obtener todos los usuarios
# ==============================
@router.get("/")
def obtener_usuarios():
    data = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("activo", True)
        .execute()
    )
    return data.data


# ==============================
# Obtener usuario por ID
# ==============================
@router.get("/{usuario_id}")
def obtener_usuario(usuario_id: int):
    data = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("id", usuario_id)
        .eq("activo", True)
        .execute()
    )

    if len(data.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado."
        )

    return data.data[0]


# ==============================
# Crear usuario
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: Usuario):
    datos = usuario.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("usuarios")
        .insert(datos)
        .execute()
    )
    return data.data


# ==============================
# Actualizar usuario
# ==============================
@router.put("/{usuario_id}")
def actualizar_usuario(usuario_id: int, usuario: Usuario):
    existe = (
        supabase
        .table("usuarios")
        .select("*")
        .eq("id", usuario_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado."
        )

    datos = usuario.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("usuarios")
        .update(datos)
        .eq("id", usuario_id)
        .execute()
    )
    return data.data


# ==============================
# Eliminar usuario (Soft Delete)
# ==============================
@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int):
    existe = (
        supabase
        .table("usuarios")
        .select("id")
        .eq("id", usuario_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado."
        )

    (
        supabase
        .table("usuarios")
        .update({"activo": False})
        .eq("id", usuario_id)
        .execute()
    )

    return {
        "message": "Usuario eliminado correctamente."
    }