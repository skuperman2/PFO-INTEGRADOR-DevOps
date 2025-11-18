import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager


# --- Configuración de SQLite (configurable por entorno) ---
# Prioridad: DATABASE_URL env var -> SQLITE_PATH env var -> default ./ecomdata.db
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    sqlite_path = os.getenv("SQLITE_PATH", "./ecomdata.db")
    # construct sqlite URL (relative or absolute path)
    DATABASE_URL = f"sqlite+aiosqlite:///{sqlite_path}"

# Controlar el logging de SQLAlchemy por variable de entorno (false por defecto en prod)
ECHO = os.getenv("SQLALCHEMY_ECHO", "false").lower() in ("1", "true", "yes")

engine = create_async_engine(DATABASE_URL, echo=ECHO, future=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


# -- Función get_db() para usar en rutas ---
@asynccontextmanager
async def get_db():
    """Provee una sesión de base de datos asíncrona para usar en rutas.

    Hace rollback si ocurre una excepción durante el uso de la sesión,
    y cierra la sesión siempre al finalizar.
    """
    async with AsyncSessionLocal() as session:
        try:
            yield session
        except Exception:
            # Asegurar rollback en caso de error antes de propagar la excepción
            try:
                await session.rollback()
            except Exception:
                pass
            raise
        finally:
            await session.close()