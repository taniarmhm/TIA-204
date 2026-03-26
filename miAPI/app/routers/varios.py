import asyncio
from typing import Optional
from fastapi import APIRouter

routerV = APIRouter(tags=["Inicio"])

@routerV.get("/")
async def bienvenido():
    return {"mensaje": "Bienvenido a FastAPI"}

@routerV.get("/holaMundo")
async def hola():
    await asyncio.sleep(2)
    return {"mensaje": "Hola Mundo FastAPI", "status": "200"}

@routerV.get("/v1/ParametroOb/{id}")
async def consulta_uno(id: int):
    return {"mensaje": "Usuario encontrado", "usuario": id}

@routerV.get("/v1/ParametroOp/")
async def consulta_dos(id: Optional[int] = None):
    return {"mensaje": "Consulta opcional", "id": id}