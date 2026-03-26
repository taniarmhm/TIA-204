from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔥 CAMBIO IMPORTANTE: usar localhost
DATABASE_URL = "postgresql://admin:123456@localhost:5432/DB_miapi"

# Motor de conexión
engine = create_engine(DATABASE_URL)

# Sesiones
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base para modelos
Base = declarative_base()

# Dependencia
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()