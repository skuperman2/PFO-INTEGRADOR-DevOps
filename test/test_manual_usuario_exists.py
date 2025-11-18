# test_manual_usuario_exists.py
"""
Prueba unitaria: Verifica que el archivo manual-usuario.md existe en la raíz.
"""
import os

def test_manual_usuario_exists():
    assert os.path.exists("manual-usuario.md")
