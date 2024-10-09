# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
def sequencia_fibonacci(limite):
    sequencia = [0, 1]
    while sequencia[-1] < limite:
        proximo_fib = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo_fib)
    return sequencia

def checa(num):
    sequencia = sequencia_fibonacci(num)

    if num in sequencia:
        return True
    else:
        return False
    
num = int(input("Digite um número, para que o código veja se ele pertence a sequência: "))
resultado = checa(num)
print(f"O número {num} {'pertence' if resultado else 'não pertence'} a sequência de Fibonacci.")