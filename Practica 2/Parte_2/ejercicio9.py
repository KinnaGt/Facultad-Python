def crearListaCarac(l):
    '''Crear lista de caracteres a partir de strings en una lista'''
    for elem in range(len(l)):
        l[elem] = list(l[elem])


def buscarMinas(l):
    crearListaCarac(l)
    for elem in range(len(l)):
        for elem2 in range(len(l[elem])):
            cont = 0
            if elem2 != 0:
                if l[elem][elem2-1] in '*':
                    cont += 1
            if elem2 < len(l[elem])-1:
                if l[elem][elem2+1] in '*':
                    cont += 1
            if elem != 0:
                if l[elem-1][elem2] in '*':
                    cont += 1
                if elem2 != 0:
                    if l[elem-1][elem2-1] in '*':
                        cont += 1
                if elem2 < len(l[elem])-1:
                    if l[elem-1][elem2+1] in '*':
                        cont += 1
            if elem < len(l)-1:
                if l[elem+1][elem2] in '*':
                    cont += 1
                if elem2 < len(l[elem])-1:
                    if l[elem+1][elem2+1] in '*':
                        cont += 1
                    if elem2 != 0:
                        if l[elem+1][elem2-1] in '*':
                            cont += 1
            l[elem][elem2] = l[elem][elem2].replace('-', f'{cont}')
    print(l)


l = [
    '-*-*-',
    '--*--',
    '----*',
    '*----',
    '---*-'
]

buscarMinas(l)
