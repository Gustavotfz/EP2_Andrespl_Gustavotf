#IMPORTS
import random
###################################

def cria_mapa(n):
    l = []
    l2 = []

    for x in range(n):
        l2.append(' ')
    
    for x in range(n):
        l.append(l2)
    
    return l

##################################

def posicao_suporta(mapa,b,l,c,o):
    if mapa[l][c] == ' ':
        if o == 'v':
            for x in range(b):
                if l + x >= (len(mapa)):
                    return False
                elif mapa[l+x][c] == ' ':
                    continue
                else:
                    return False
        else:
            for x in range(b):
                if c + x >= len(mapa[l]):
                    return False
                elif mapa[l][c+x] == ' ':
                    continue
                else:
                    return False
    else:
        return False
    
    return True

#########################################

def aloca_navios (mapa, blocos):
    pecas = 0
    while pecas < len(blocos):
        linha = random.randint(0, len(mapa)-1)
        coluna = random.randint(0, len(mapa)-1)
        orientacao = random.choice(['h', 'v'])
        if posicao_suporta(mapa,blocos[pecas],linha,coluna,orientacao):
            for i in range(blocos[pecas]):
                if orientacao == "v":
                    mapa[linha+i][coluna] = "N"
                elif orientacao == "h":
                    mapa[linha][coluna+i] = "N"
            pecas += 1
    return mapa

##########################################################################