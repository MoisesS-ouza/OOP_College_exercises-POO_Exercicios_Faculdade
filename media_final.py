def aprovado(m_final):
    print(f'FS, Aprovado, MF: {m_final}')

def reprovado(m_final):
    print(f'FS, Reprovado, MF: {m_final}')

p1 = float(input())
p2 = float(input())
tp = float(input())
me = float(input())

"""
Legenda:
p1 - Prova 1
p2 - Prova 2
tp - Trabalho prático
me - Média dos exercícios
"""

total_aulas = int(input())
presencas = int(input())

media_final = (p1 + p2) / 2 * 0.7 + me * 0.1 + tp * 0.2

frequencia = 'FS' if total_aulas * 3/4 <= presencas else 'FI'

verificacao_p1_p2 = True if p1 <= 10 and p2 <= 10 else False
verificacao_tp_me = True if tp <= 10 and me <= 10 else False
verificacao_media_final = True if media_final <= 10 else False

if verificacao_p1_p2 and verificacao_tp_me and verificacao_media_final:
    if 14 <= total_aulas <= 16 \
    and 0 <= presencas <= total_aulas:
    
        if media_final > 5.5 and frequencia == 'FS':
            aprovado(media_final)
    
        elif media_final < 5.5 and frequencia == 'FS':
            
            if 3.0 <= media_final <= 5.5 and frequencia == 'FS':
                recuperacao = float(input())
                media_final = (media_final + recuperacao)/ 2
                print(aprovado(media_final) if media_final > 5.5 else reprovado(media_final))
        
            else:
                reprovado(media_final)
                
        else:
            print('FI')
    else:
        print('entrada inválida')
else:
    print('entrada inválida')