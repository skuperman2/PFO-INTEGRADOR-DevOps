# test_scripts_import.py
"""
Prueba unitaria: Verifica que los scripts de la carpeta scripts se importan correctamente.
"""
import pytest
import importlib.util
import os

SCRIPTS_DIR = "scripts"

@pytest.mark.parametrize("script_file", [
    f[:-3] for f in os.listdir(SCRIPTS_DIR) if f.endswith(".py") and not f.startswith("__")
])
def test_script_import(script_file):
    script_path = os.path.join(SCRIPTS_DIR, f"{script_file}.py")
    spec = importlib.util.spec_from_file_location(script_file, script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
