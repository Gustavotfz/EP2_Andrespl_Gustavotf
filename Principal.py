import random

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
    
    break
    

