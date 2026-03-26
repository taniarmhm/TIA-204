from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

security = HTTPBasic()

def verificar_peticion(credentials: HTTPBasicCredentials = Depends(security)):
    usuarioAut = secrets.compare_digest(credentials.username, "main")
    passAut = secrets.compare_digest(credentials.password, "123456")

    if not (usuarioAut and passAut):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales no autorizadas"
        )

    return credentials.username