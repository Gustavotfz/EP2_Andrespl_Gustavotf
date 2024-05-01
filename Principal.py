#IMPORTS
from Constantes import *
from Funcoes import *

##########################################################################

game_status = True

while game_status:
    titulo = u"\u001b[36;1m =====================================\n|                                     |\n| Bem-vindo ao INSPER - Batalha Naval |\n|                                     |\n =======   xxxxxxxxxxxxxxxxx   ======= \n"
    msg_inicial = u"\u001b[33;1m\u001b[1mIniciando o Jogo!\n"
    print (titulo, CORES["reset"])
    print(msg_inicial, CORES["reset"]) 
    pais_computador = random.choice(list(PAISES.keys()))
    print("\u001b[35;1mComputador está alocando os navios de batalhado país","\u001b[37;1m"+pais_computador+"...")
    print("\u001b[35;1mComputador já está em posição de batalha!\n",CORES["reset"])

    for x in NUMERO_PAISES:
        a = str(x) + ': ' + NUMERO_PAISES[x]
        print(a)
        z = NUMERO_PAISES[x]
        for y in PAISES[z]:
            b = '   ' + str(PAISES[z][y]) + ': ' + y
            print(b)
    
    escolha_pais = int(input("Qual o número da nação da sua frota? "))
    while escolha_pais not in [i for i in range(1,6)]:
        print("Opção inválida")
        escolha_pais = int(input("Qual o número da nação da sua frota? "))

    mapa_computador = cria_mapa(10)
    mapa_jogador = cria_mapa(10)

    lista_blocos = []
    for navio in PAISES[pais_computador]:
        for i in range(PAISES[pais_computador][navio]):
            lista_blocos.append(CONFIGURACAO[navio])
    mapa_computador = aloca_navios(mapa_computador, lista_blocos)
    c = cria_mapa(10)
    j = mapa_jogador

    framework = (f"""         COMPUTADOR - {pais_computador}                      JOGADOR - {NUMERO_PAISES[escolha_pais]}
      A  B  C  D  E  F  G  H  I  J            A  B  C  D  E  F  G  H  I  J
  1  {c[0][0]}{c[0][1]}{c[0][2]}{c[0][3]}{c[0][4]}{c[0][5]}{c[0][6]}{c[0][7]}{c[0][8]}{c[0][9]}  1    1  {j[0][0]}{j[0][1]}{j[0][2]}{j[0][3]}{j[0][4]}{j[0][5]}{j[0][6]}{j[0][7]}{j[0][8]}{j[0][9]}  1
  2  {c[1][0]}{c[1][1]}{c[1][2]}{c[1][3]}{c[1][4]}{c[1][5]}{c[1][6]}{c[1][7]}{c[1][8]}{c[1][9]}  2    2  {j[1][0]}{j[1][1]}{j[1][2]}{j[1][3]}{j[1][4]}{j[1][5]}{j[1][6]}{j[1][7]}{j[1][8]}{j[1][9]}  2
  3  {c[2][0]}{c[2][1]}{c[2][2]}{c[2][3]}{c[2][4]}{c[2][5]}{c[2][6]}{c[2][7]}{c[2][8]}{c[2][9]}  3    3  {j[2][0]}{j[2][1]}{j[2][2]}{j[2][3]}{j[2][4]}{j[2][5]}{j[2][6]}{j[2][7]}{j[2][8]}{j[2][9]}  3
  4  {c[3][0]}{c[3][1]}{c[3][2]}{c[3][3]}{c[3][4]}{c[3][5]}{c[3][6]}{c[3][7]}{c[3][8]}{c[3][9]}  4    4  {j[3][0]}{j[3][1]}{j[3][2]}{j[3][3]}{j[3][4]}{j[3][5]}{j[3][6]}{j[3][7]}{j[3][8]}{j[3][9]}  4
  5  {c[4][0]}{c[4][1]}{c[4][2]}{c[4][3]}{c[4][4]}{c[4][5]}{c[4][6]}{c[4][7]}{c[4][8]}{c[4][9]}  5    5  {j[4][0]}{j[4][1]}{j[4][2]}{j[4][3]}{j[4][4]}{j[4][5]}{j[4][6]}{j[4][7]}{j[4][8]}{j[4][9]}  5
  6  {c[5][0]}{c[5][1]}{c[5][2]}{c[5][3]}{c[5][4]}{c[5][5]}{c[5][6]}{c[5][7]}{c[5][8]}{c[5][9]}  6    6  {j[5][0]}{j[5][1]}{j[5][2]}{j[5][3]}{j[5][4]}{j[5][5]}{j[5][6]}{j[5][7]}{j[5][8]}{j[5][9]}  6
  7  {c[6][0]}{c[6][1]}{c[6][2]}{c[6][3]}{c[6][4]}{c[6][5]}{c[6][6]}{c[6][7]}{c[6][8]}{c[6][9]}  7    7  {j[6][0]}{j[6][1]}{j[6][2]}{j[6][3]}{j[6][4]}{j[6][5]}{j[6][6]}{j[6][7]}{j[6][8]}{j[6][9]}  7
  8  {c[7][0]}{c[7][1]}{c[7][2]}{c[7][3]}{c[7][4]}{c[7][5]}{c[7][6]}{c[7][7]}{c[7][8]}{c[7][9]}  8    8  {j[7][0]}{j[7][1]}{j[7][2]}{j[7][3]}{j[7][4]}{j[7][5]}{j[7][6]}{j[7][7]}{j[7][8]}{j[7][9]}  8
  9  {c[8][0]}{c[8][1]}{c[8][2]}{c[8][3]}{c[8][4]}{c[8][5]}{c[8][6]}{c[8][7]}{c[8][8]}{c[8][9]}  9    9  {j[8][0]}{j[8][1]}{j[8][2]}{j[8][3]}{j[8][4]}{j[8][5]}{j[8][6]}{j[8][7]}{j[8][8]}{j[7][9]}  9
 10  {c[9][0]}{c[9][1]}{c[9][2]}{c[9][3]}{c[9][4]}{c[9][5]}{c[9][6]}{c[9][7]}{c[9][8]}{c[9][9]}  10  10  {j[9][0]}{j[9][1]}{j[9][2]}{j[9][3]}{j[9][4]}{j[9][5]}{j[9][6]}{j[9][7]}{j[9][8]}{j[8][9]}  10
      A  B  C  D  E  F  G  H  I  J            A  B  C  D  E  F  G  H  I  J

""")
    print(framework)
    
    lista_navios = []
    for x in PAISES[NUMERO_PAISES[escolha_pais]]:
        for y in range(PAISES[NUMERO_PAISES[escolha_pais]][x]):
            lista_navios.append(x)
                               
    for x in PAISES[NUMERO_PAISES[escolha_pais]]:
        lista_navios.remove(x)
        print('alocar: ' + x + '(' + str(CONFIGURACAO[x]) + ' blocos)')
        print('próximos:' + str(lista_navios))

        escolha_letra = input('\nInforme uma letra: ')
        escolha_letra = escolha_letra.upper()
        while escolha_letra not in ALFABETO:
            print('Letra inválida')
            escolha_letra = input('Informe uma letra: ')
            escolha_letra = escolha_letra.upper()

        escolha_linha = input('Informe a linha: ')
        while escolha_linha not in NUMEROS:
            print('Linha inválida')
            escolha_linha = input('Informe a linha: ')
            

        escolha_orientacao = input('Informe a orientação [h|v]: ')

        if posicao_suporta(j,CONFIGURACAO[x],escolha_linha,escolha_letra,escolha_orientacao):
            j = posiciona_navios(j,CONFIGURACAO[x],escolha_linha,escolha_letra,escolha_orientacao)
            print('Navio alocado!')
            print(j)