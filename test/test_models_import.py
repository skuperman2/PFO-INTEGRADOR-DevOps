# test_models_import.py
"""
Prueba unitaria: Verifica que todos los modelos se importan correctamente.
"""
import pytest
import importlib
import os

MODELS_DIR = "models"

@pytest.mark.parametrize("model_file", [
    f[:-3] for f in os.listdir(MODELS_DIR) if f.endswith(".py") and not f.startswith("__")
])
def test_model_import(model_file):
    module_name = f"{MODELS_DIR}.{model_file}"
    importlib.import_module(module_name)
