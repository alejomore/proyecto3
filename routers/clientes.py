from fastapi import APIRouter, HTTPException, status
from database import supabase
from models.cliente import Cliente

router = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

# ==============================
# Obtener todos los clientes
# ==============================
@router.get("/")
def obtener_clientes():

    data = (
        supabase
        .table("clientes")
        .select("*")
        .eq("activo", True)
        .execute()
    )

    return data.data


# ==============================
# Obtener cliente por ID
# ==============================
@router.get("/{cliente_id}")
def obtener_cliente(cliente_id: int):

    data = (
        supabase
        .table("clientes")
        .select("*")
        .eq("id", cliente_id)
        .eq("activo", True)
        .execute()
    )

    if len(data.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado."
        )

    return data.data[0]


# ==============================
# Crear cliente
# ==============================
@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: Cliente):

    datos = cliente.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("clientes")
        .insert(datos)
        .execute()
    )

    return data.data


# ==============================
# Actualizar cliente
# ==============================
@router.put("/{cliente_id}")
def actualizar_cliente(cliente_id: int, cliente: Cliente):

    existe = (
        supabase
        .table("clientes")
        .select("*")
        .eq("id", cliente_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado."
        )

    datos = cliente.model_dump(
        exclude={"id", "created_at", "activo"},
        mode="json"
    )

    data = (
        supabase
        .table("clientes")
        .update(datos)
        .eq("id", cliente_id)
        .execute()
    )

    return data.data


# ==============================
# Eliminar cliente (Soft Delete)
# ==============================
@router.delete("/{cliente_id}")
def eliminar_cliente(cliente_id: int):

    existe = (
        supabase
        .table("clientes")
        .select("id")
        .eq("id", cliente_id)
        .eq("activo", True)
        .execute()
    )

    if len(existe.data) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado."
        )

    (
        supabase
        .table("clientes")
        .update({"activo": False})
        .eq("id", cliente_id)
        .execute()
    )

    return {
        "message": "Cliente eliminado correctamente."
    }