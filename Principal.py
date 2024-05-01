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
            quantidade_navio = '   ' +  str(PAISES[pais][navio]) + ': ' + navio
            print(quantidade_navio)
    
    escolha_pais = int(input(CORES["bold"] + CORES["yellow"] + "\nQual o número da nação da sua frota?" + CORES["reset"]))
    while escolha_pais not in [numero for numero in range(1,6)]:
        print("Opção inválida")
        escolha_pais = int(input(CORES["bold"] + CORES["yellow"] + "\nQual o número da nação da sua frota?" + CORES["reset"]))

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
                               
    for navio in PAISES[NUMERO_PAISES[escolha_pais]]:
        lista_navios.remove(navio)
        print(CORES["bold"]+CORES["yellow"]+'ALOCAR:'+CORES["reset"], CORES["cyan"] + navio, CORES["reset"] + '(' + CORES["underline"] + str(CONFIGURACAO[navio]) +  ' blocos' + CORES["reset"] + ")")
        navios_disponiveis = ", ".join(lista_navios)
        print(CORES["bold"]+CORES["yellow"]+'PRÓXIMOS:'+CORES["reset"], navios_disponiveis)

        escolha_letra = (input('\nInforme uma letra: ')).upper()
        while escolha_letra not in ALFABETO:
            print('Letra inválida')
            escolha_letra = (input('\nInforme uma letra: ')).upper()

        escolha_linha = input('Informe a linha: ')
        while escolha_linha not in NUMEROS:
            print('Linha inválida')
            escolha_linha = input('Informe a linha: ')
            

        escolha_orientacao = (input('Informe a orientação [h|v]: ')).upper()
        while escolha_orientacao not in ["H","V"]:
            print('Orientação inválida')
            escolha_linha = (input('Informe a orientação [h|v]: ')).upper()

        if posicao_suporta(jogador,CONFIGURACAO[navio],int(escolha_linha),LETRAS_NUMEROS[escolha_letra],escolha_orientacao):
            jogador = posiciona_navios(jogador,CONFIGURACAO[navio],int(escolha_linha)-1,LETRAS_NUMEROS[escolha_letra],escolha_orientacao)
            print('Navio alocado!')
            framework = gera_framework(computador, jogador, pais_computador, escolha_pais)
            print(framework)