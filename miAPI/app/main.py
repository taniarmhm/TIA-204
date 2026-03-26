from fastapi import FastAPI
from app.routers import usuarios, varios
from app.data.db import engine, Base

# Crear tablas
#Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mi Primer API",
    description="Tania Mejia Moreno",
    version="1.0"
)

# Rutas
app.include_router(usuarios.router)
app.include_router(varios.routerV)
