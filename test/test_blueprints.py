# test_blueprints.py
"""
Prueba de integración: Verifica que todos los blueprints están registrados en la app.
"""
import pytest
import app

@pytest.mark.asyncio
async def test_blueprints_registered():
    blueprints = app.app.blueprints.keys()
    # Lista esperada de blueprints (puedes actualizarla si agregas más)
    expected = [
        "administracion", "analisis_negocio_clientes", "analisis_negocio_productos", "analisis_negocio_resumen",
        "auth", "catalogo_categorias", "catalogo_productos", "clientes", "configuracion_general",
        "configuracion_notificaciones", "configuracion_seguridad", "inicio", "inventario", "inventario_agregar",
        "nueva_categoria", "nuevo_producto", "pagos", "pagos_nuevo_pago", "panel", "reportes", "usuarios",
        "usuarios_agregar", "ventas", "ventas_carrito"
    ]
    for bp in expected:
        assert bp in blueprints
