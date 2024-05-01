# quantidade de blocos por modelo de navio
CONFIGURACAO = {
    'Destroyer': 3,
    'Porta-aviões': 5,
    'Submarino': 2,
    'Torpedeiro': 3,
    'Cruzador': 2,
    'Couraçado': 4
}

# frotas de cada pais
PAISES =  {
    'Brasil': {
        'Cruzador': 1,
        'Torpedeiro': 2,
        'Destroyer': 1,
        'Couraçado': 1,
        'Porta-aviões': 1
    }, 
    'França': {
        'Cruzador': 3, 
        'Porta-aviões': 1, 
        'Destroyer': 1, 
        'Submarino': 1, 
        'Couraçado': 1
    },
    'Austrália': {
        'Couraçado': 1,
        'Cruzador': 3, 
        'Submarino': 1,
        'Porta-aviões': 1, 
        'Torpedeiro': 1
    },
    'Rússia': {
        'Cruzador': 1,
        'Porta-aviões': 1,
        'Couraçado': 2,
        'Destroyer': 1,
        'Submarino': 1
    },
    'Japão': {
        'Torpedeiro': 2,
        'Cruzador': 1,
        'Destroyer': 2,
        'Couraçado': 1,
        'Submarino': 1
    }
}

# alfabeto para montar o nome das colunas
ALFABETO = ["A","B","C","D","E","F","G","H","I","J"]
NUMEROS = ['1','2','3','4','5','6','7','8','9','10']

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
    'white': '\u001b[37m',
    'bold': '\u001b[1m',
    'underline': '\u001b[4m',
    'reversed': '\u001b[7m'
}

# Relação para o Entre índice e o nome dos países
NUMERO_PAISES = {1: 'Brasil', 2: 'França', 3: 'Austrália', 4: 'Rússia', 5: 'Japão'}
LETRAS_NUMEROS = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7, "I": 8, "J": 9}

separador = "\n================================================================================================="