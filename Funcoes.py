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