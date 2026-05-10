num_pares = 0
num_impares = 0
maior_impar = 0

while True:
    entrada = int(input())
    nenhum = ', nenhum' if entrada == '' else ''
    
    if entrada < 0:
        break
    
    if entrada % 2 == 0:
        num_pares += 1
    else:
        num_impares += 1
    
    if entrada > maior_impar and entrada % 2 != 0:
        maior_impar = entrada
    
if maior_impar == 0:
    maior_impar = 'nenhum'
    
print(f'{num_pares}, {num_impares}, {maior_impar}')