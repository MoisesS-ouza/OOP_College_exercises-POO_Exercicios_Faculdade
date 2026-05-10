def numero_primo(n):
    if n == 0:
        print('Não é primo!')
        return False
    elif n == 1:
        print('Não é primo!')
        return False
    elif n == 2:
        print('É primo!')
        return True
    
    for num in range(2, n):
        if n % num == 0:
            return False
    
    return True
    
entrada = int(input())

if entrada == 0:
    print(f'O próximo número primo é: 2')

else:
    entrada+= 1
    while not numero_primo(entrada):
        entrada+= 1
        numero_primo(entrada)
    
    print(f'O próximo número primo é: {entrada}')