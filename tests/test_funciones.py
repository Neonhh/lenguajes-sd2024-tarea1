import pytest
import sys
import os
from unittest.mock import patch

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'pregunta_3')))

from funciones import *

def test_definir_programa():
    # Test case for definir function with 'PROGRAMA'
    definir(['PROGRAMA', 'test_program', 'Python'])
    assert 'test_program' in programas
    assert programas['test_program'] == 'Python'

def test_definir_interprete():
    # Test case for definir function with 'INTERPRETE'
    definir(['INTERPRETE', 'LOCAL', 'Python'])
    assert 'Python' in lenguajes

def test_definir_traductor():
    # Test case for definir function with 'TRADUCTOR'
    # Dado que LOCAL y Python son ejecutables
    definir(['TRADUCTOR', 'LOCAL', 'Javascript', 'Python'])
    # Add assertions based on the expected behavior of traductor function
    assert 'Javascript' in lenguajes

def test_definir_traductor2():
    # Test case for definir function with 'TRADUCTOR'
    # Dado que LOCAL y Python son ejecutables
    definir(['TRADUCTOR', 'C', 'Kotlin', 'Javascript'])
    assert 'Kotlin' not in lenguajes
    assert 'C' not in lenguajes

    traductor('LOCAL', 'C', 'Javascript')
    assert 'C' in lenguajes
    assert 'Kotlin' in lenguajes #cuando se revisen los traductores al agregar lenguajes

def test_ejecutable():
    # Test case for ejecutable function
    programa('test_program', 'LOCAL')
    with patch('builtins.print') as mocked_print:
        ejecutable('test_program')
        mocked_print.assert_any_call("Si, es posible ejecutar el programa 'test_program'.")

def test_ejecutable2():
    # Test case for ejecutable function
    programa('test_program2', 'Java')
    with patch('builtins.print') as mocked_print:
        ejecutable('test_program2')
        mocked_print.assert_any_call("No es posible ejecutar el programa 'test_program2'.")

def test_ejecutable3():
    # Test case for ejecutable function
    with patch('builtins.print') as mocked_print:
        ejecutable('test_program3')
        mocked_print.assert_any_call("Programa no definido.")

def test_programa():
    # Test case for programa function
    programa('test_program', 'Python')
    assert 'test_program' in programas
    assert programas['test_program'] == 'Python'

def test_programa2():
    # Test case for programa function
    with patch('builtins.print') as mocked_print:
        programa('test_program', 'Python')
        mocked_print.assert_any_call("El programa 'test_program' ya esta definido.")
        programa('test_program', 'Java')
        mocked_print.assert_any_call("El programa 'test_program' ya esta definido.")
    

def test_interprete():
    # Test case for interprete function
    interprete('LOCAL', 'Python')
    assert 'Python' in lenguajes

def test_agregar_lenguaje():
    # Test case for agregar_lenguaje function
    agregar_lenguaje('Python')
    assert 'Python' in lenguajes

if __name__ == "__main__":
    pytest.main()