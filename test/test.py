from src.Main import calcular_soma, calcular_divisao, calcular_subtracao


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