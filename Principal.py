#IMPORTS
from Funcoes import *
from Constantes import *
import time
import random
##########################################################################

game_status = True

while game_status:
    titulo = CORES["cyan"] + " =====================================\n|                                     |\n| Bem-vindo ao INSPER - Batalha Naval |\n|                                     |\n =======   xxxxxxxxxxxxxxxxx   ======= \n"
    msg_inicial = CORES["bold"] + CORES["yellow"] + "Iniciando o Jogo!\n"
    print (titulo + CORES["reset"])
    print(msg_inicial + CORES["reset"]) 
    pais_computador = random.choice(list(PAISES.keys()))
    print(CORES["magenta"] + "Computador está alocando os navios de batalhado país", CORES["bold"]+CORES["underline"]+CORES["red"] + pais_computador + CORES["reset"] + CORES["magenta"] + " ..." + CORES["reset"])
    print(CORES["magenta"] + "Computador já está em posição de batalha!\n" + CORES["reset"])

    for Numero in NUMERO_PAISES:
        Numero_Pais = CORES["bold"] + str(Numero) + ': ' + CORES["cyan"] + CORES["underline"] + NUMERO_PAISES[Numero] + CORES["reset"]
        print(Numero_Pais)
        pais = NUMERO_PAISES[Numero]
        for navio in PAISES[pais]:
            quantidade_navio = '   ' +  str(PAISES[pais][navio]) + ': ' + CORES["blue"] + navio + CORES["reset"]
            print(quantidade_navio)
    
    escolha_pais = input(CORES["bold"] + CORES["yellow"] + "\nQual o número da nação da sua frota? " + CORES["reset"])
    while int(escolha_pais) not in [numero for numero in range(1,6)]:
        print(CORES["red"] + "Opção inválida" + CORES["reset"])
        escolha_pais = input(CORES["bold"] + CORES["yellow"] + "\nQual o número da nação da sua frota? " + CORES["reset"])
    escolha_pais = int(escolha_pais)

    print(separador)

    mapa_computador = cria_mapa(10)
    mapa_jogador = cria_mapa(10)

    lista_blocos = []
    for navio in PAISES[pais_computador]:
        for numero_navio in range(PAISES[pais_computador][navio]):
            lista_blocos.append(CONFIGURACAO[navio])
    mapa_computador = aloca_navios(mapa_computador, lista_blocos)
    computador = cria_mapa(10)
    jogador = mapa_jogador

    framework = gera_framework(computador, jogador, pais_computador, escolha_pais)
    print(framework)
    
    lista_navios = []
    for navio in PAISES[NUMERO_PAISES[escolha_pais]]:
        for numero_navio in range(PAISES[NUMERO_PAISES[escolha_pais]][navio]):
            lista_navios.append(navio)
                               
    for navio in lista_navios:
        lista_navios.remove(navio)
        print(CORES["bold"]+CORES["yellow"]+'ALOCAR:'+CORES["reset"], CORES["cyan"] + navio, CORES["reset"] + '(' + CORES["underline"] + str(CONFIGURACAO[navio]) +  ' blocos' + CORES["reset"] + ")")
        navios_disponiveis = ", ".join(lista_navios)
        print(CORES["bold"]+CORES["yellow"]+'PRÓXIMOS:'+CORES["reset"], navios_disponiveis)

        escolha_letra = (input(CORES["yellow"] + '\nInforme uma letra: ' + CORES["reset"])).upper()
        while escolha_letra not in ALFABETO:
            print(CORES["red"] + 'Letra inválida' + CORES["reset"])
            escolha_letra = (input(CORES["yellow"] + '\nInforme uma letra: ' + CORES["reset"])).upper()

        escolha_linha = input(CORES["yellow"] + 'Informe a linha: ' + CORES["reset"])
        while escolha_linha not in NUMEROS:
            print(CORES["red"] + 'Linha inválida' + CORES["reset"])
            escolha_linha = input(CORES["yellow"] + 'Informe a linha: ' + CORES["reset"])
        escolha_linha = int(escolha_linha)
            
        escolha_orientacao = (input(CORES["yellow"] + 'Informe a orientação ' + CORES["bold"] + CORES["underline"] + '[h|v]' + CORES["reset"] + CORES["yellow"] + ': ' + CORES["reset"])).upper()
        while escolha_orientacao not in ["H","V"]:
            print(CORES["red"] + 'Orientação inválida' + CORES["reset"])
            escolha_linha = (input(CORES["yellow"] + 'Informe a orientação ' + CORES["bold"] + CORES["underline"] + '[h|v]' + CORES["reset"] + CORES["yellow"] + ': ' + CORES["reset"])).upper()

        if posicao_suporta(jogador,CONFIGURACAO[navio],int(escolha_linha),LETRAS_NUMEROS[escolha_letra],escolha_orientacao):
            jogador = posiciona_navios(jogador,CONFIGURACAO[navio],int(escolha_linha)-1,LETRAS_NUMEROS[escolha_letra],escolha_orientacao)
            if lista_navios != []:
                print(CORES["green"] + CORES["bold"] + 'Navio alocado!' + CORES["reset"])
            else:
                print(CORES["green"] + CORES["bold"] + 'Todos os navios foram alocados!' + CORES["reset"])
            framework = gera_framework(computador, jogador, pais_computador, escolha_pais)
            print(framework)
        
    print(CORES["cyan"] + CORES["underline"] + "Iniciando a " + CORES["bold"] + "Batalha Naval\n" + CORES["reset"])
  
    time.sleep(0.5)
    for numero in range(1,6):
        time.sleep(0.5)
        print(6 - numero)
    
    while '?': #DUVIDA
        print('Coordenadas do seu disparo')
        letra_disparo = input('Letra: ')
        linha_disparo = input('Linha: ')

        letra_disparo_computador = random.choice(ALFABETO)
        linha_disparo_computador = random.choice(NUMEROS)

        if '?': #NAVIO COMPUTADOR ATINGIDO #DUVIDA 
            print('Jogador ------>>>>>>>   ' + letra_disparo+linha_disparo + '     BOOOOMMMMM!!!!')

        else:
            print('Jogador ------>>>>>>>   ' + letra_disparo+linha_disparo + '     Água!')

        if jogador[linha_disparo_computador][letra_disparo_computador] == "▓▓▓": #NAVIO JOGADOR ATINGIDO #DUVIDA
            print('Computador ------>>>>>>>   ' + letra_disparo_computador+linha_disparo_computador + '     BOOOOMMMMM!!!!')
            jogador[linha_disparo_computador][letra_disparo_computador] = CORES["red"] + "▓▓▓" + CORES["reset"]
            framework = gera_framework(computador, jogador, pais_computador, escolha_pais)
        else:
            print('Computador ------>>>>>>>   ' + letra_disparo_computador+linha_disparo_computador + '     Água!')

        print(framework)
                  
    print('Você venceu!')
    print('Já temos o futuro Jack Sparrow Jr!')

    jogar_novamente = input('Jogar novamente? [s|n] ')
    if jogar_novamente == 'n':
        game_status = False
        print('Até a próxima!')