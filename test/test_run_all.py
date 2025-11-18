# test_run_all.py
"""
Este script ejecuta todas las pruebas del directorio test usando pytest.
"""
import pytest
import sys

if __name__ == "__main__":
    sys.exit(pytest.main(["test"]))
