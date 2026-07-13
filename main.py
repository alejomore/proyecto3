from fastapi import FastAPI

from routers import (
    productos,
    clientes,
    usuarios,
    ventas,
    inventario,
    devoluciones,
    proveedores
)

app = FastAPI(
    title="API ANCISA",
    description="Sistema REST para la gestión comercial de ANCISA S.A.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "API ANCISA funcionando correctamente"
    }

app.include_router(productos.router)
app.include_router(clientes.router)
app.include_router(usuarios.router)
app.include_router(ventas.router)
app.include_router(inventario.router)
app.include_router(devoluciones.router)
app.include_router(proveedores.router)