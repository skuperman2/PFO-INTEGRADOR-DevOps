# test_app_startup.py
"""
Prueba de integración: Verifica que la app Quart inicia correctamente.
"""
import pytest
from quart import Quart
import app

@pytest.mark.asyncio
async def test_app_startup():
    assert isinstance(app.app, Quart)
    test_client = app.app.test_client()
    response = await test_client.get("/")
    assert response.status_code in [200, 302, 404]  # Depende de la ruta raíz
