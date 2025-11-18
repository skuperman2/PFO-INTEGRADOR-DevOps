import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager


# --- Configuración de SQLite (configurable por entorno) ---
# Prioridad: DATABASE_URL env var -> SQLITE_PATH env var -> default ./ecomdata.db
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    sqlite_path = os.getenv("SQLITE_PATH", "./ecomdata.db")
    # If absolute path, ensure URL has the correct slashes
    if os.path.isabs(sqlite_path):
        DATABASE_URL = f"sqlite+aiosqlite:///{sqlite_path}"
    else:
        DATABASE_URL = f"sqlite+aiosqlite:///{sqlite_path}"

engine = create_async_engine(DATABASE_URL, echo=True, future=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


# -- Función get_db() para usar en rutas ---
@asynccontextmanager
async def get_db():
    """Provee una sesión de base de datos asíncrona para usar en rutas."""
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()