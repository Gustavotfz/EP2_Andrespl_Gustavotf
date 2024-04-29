#IMPORTS
import random
##########################################################################

def cria_mapa(n):
    return [[" " for a in range(n)] for b in range(n)] 

##########################################################################

def posicao_suporta(mapa,blocos,linha,coluna,orientacao):
    if (orientacao == "h" and (coluna + blocos)>len(mapa)) or (orientacao == "v" and (linha + blocos)>len(mapa)) or (linha > len(mapa)-1) or (coluna > len(mapa)-1): 
        return False
    for i in range(blocos):
        if orientacao == "v":
            if (mapa[linha+i][coluna] != " " ):
                return False
        elif orientacao == "h":
            if (mapa[linha][coluna+i] != " "):
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
                    mapa[linha+i][coluna] = "N"
                elif orientacao == "h":
                    mapa[linha][coluna+i] = "N"
            pecas += 1
    return mapa

##########################################################################

def foi_derrotado (matriz):
    for linha in matriz:
        for item in linha:
            if item == "N":
                return False
    return True

##########################################################################

# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'destroyer': 3,
    'porta-avioes': 5,
    'submarino': 2,
    'torpedeiro': 3,
    'cruzador': 2,
    'couracado': 4
}

# frotas de cada pais
PAISES =  {
    'Brasil': {
        'cruzador': 1,
        'torpedeiro': 2,
        'destroyer': 1,
        'couracado': 1,
        'porta-avioes': 1
    }, 
    'França': {
        'cruzador': 3, 
        'porta-avioes': 1, 
        'destroyer': 1, 
        'submarino': 1, 
        'couracado': 1
    },
    'Austrália': {
        'couracado': 1,
        'cruzador': 3, 
        'submarino': 1,
        'porta-avioes': 1, 
        'torpedeiro': 1
    },
    'Rússia': {
        'cruzador': 1,
        'porta-avioes': 1,
        'couracado': 2,
        'destroyer': 1,
        'submarino': 1
    },
    'Japão': {
        'torpedeiro': 2,
        'cruzador': 1,
        'destroyer': 2,
        'couracado': 1,
        'submarino': 1
    }
}

NUMERO_PAISES = {1: 'Brasil', 2: 'França', 3: 'Austrália', 4: 'Rússia', 5: 'Japão'}

# alfabeto para montar o nome das colunas
ALFABETO = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# cores para o terminal
CORES = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'black': '\u001b[30m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'white': '\u001b[37m'
}

##########################################################################

game_status = True

while game_status:
    titulo = " =====================================\n|                                     |\n| Bem-vindo ao INSPER - Batalha Naval |\n|                                     |\n =======   xxxxxxxxxxxxxxxxx   ======= \n"
    msg_inicial = "Iniciando o Jogo!"
    print(titulo)
    print(msg_inicial)
    pais_computador = random.choice(list(PAISES.keys()))
    print("Computador está alocando os navios de batalhado país",pais_computador+"...")
    print("Computador já está em posição de batalha!")

    for x in NUMERO_PAISES:
        a = str(x) + ': ' + NUMERO_PAISES[x]
        print(a)
        z = NUMERO_PAISES[x]
        for y in PAISES[z]:
            b = '   ' + str(PAISES[z][y]) + ': ' + y
            print(b)
    
    escolha_pais = int(input('Qual número da nação da sua frota?'))

    mapa_computador = cria_mapa(10)
    mapa_jogador = cria_mapa(10)
    lista_blocos = []
    for navio in PAISES[pais_computador]:
        for i in range(PAISES[pais_computador][navio]):
            lista_blocos.append(CONFIGURACAO[navio])
    mapa_computador = aloca_navios(mapa_computador, lista_blocos)
    for linha in mapa_computador:
        print(linha)
    break
    