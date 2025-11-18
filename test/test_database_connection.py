# test_database_connection.py
"""
Prueba de integración: Verifica la conexión a la base de datos SQLite.
"""
import pytest
import sqlite3

DB_PATH = "ecomdata.db"

def test_database_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        assert len(tables) > 0
    finally:
        conn.close()
