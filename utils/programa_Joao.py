#--------------------------------------------------------------------------------------------------------------------------------
#-- CARREGAR A MATRIZ | PROFESSOR
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
#-- DIVISAO | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def divisao(a, b):
    if a == 0 and b == 0:
        return "indeterminado"
    elif b == 0:
        return "infinito"
    else:
        return a/b
#--------------------------------------------------------------------------------------------------------------------------------
def divDumVetorPorOutro (x,y):
    ret=[]
    for i in range(len(x)-1): ret.append(divisao(x[i],y[i]))
    return ret
#--------------------------------------------------------------------------------------------------------------------------------
#-- PERMUTA | PROFESSOR
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
#-- ZERO NA DIAGONAL | PROFESSOR
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
#-- MULTIPLICAR AS LINHAS
#--------------------------------------------------------------------------------------------------------------------------------
# def MultiplicarAsLinha(m, lin, col):

#     for coluna in range(len(m[col])):
#         m[lin][coluna] - m[lin][coluna] + (m[col][coluna]*m[lin][col])
#--------------------------------------------------------------------------------------------------------------------------------
#-- COLOCAR UM NA DIAGONAL PRINCIPAL NA LINHA | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def poeUmNaDiagonalPrincipalNaLinha(lin, m):
    divisor = m[lin][lin]
    col = 0
    while col <= len(m):
        m[lin][col] /= divisor
        col += 1
#--------------------------------------------------------------------------------------------------------------------------------
#-- PROGRAMA
#--------------------------------------------------------------------------------------------------------------------------------
def Programa(P):
    var = 0
    while var < len(P): #RECEBER A QUANTIDADE DE PERMUTACOES ADQUIRIDAS
        matriz = P[var] #PEGAR CADA PERMUTACAO

        while haZeroNaDiagonal(matriz): #CHECAR SE TEM ZERO NAS PERMUTAÇÕES
            var += 1
            matriz = P[var]

        linhas = len(matriz)

        for l in range(linhas):
            for m in range(linhas):
                divDumVetorPorOutro(matriz[l],matriz[m]) #DIVIDIR OS VETORES

            poeUmNaDiagonalPrincipalNaLinha(l,matriz) #COLOCAR UM NA DIAGONAL PRINCIPAL
            #print(matriz)
            for y in range(linhas):
                #MULTIPLICAR AS LINHAS
                for coluna in range(len(matriz[y])):
                    matriz[m][coluna] - matriz[m][coluna] + (matriz[y][coluna]*matriz[m][y])

                while haZeroNaDiagonal(matriz): #CHECAR SE TEM ZERO NA MATRIZ
                    var += 1
                    matriz = P[var]
        break

    letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    count = 0

    for col in range(linhas): #PRINTAR OS VALORES FINAIS
        print(f"{letters[count]} vale: {matriz[col][linhas]}")
        count += 1
#--------------------------------------------------------------------------------------------------------------------------------
#-- START
#--------------------------------------------------------------------------------------------------------------------------------
Programa(permutacoes(OriginalMatriz))