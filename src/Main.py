#Criação da Main

def calcular_soma(numero1: int, numero2: int) -> int:
    return numero1 + numero2

def calcular_divisao(numero1: int, numero2: int):
    if numero2 != 0:
        return numero1 / numero2
    return "Indefinida (divisão por zero)"

def calcular_subtracao(numero1: int, numero2: int) -> int:
    return numero1 - numero2

def e_par(numero: int) -> bool:
    return numero % 2 == 0

def calcular_potencia(base: int, expoente: int):
    return base ** expoente

# Bloco 1
def executar():
    numero1 = int(input("(alterado)Digite o primeiro número: "))
    numero2 = int(input("(alterado)Digite o segundo número: "))

# Bloco 2
    soma = calcular_soma(numero1, numero2)
    divisao = calcular_divisao(numero1, numero2)
    subtracao = calcular_subtracao(numero1, numero2)
    potencia = calcular_potencia(numero1, numero2)

    # Bloco 3
    print("A soma é:", soma)
    print("A divisão é:", divisao)
    print("A subtração é:", subtracao)
    print("A potência é:", potencia)

if __name__ == "_main_":
    executar()


