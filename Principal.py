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
    while escolha_pais not in [str(numero) for numero in range(1,6)]:
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

    navios_alocar = lista_navios                
    for n_navio in range(len(lista_navios)):
        navio_alocando = lista_navios[0]
        print(CORES["bold"]+CORES["yellow"]+'ALOCAR: '+CORES["reset"], CORES["cyan"] + lista_navios[0], CORES["reset"] + '(' + CORES["underline"] + str(CONFIGURACAO[lista_navios[0]]) +  ' blocos' + CORES["reset"] + ")")
        navios_alocar.remove(navios_alocar[0])
        navios_disponiveis = ", ".join(navios_alocar)
        if navios_alocar != []:
            print(CORES["bold"]+CORES["yellow"]+'PRÓXIMOS: '+CORES["reset"], navios_disponiveis)

        suporta = False
        while suporta == False:
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
                escolha_orientacao = (input(CORES["yellow"] + 'Informe a orientação ' + CORES["bold"] + CORES["underline"] + '[h|v]' + CORES["reset"] + CORES["yellow"] + ': ' + CORES["reset"])).upper()

            if posicao_suporta(jogador,CONFIGURACAO[navio_alocando],int(escolha_linha),LETRAS_NUMEROS[escolha_letra],escolha_orientacao):
                jogador = posiciona_navios(jogador,CONFIGURACAO[navio_alocando],int(escolha_linha)-1,LETRAS_NUMEROS[escolha_letra],escolha_orientacao)
                if lista_navios != []:
                    print(CORES["green"] + CORES["bold"] + 'Navio alocado!' + CORES["reset"])
                else:
                    print(CORES["green"] + CORES["bold"] + 'Todos os navios foram alocados!' + CORES["reset"])
                framework = gera_framework(computador, jogador, pais_computador, escolha_pais)
                print(framework)
                suporta = True
            else:
                print('Não foi possível alocar navio em ' + escolha_letra + str(escolha_linha) + escolha_orientacao + ' !')
        
    print(CORES["cyan"] + CORES["underline"] + "Iniciando a " + CORES["bold"] + "Batalha Naval\n" + CORES["reset"])
  
    time.sleep(0.5)
    for numero in range(1,6):
        time.sleep(0.5)
        print(6 - numero)
    

    rodada = True
    while rodada:
        print('Coordenadas do seu disparo')

        tiro_autorizado = False
        while tiro_autorizado == False:
            letra_disparo = (input(CORES["yellow"] + 'Letra: ' + CORES["reset"])).upper()
            while letra_disparo not in ALFABETO:
                print(CORES["red"] + 'Letra inválida' + CORES["reset"])
                letra_disparo = (input(CORES["yellow"] + 'Letra: ' + CORES["reset"])).upper()
            numero_da_letra_disparo = LETRAS_NUMEROS[letra_disparo]

            linha_disparo = input('Linha: ')
            while linha_disparo not in NUMEROS:
                print(CORES["red"] + 'Linha inválida' + CORES["reset"])
                linha_disparo = (input(CORES["yellow"] + 'Linha: ' + CORES["reset"])).upper()

            if computador[int(linha_disparo)-1][numero_da_letra_disparo] == (CORES["blue"] + "▓▓▓" + CORES["reset"]) or mapa_computador[int(linha_disparo)-1][numero_da_letra_disparo] == (CORES["red"] + "▓▓▓" + CORES["reset"]):#
                print ('Posição ' + letra_disparo + str(linha_disparo) + ' já bombardeada!')
            else:
                tiro_autorizado = True

        tiro_computador_autorizado = False
        while tiro_computador_autorizado == False:
            letra_disparo_computador = random.choice(ALFABETO)
            letra_disparo_computador = letra_disparo_computador.upper()
            numero_da_letra_disparo_computador = LETRAS_NUMEROS[letra_disparo_computador]
            linha_disparo_computador = random.choice(NUMEROS)
            if jogador[int(linha_disparo_computador)-1][numero_da_letra_disparo_computador] == (CORES["red"] + "▓▓▓" + CORES["reset"]) or jogador[int(linha_disparo_computador)-1][numero_da_letra_disparo_computador] == (CORES["blue"] + "▓▓▓" + CORES["reset"]):
                continue
            else:
                tiro_computador_autorizado = True
                
        if mapa_computador[int(linha_disparo)-1][numero_da_letra_disparo] == (CORES["green"] + "▓▓▓" + CORES["reset"]): #NAVIO COMPUTADOR ATINGIDO / JOGADOR ATIRANDO
            print('Jogador ' + arma + '  ' + letra_disparo+linha_disparo + '     BOOOOMMMMM!!!!')
            mapa_computador[int(linha_disparo)-1][numero_da_letra_disparo] = CORES["red"] + "▓▓▓" + CORES["reset"]
            computador[int(linha_disparo)-1][numero_da_letra_disparo] = CORES["red"] + "▓▓▓" + CORES["reset"]
            framework = gera_framework(computador, jogador, pais_computador, escolha_pais)
        else:
            print('Jogador ' + arma + '  ' + letra_disparo +  linha_disparo + '     Água!')
            #print('Jogador ------>>>>>>>   ' + letra_disparo+linha_disparo + '     Água!')
            computador[int(linha_disparo)-1][numero_da_letra_disparo] = CORES["blue"] + "▓▓▓" + CORES["reset"]
            framework = gera_framework(computador, jogador, pais_computador, escolha_pais)

        if jogador[int(linha_disparo_computador)-1][numero_da_letra_disparo_computador] == (CORES["green"] + "▓▓▓" + CORES["reset"]): #NAVIO JOGADOR ATINGIDO / COMPUTADOR ATIRANDO
            print('Computador ' + arma + '  ' + letra_disparo_computador+linha_disparo_computador + '     BOOOOMMMMM!!!!')
            jogador[int(linha_disparo_computador)-1][numero_da_letra_disparo_computador] = CORES["red"] + "▓▓▓" + CORES["reset"]
            framework = gera_framework(computador, jogador, pais_computador, escolha_pais)
        else:
            print('Computador ' + arma + '  ' + letra_disparo_computador+linha_disparo_computador + '     Água!')
            jogador[int(linha_disparo_computador)-1][numero_da_letra_disparo_computador] = CORES["blue"] + "▓▓▓" + CORES["reset"]
            framework = gera_framework(computador, jogador, pais_computador, escolha_pais)

        print(framework)

        vitoria = foi_derrotado(mapa_computador)
        if vitoria == True:
            print('Você venceu!')
            print(pirata_da_vitoria)
            rodada = False

        derrota = foi_derrotado(jogador)
        if derrota == True:
            print('Você perdeu!')
            print(cara_triste_de_derrota)
            print('Pena, mais sorte da próxima vez!')
            rodada = False

    jogar_novamente = input('Jogar novamente? [s|n] ')
    jogar = True
    while jogar:
        jogar_novamente = jogar_novamente.lower()
        if jogar_novamente == 's' or jogar_novamente == 'n':
            if jogar_novamente == 'n':
                print('Até a próxima!')
                game_status = False
                jogar = False
            elif jogar_novamente == 's':
                print('Que bom!')
                print('Bom divertimento!')
                jogar = False
        else:
            print('Resposta inválida')
            jogar_novamente = input('Jogar novamente? [s|n] ')