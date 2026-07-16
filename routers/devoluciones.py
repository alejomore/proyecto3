from fastapi import APIRouter, HTTPException, status
from database import supabase
from models.devolucion import Devolucion

router = APIRouter(
    prefix="/devoluciones",
    tags=["Devoluciones"]
)

# ==============================
# Obtener todas las devoluciones
# ==============================
@router.get("/")
def obtener_devoluciones():
    data = (
        supabase
        .table("devoluciones")
        .select("*")
        .eq("activo", True)
        .execute()
    )
    return data.data


# ==============================
# Obtener devolución por ID
# ==============================
@router.get("/{devolucion_id}")
def obtener_devolucion(devolucion_id: int):
    data = (
        supabase
        .table("devoluciones")
        .select("*")
        .eq("id", devolucion_id)
        .eq("activo", True)
        .execute()
    )

    if len(data.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Devolución no encontrada."
        )

    return data.data[0]


# ==============================
# Crear devolución
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_devolucion(devolucion: Devolucion):
    datos = devolucion.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("devoluciones")
        .insert(datos)
        .execute()
    )
    return data.data


# ==============================
# Actualizar devolución
# ==============================
@router.put("/{devolucion_id}")
def actualizar_devolucion(devolucion_id: int, devolucion: Devolucion):
    existe = (
        supabase
        .table("devoluciones")
        .select("*")
        .eq("id", devolucion_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Devolución no encontrada."
        )

    datos = devolucion.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("devoluciones")
        .update(datos)
        .eq("id", devolucion_id)
        .execute()
    )
    return data.data


# ==============================
# Eliminar devolución (Soft Delete)
# ==============================
@router.delete("/{devolucion_id}")
def eliminar_devolucion(devolucion_id: int):
    existe = (
        supabase
        .table("devoluciones")
        .select("id")
        .eq("id", devolucion_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Devolución no encontrada."
        )

    (
        supabase
        .table("devoluciones")
        .update({"activo": False})
        .eq("id", devolucion_id)
        .execute()
    )

    return {
        "message": "Devolución eliminada correctamente."
    }