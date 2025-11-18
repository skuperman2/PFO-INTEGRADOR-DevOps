# test_static_files.py
"""
Prueba unitaria: Verifica que el archivo de estilos existe.
"""
import os

def test_styles_css_exists():
    assert os.path.exists("static/styles.css")
