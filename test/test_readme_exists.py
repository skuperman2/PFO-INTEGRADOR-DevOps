# test_readme_exists.py
"""
Prueba unitaria: Verifica que el archivo README.md existe en la raíz.
"""
import os

def test_readme_exists():
    assert os.path.exists("README.md")
