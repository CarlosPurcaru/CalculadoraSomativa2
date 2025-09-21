
from src.Main import calcular_soma, calcular_divisao, calcular_subtracao, e_par, calcular_potencia

def test_calcular_soma():
    assert calcular_soma(3, 5) == 8
    assert calcular_soma(-2, 2) == 0

def test_calcular_divisao():
    assert calcular_divisao(10, 2) == 5
    assert calcular_divisao(9, 3) == 3
    assert calcular_divisao(5, 0) == "Indefinida (divisão por zero)"

def test_calcular_subtracao():
    assert calcular_subtracao(10, 5) == 5
    assert calcular_subtracao(5, 10) == -5

def test_e_par():
    assert e_par(4) is True
    assert e_par(5) is False

def test_calcular_potencia():
    assert calcular_potencia(2, 3) == 8
    assert calcular_potencia(5, 0) == 1
    assert calcular_potencia(-2, 3) == -8


   
