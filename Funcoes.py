def cria_mapa(n):
    l = []
    l2 = []

    for x in range(n):
        l2.append(' ')
    
    for x in range(n):
        l.append(l2)
    
    return l