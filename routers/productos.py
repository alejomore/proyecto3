from fastapi import APIRouter, HTTPException, status
from database import supabase
from models.producto import Producto

router = APIRouter(
    prefix="/productos",
    tags=["Productos"]
)

# ==============================
# Obtener todos los productos
# ==============================
@router.get("/")
def obtener_productos():
    data = supabase.table("productos").select("*").execute()
    return data.data


# ==============================
# Obtener producto por ID
# ==============================
@router.get("/{producto_id}")
def obtener_producto(producto_id: int):

    data = (
        supabase
        .table("productos")
        .select("*")
        .eq("id", producto_id)
        .execute()
    )

    if len(data.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado."
        )

    return data.data[0]


# ==============================
# Crear producto
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(producto: Producto):

    datos = producto.model_dump(exclude={"id", "created_at"})

    data = (
        supabase
        .table("productos")
        .insert(datos)
        .execute()
    )

    return data.data


# ==============================
# Actualizar producto
# ==============================
@router.put("/{producto_id}")
def actualizar_producto(producto_id: int, producto: Producto):

    existe = (
        supabase
        .table("productos")
        .select("*")
        .eq("id", producto_id)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado."
        )

    datos = producto.model_dump(exclude={"id", "created_at"})

    data = (
        supabase
        .table("productos")
        .update(datos)
        .eq("id", producto_id)
        .execute()
    )

    return data.data


# ==============================
# Eliminar producto
# ==============================
@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int):

    existe = (
        supabase
        .table("productos")
        .select("id")
        .eq("id", producto_id)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado."
        )

    (
        supabase
        .table("productos")
        .delete()
        .eq("id", producto_id)
        .execute()
    )

    return {
        "message": "Producto eliminado correctamente."
    }