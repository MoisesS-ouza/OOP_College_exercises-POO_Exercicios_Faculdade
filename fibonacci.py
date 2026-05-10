def fibonacci(n):
    a = 0
    b = 1
    
    for i in range(n):
        if i == n - 1:
            print(a, end= ' ')
            valor_a = a
            a = b
            b = valor_a + b
        else:
            print(a, end=', ')
            valor_a = a
            a = b
            b = valor_a + b
        
numero = int(input())
fibonacci(numero)