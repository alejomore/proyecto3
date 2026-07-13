from fastapi import APIRouter, HTTPException, status
from database import supabase
from models.proveedor import Proveedor

router = APIRouter(
    prefix="/proveedores",
    tags=["Proveedores"]
)

# ==============================
# Obtener todos los proveedores
# ==============================
@router.get("/")
def obtener_proveedores():

    data = (
        supabase
        .table("proveedores")
        .select("*")
        .execute()
    )

    return data.data


# ==============================
# Obtener proveedor por ID
# ==============================
@router.get("/{proveedor_id}")
def obtener_proveedor(proveedor_id: int):

    data = (
        supabase
        .table("proveedores")
        .select("*")
        .eq("id", proveedor_id)
        .execute()
    )

    if len(data.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado."
        )

    return data.data[0]


# ==============================
# Crear proveedor
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_proveedor(proveedor: Proveedor):

    datos = proveedor.model_dump(exclude={"id", "created_at"})

    data = (
        supabase
        .table("proveedores")
        .insert(datos)
        .execute()
    )

    return data.data


# ==============================
# Actualizar proveedor
# ==============================
@router.put("/{proveedor_id}")
def actualizar_proveedor(proveedor_id: int, proveedor: Proveedor):

    existe = (
        supabase
        .table("proveedores")
        .select("*")
        .eq("id", proveedor_id)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado."
        )

    datos = proveedor.model_dump(exclude={"id", "created_at"})

    data = (
        supabase
        .table("proveedores")
        .update(datos)
        .eq("id", proveedor_id)
        .execute()
    )

    return data.data


# ==============================
# Eliminar proveedor
# ==============================
@router.delete("/{proveedor_id}")
def eliminar_proveedor(proveedor_id: int):

    existe = (
        supabase
        .table("proveedores")
        .select("id")
        .eq("id", proveedor_id)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Proveedor no encontrado."
        )

    (
        supabase
        .table("proveedores")
        .delete()
        .eq("id", proveedor_id)
        .execute()
    )

    return {
        "message": "Proveedor eliminado correctamente."
    }