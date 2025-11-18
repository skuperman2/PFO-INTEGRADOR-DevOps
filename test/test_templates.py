# test_templates.py
"""
Prueba unitaria: Verifica que todos los archivos de templates existen.
"""
import pytest
import os

TEMPLATES_DIR = "templates"
TEMPLATES = [
    "administracion.html", "analisis-negocio-cliente.html", "analisis-negocio-producto.html", "analisis-negocio-resumen.html",
    "catalogo-categorias.html", "catalogo-productos.html", "clientes.html", "configuracion_general.html",
    "configuracion_notificaciones.html", "configuracion_seguridad.html", "index.html", "inventario-agregar-producto.html",
    "inventario.html", "login.html", "modal-nueva-categoria.html", "modal-nuevo-producto.html", "pagos-nuevo-pago.html",
    "pagos.html", "panel.html", "reportes.html", "usuario-agregar-usuario.html", "usuario.html", "ventas-carrito.html",
    "ventas.html"
]

@pytest.mark.parametrize("template_file", TEMPLATES)
def test_template_exists(template_file):
    assert os.path.exists(os.path.join(TEMPLATES_DIR, template_file))
