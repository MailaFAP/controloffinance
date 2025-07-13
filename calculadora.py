"""
Módulo de calculadora com funções básicas e validação de tipos.
"""
def validar_numeros(func):
    """Decorador que garante que os argumentos são números (int ou float)."""
    def wrapper(a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Os argumentos devem ser números (int ou float).")
        return func(a, b)
    return wrapper

@validar_numeros
def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

@validar_numeros
def subt(a, b):
    """Retorna a subtração de dois números."""
    return a - b

@validar_numeros
def mult(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

@validar_numeros
def div(a, b):
    """Retorna a divisão de dois números."""
    return a / b

if __name__ == "__main__":
    print("Soma 2 + 3:", soma(2, 3))
    print("Subtração 5 - 2:", subt(5, 2))
    print("Multiplicação 4 * 3:", mult(4, 3))
    print("Divisão 10 / 2:", div(10, 2))
    try:
        soma(2, "a")
    except TypeError as e:
        print("Erro esperado:", e)
