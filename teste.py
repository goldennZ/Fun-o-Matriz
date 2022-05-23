#--------------------------------------------------------------------------------------------------------------------------------
#-- CARREGAR A MATRIZ
#--------------------------------------------------------------------------------------------------------------------------------
def carregaMatriz(nomeArq):
    arq = open(nomeArq, "r")
    qtdLins = int(arq.readline())

    ret = []
    for lin in range(qtdLins):
        texto = arq.readline().split()

        linha = []
        for col in range(qtdLins + 1):
            linha.append(float(texto[col]))

        ret.append(linha)

    arq.close()
    return ret

OriginalMatriz = carregaMatriz("sistema.txt")
#--------------------------------------------------------------------------------------------------------------------------------
#-- DIVISAO
#--------------------------------------------------------------------------------------------------------------------------------
def divisao(a, b):
    if a == 0 and b == 0:
        return "indeterminado"
    elif b == 0:
        return "infinito"
    else:
        return a/b
#--------------------------------------------------------------------------------------------------------------------------------
#-- DIVIDIR UM VETOR POR OUTRO
#--------------------------------------------------------------------------------------------------------------------------------
def divDumVetorPorOutro(m, x, y):
    ret = []
    for i in range(len(m[x])-1):
        ret.append(divisao(m[x][i], m[y][i]))
#--------------------------------------------------------------------------------------------------------------------------------
#-- PERMUTA
#--------------------------------------------------------------------------------------------------------------------------------
def permuta(linha, perm, perms):
    if linha == []:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin]+linha[lin+1:len(linha)],
                    perm+[linha[lin]], perms)
#--------------------------------------------------------------------------------------------------------------------------------
def permutacoes(linha):
    perms = []
    permuta(linha, [], perms)
    return perms
#--------------------------------------------------------------------------------------------------------------------------------
#-- ZERO NA DIAGONAL
#--------------------------------------------------------------------------------------------------------------------------------
def haZeroNaDiagonal(m):
    qtdDeZeros = 0
    posicao = 0
    while posicao < len(m):
        if m[posicao][posicao] == 0:
            qtdDeZeros += 1
        posicao += 1
    return qtdDeZeros > 0
#--------------------------------------------------------------------------------------------------------------------------------
#-- COLOCAR UM NA DIAGONAL PRINCIPAL NA LINHA
#--------------------------------------------------------------------------------------------------------------------------------
def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    divisor = m[lin][lin]
    col = 0
    while col <= len(m):
        m[lin][col] /= divisor
        col += 1
#--------------------------------------------------------------------------------------------------------------------------------
#-- MULTIPLICAR AS LINHAS
#--------------------------------------------------------------------------------------------------------------------------------
def multilinha(m, lin, col):

    constante = m[lin][col]

    for colI in range(len(m[col])):
        m[lin][colI] - m[lin][colI] + (m[col][colI]*constante)
#--------------------------------------------------------------------------------------------------------------------------------
#-- PROGRAMA RESULTADO
#--------------------------------------------------------------------------------------------------------------------------------
def program(P):
    var = 0
    while var < len(P):
        matriz = P[var]

        while haZeroNaDiagonal(matriz):
            var += 1
            matriz = P[var]
        linhas = len(matriz)

        for l in range(linhas):
            for j in range(linhas):
                if l != j:
                    divDumVetorPorOutro(matriz, l, j)

        for x in range(linhas):
            poeUmNaDiagonalPrincipalNaLinha(x, matriz)

            for y in range(linhas):
                if x != y:
                    multilinha(matriz, x, y)
                    while haZeroNaDiagonal(matriz):
                        var += 1
                        matriz = OriginalMatriz[var]
        break

    variables = ["X","Y","Z"]
    variables2 = 0

    for var2 in range(linhas):
        print(f"{variables[variables2]} vale: {matriz[var2][linhas]}")
        variables2 += 1
#--------------------------------------------------------------------------------------------------------------------------------
#-- START
#--------------------------------------------------------------------------------------------------------------------------------
program(permutacoes(OriginalMatriz))
