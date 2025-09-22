# test_integracao
from src.Main import executar
from unittest.mock import patch
import io
import sys

def test_executar_inteiro():
    with patch("builtins.input", side_effect=["8", "2"]), patch("sys.stdout", new_callable=io.StringIO) as fake_stdout:
        executar()
        saida = fake_stdout.getvalue()
        assert "A soma é: 10" in saida
        assert "A divisão é: 4.0" in saida
