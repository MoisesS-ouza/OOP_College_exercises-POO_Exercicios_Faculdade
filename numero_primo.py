def numero_primo(n):
    if n == 0:
        return 'Não é primo!'
    elif n == 1:
        return 'Não é primo!'
    elif n == 2:
        return 'É primo!'
    
    for num in range(2, n):
        if n % num == 0:
            return 'Não é primo!'
    
    return 'É primo!'

        
    
entrada = int(input())
print(numero_primo(entrada))