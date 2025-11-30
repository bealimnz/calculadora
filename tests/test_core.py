import pytest
from src.calculadora.core import Calculator

# Cria uma instância da calculadora para ser usada em todos os testes
@pytest.fixture
def calculator():
    """Instância da calculadora para testes."""
    return Calculator()

# --- Testes para Operações Aritméticas Básicas ---

def test_add_two_numbers(calculator):
    """Verifica a função de soma (adição)."""
    assert calculator.add(5, 3) == 8.0
    assert calculator.add(-1, 1) == 0.0
    assert calculator.add(1.5, 2.5) == 4.0

def test_subtract_two_numbers(calculator):
    """Verifica a função de subtração."""
    assert calculator.subtract(10, 4) == 6.0
    assert calculator.subtract(5, 10) == -5.0
    assert calculator.subtract(100, 0) == 100.0

def test_multiply_two_numbers(calculator):
    """Verifica a função de multiplicação."""
    assert calculator.multiply(6, 7) == 42.0
    assert calculator.multiply(2.5, 2) == 5.0
    assert calculator.multiply(5, 0) == 0.0

def test_divide_two_numbers(calculator):
    """Verifica a função de divisão."""
    assert calculator.divide(10, 2) == 5.0
    assert calculator.divide(1, 4) == 0.25
    assert calculator.divide(100, 10) == 10.0

# --- Teste para Exceção (Divisão por Zero) ---

def test_divide_by_zero(calculator):
    """Verifica se a divisão por zero levanta um ValueError."""
    with pytest.raises(ValueError, match="Não é possível dividir por zero."):
        calculator.divide(10, 0)

# --- Novos Testes para Funções Avançadas ---

def test_power_function(calculator):
    """Verifica a função de potenciação (power)."""
    assert calculator.power(2, 3) == 8.0     # 2³ = 8
    assert calculator.power(5, 0) == 1.0     # 5⁰ = 1
    assert calculator.power(4, 0.5) == 2.0   # 4^(1/2) = 2 (Raiz quadrada)

def test_square_root_function_positive(calculator):
    """Verifica a função de raiz quadrada (square_root) para números positivos."""
    assert calculator.square_root(9) == 3.0
    assert calculator.square_root(0) == 0.0
    assert calculator.square_root(25) == 5.0
    assert calculator.square_root(1.44) == 1.2

def test_square_root_negative_number(calculator):
    """Verifica se a raiz quadrada de um número negativo levanta um ValueError."""
    with pytest.raises(ValueError, match="Não é possível calcular a raiz quadrada de um número negativo."):
        calculator.square_root(-4)