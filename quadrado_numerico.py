def quadrado_num(n):
    for i in range(1, n + 1):          
        for j in range(1, n + 1): 
            if j < i:
               print(i, end='')
            else:
                print(j, end='')
        print()
        

quadrado_num(6)
        
entrada = int(input())
quadrado_num(entrada)