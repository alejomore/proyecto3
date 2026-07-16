from fastapi import APIRouter, HTTPException, status
from database import supabase
from models.inventario import Inventario

router = APIRouter(
    prefix="/inventario",
    tags=["Inventario"]
)

# ==============================
# Obtener todo el inventario
# ==============================
@router.get("/")
def obtener_inventarios():
    data = (
        supabase
        .table("inventario")
        .select("*")
        .eq("activo", True)
        .execute()
    )
    return data.data


# ==============================
# Obtener item de inventario por ID
# ==============================
@router.get("/{inventario_id}")
def obtener_inventario(inventario_id: int):
    data = (
        supabase
        .table("inventario")
        .select("*")
        .eq("id", inventario_id)
        .eq("activo", True)
        .execute()
    )

    if len(data.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro de inventario no encontrado."
        )

    return data.data[0]


# ==============================
# Crear registro de inventario
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_inventario(inventario: Inventario):
    datos = inventario.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("inventario")
        .insert(datos)
        .execute()
    )
    return data.data


# ==============================
# Actualizar registro de inventario
# ==============================
@router.put("/{inventario_id}")
def actualizar_inventario(inventario_id: int, inventario: Inventario):
    existe = (
        supabase
        .table("inventario")
        .select("*")
        .eq("id", inventario_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro de inventario no encontrado."
        )

    datos = inventario.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("inventario")
        .update(datos)
        .eq("id", inventario_id)
        .execute()
    )
    return data.data


# ==============================
# Eliminar registro de inventario (Soft Delete)
# ==============================
@router.delete("/{inventario_id}")
def eliminar_inventario(inventario_id: int):
    existe = (
        supabase
        .table("inventario")
        .select("id")
        .eq("id", inventario_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Registro de inventario no encontrado."
        )

    (
        supabase
        .table("inventario")
        .update({"activo": False})
        .eq("id", inventario_id)
        .execute()
    )

    return {
        "message": "Registro de inventario eliminado correctamente."
    }