numeros = ''
contador_num_distintos = 0
num_distintos = ''

while True:
    entrada = input()

    if entrada == '-1':
        break
    
    numeros += entrada
    
    if f' {entrada} ' not in f' {num_distintos} ':
        num_distintos += f'{entrada} '
        contador_num_distintos += 1
    else:
        continue


print(int(contador_num_distintos))
print(num_distintos.strip())