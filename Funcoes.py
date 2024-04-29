#IMPORTS
import random
##########################################################################

def cria_mapa(n):
    return [["   " for a in range(n)] for b in range(n)] 

##########################################################################

def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
    if (orientacao == "h" and (coluna + blocos)>len(mapa)) or (orientacao == "v" and (linha + blocos)>len(mapa)) or (linha > len(mapa)-1) or (coluna > len(mapa)-1): 
        return False
    for i in range(blocos):
        if orientacao == "v":
            if (mapa[linha+i][coluna] != "   " ):
                return False
        elif orientacao == "h":
            if (mapa[linha][coluna+i] != "   "):
                return False      
    return True

##########################################################################

def aloca_navios (mapa, blocos):
    pecas = 0
    while pecas < len(blocos):
        linha = random.randint(0, len(mapa)-1)
        coluna = random.randint(0, len(mapa)-1)
        orientacao = random.choice(['h', 'v'])
        if posicao_suporta(mapa,blocos[pecas],linha,coluna,orientacao):
            for i in range(blocos[pecas]):
                if orientacao == "v":
                    mapa[linha+i][coluna] = " N "
                elif orientacao == "h":
                    mapa[linha][coluna+i] = " N "
            pecas += 1
    return mapa

##########################################################################

def foi_derrotado (matriz):
    for linha in matriz:
        for item in linha:
            if item == " N ":
                return False
    return True

##########################################################################

def posiciona_navios (mapa, blocos, linha, coluna, orientacao):
    for i in range(blocos):
        if orientacao == "v":
            mapa[linha+i][coluna] = " N "
        else:
            mapa[linha][coluna+i] = " N "
    return mapa