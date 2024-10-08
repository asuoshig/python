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