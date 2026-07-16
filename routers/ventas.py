from fastapi import APIRouter, HTTPException, status
from database import supabase
from models.venta import Venta

router = APIRouter(
    prefix="/ventas",
    tags=["Ventas"]
)

# ==============================
# Obtener todas las ventas
# ==============================
@router.get("/")
def obtener_ventas():
    data = (
        supabase
        .table("ventas")
        .select("*")
        .eq("activo", True)
        .execute()
    )
    return data.data


# ==============================
# Obtener venta por ID
# ==============================
@router.get("/{venta_id}")
def obtener_venta(venta_id: int):
    data = (
        supabase
        .table("ventas")
        .select("*")
        .eq("id", venta_id)
        .eq("activo", True)
        .execute()
    )

    if len(data.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venta no encontrada."
        )

    return data.data[0]


# ==============================
# Crear venta
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_venta(venta: Venta):
    datos = venta.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("ventas")
        .insert(datos)
        .execute()
    )
    return data.data


# ==============================
# Actualizar venta
# ==============================
@router.put("/{venta_id}")
def actualizar_venta(venta_id: int, venta: Venta):
    existe = (
        supabase
        .table("ventas")
        .select("*")
        .eq("id", venta_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venta no encontrada."
        )

    datos = venta.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("ventas")
        .update(datos)
        .eq("id", venta_id)
        .execute()
    )
    return data.data


# ==============================
# Eliminar venta (Soft Delete)
# ==============================
@router.delete("/{venta_id}")
def eliminar_venta(venta_id: int):
    existe = (
        supabase
        .table("ventas")
        .select("id")
        .eq("id", venta_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Venta no encontrada."
        )

    (
        supabase
        .table("ventas")
        .update({"activo": False})
        .eq("id", venta_id)
        .execute()
    )

    return {
        "message": "Venta eliminada correctamente."
    }