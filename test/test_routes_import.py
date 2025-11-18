# test_routes_import.py
"""
Prueba unitaria: Verifica que todos los archivos de rutas se importan correctamente.
"""
import pytest
import importlib
import os

ROUTES_DIR = "routes"

# Archivos que han sido movidos y lanzan RuntimeError
IGNORED_ROUTES = {"categoria_routes", "cliente_routes", "pago_routes", "producto_routes", "venta_routes"}

@pytest.mark.parametrize("route_file", [
    f[:-3] for f in os.listdir(ROUTES_DIR) if f.endswith(".py") and not f.startswith("__")
])
def test_route_import(route_file):
    if route_file in IGNORED_ROUTES:
        pytest.skip(f"{route_file} fue movido a legacy_routes y lanza RuntimeError")
    module_name = f"{ROUTES_DIR}.{route_file}"
    importlib.import_module(module_name)
