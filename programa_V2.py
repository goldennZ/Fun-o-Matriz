table = []
#--------------------------------------------------------------------------------------------------------------------------------
#-- ALTERAR OS VALORES DAS LINHAS PARA TORNAR ZERO
#--------------------------------------------------------------------------------------------------------------------------------
def change_lines_value(m, t1, t2, v1, v2):
    valornegativo = -(m[t1][t2])
    col = 0
    while col <= len(m):
        value = m[v1][col] * valornegativo
        table.append(value)
        col += 1

    val = 0
    while val <= len(m):
        m[v2][val] += table[val]
        val += 1
#--------------------------------------------------------------------------------------------------------------------------------
#-- VERIFICAR SE TEM ZERO NA DIAGONAL | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def haZeroNaDiagonal(m):
    qtdDeZeros=0
    posicao=0
    while posicao<len(m):
        if m[posicao][posicao]==0: qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
#--------------------------------------------------------------------------------------------------------------------------------
#-- COLOCAR NUMERO UM NA DIAGONAL | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    divisor = m[lin][lin]
    col = 0
    while col <= len(m):
        m[lin][col] /= divisor
        col += 1
#--------------------------------------------------------------------------------------------------------------------------------
#-- ALTERAR AS ORDENS PARA TIRAR OS ZEROS DA DIAGONAL | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def comoSeLivrarDeZerosNaDiagonal(m):
    perms = permutacoes(list(range(len(m))))

    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(m, perms[i], perms[j]):
                return [perms[i], perms[j]]
    return None
#--------------------------------------------------------------------------------------------------------------------------------
#-- PEGAR A MATRIZ DO .TXT | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def divisao(a, b):
    if a == 0 and b == 0:
        return "indeterminado"
    elif b == 0:
        return "infinito"
    else:
        return a/b


def divDumVetorPorOutro(x, y):
    ret = []
    for i in range(len(x)-1):
        ret.append(divisao(x[i], y[i]))
    return ret


def paresDeLinhas(m):
    ret = []
    for lin in range(len(m)):
        for col in range(lin+1, len(m)):
            ret.append([lin, col])
    return ret
#--------------------------------------------------------------------------------------------------------------------------------
#-- FAZ A PERMUTACAO PARA ACHAR AS POSSIVEIS COMBINAÇÕES | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def permuta(linha, perm, perms):
    if linha == []:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin]+linha[lin+1:len(linha)],
                    perm+[linha[lin]], perms)

def permutacoes(linha):
    perms = []
    permuta(linha, [], perms)
    return perms
#--------------------------------------------------------------------------------------------------------------------------------
#-- PEGAR A MATRIZ DO .TXT | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def carregaMatriz(nomeArq):
    arq = open(nomeArq, "r")
    qtdLins = int(arq.readline())

    ret = []
    for lin in range(qtdLins):
        texto = arq.readline().split()

        linha = []
        for col in range(qtdLins+1):
            linha.append(float(texto[col]))

        ret.append(linha)

    arq.close()
    return ret
#--------------------------------------------------------------------------------------------------------------------------------
#-- PROGRAMA RESULT
#--------------------------------------------------------------------------------------------------------------------------------
matrizO = carregaMatriz("sistema.txt")
matrizPerm = permutacoes(matrizO)

var = 0
while var < len(matrizPerm):
    matriz = matrizPerm[var]

    while haZeroNaDiagonal(matriz):
        var += 1
        matriz = matrizPerm[var]

    linhas = len(matriz)
    
    for l in range(linhas):
        poeUmNaDiagonalPrincipalNaLinha(l,matriz)
        divDumVetorPorOutro(matriz[1],matriz[0])
        print(matriz)
    break







