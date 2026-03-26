from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.usuarios import CrearUsuario
from app.data.db import get_db
from app.data.usuario import Usuario as UsuarioDB
from app.security.auth import verificar_peticion

router = APIRouter(
    prefix="/v1/usuarios",
    tags=["CRUD HTTP"],
    dependencies=[Depends(verificar_peticion)]
)

# Obtener todos
@router.get("/")
def obtener_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(UsuarioDB).all()
    return {
        "status": "200",
        "total": len(usuarios),
        "usuarios": usuarios
    }

# Crear usuario
@router.post("/")
def crear_usuario(usuario: CrearUsuario, db: Session = Depends(get_db)):
    nuevo = UsuarioDB(
        nombre=usuario.nombre,
        edad=usuario.edad
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)

    return {
        "status": "201",
        "mensaje": "Usuario creado",
        "usuario": nuevo
    }