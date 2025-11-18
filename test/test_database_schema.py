# test_database_schema.py
"""
Prueba de integración: Verifica que las tablas principales existen en la base de datos.
"""
import pytest
import sqlite3

DB_PATH = "ecomdata.db"
TABLES = [
    "categorias", "clientes", "configuracion_general", "configuracion_notificaciones", "configuracion_seguridad", "detalle_ventas", "inventario", "pagos", "productos", "roles", "usuarios", "ventas"
]

def test_database_tables_exist():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    for table in TABLES:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}';")
        result = cursor.fetchone()
        assert result is not None, f"Tabla {table} no existe"
    conn.close()
