import pytest
from unittest.mock import patch
import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pregunta_3')))

from simuladorT import main

def test_definir():
    with patch('builtins.input', side_effect=['DEFINIR tipo arg1 arg2 arg3', 'SALIR']):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_any_call("Iniciando ejecucion del programa simuladorT.")
            mocked_print.assert_any_call("Opciones:\n DEFINIR <tipo> [<argumentos>]")
            mocked_print.assert_any_call(" EJECUTABLE <programa>\n SALIR\n")

def test_ejecutable():
    with patch('builtins.input', side_effect=['EJECUTABLE programa', 'SALIR']):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_any_call("Iniciando ejecucion del programa simuladorT.")
            mocked_print.assert_any_call("Opciones:\n DEFINIR <tipo> [<argumentos>]")
            mocked_print.assert_any_call(" EJECUTABLE <programa>\n SALIR\n")

def test_comando_no_reconocido():
    with patch('builtins.input', side_effect=['UNKNOWN', 'SALIR']):
        with patch('builtins.print') as mocked_print:
            main()
            mocked_print.assert_any_call("Iniciando ejecucion del programa simuladorT.")
            mocked_print.assert_any_call("Opciones:\n DEFINIR <tipo> [<argumentos>]")
            mocked_print.assert_any_call(" EJECUTABLE <programa>\n SALIR\n")
            mocked_print.assert_any_call("Comando no reconocido.")

if __name__ == "__main__":
    pytest.main()