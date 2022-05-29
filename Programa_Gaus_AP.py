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
#-- PERMUTA
#--------------------------------------------------------------------------------------------------------------------------------
def permuta(linha, perm, perms):
    if not linha:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin] + linha[lin + 1:len(linha)],
                    perm + [linha[lin]], perms)
#--------------------------------------------------------------------------------------------------------------------------------
#-- PERMUTACOES
#--------------------------------------------------------------------------------------------------------------------------------
def permutacoes(linha):
    perms = []
    permuta(linha, [], perms)
    return perms
#--------------------------------------------------------------------------------------------------------------------------------
#-- LISTA ORDENADA GENERICA
#--------------------------------------------------------------------------------------------------------------------------------
def listaOrdenadaGenerica(m):
    lista_linhas = []
    for pos in range(len(m)):
        lista_linhas.append(pos)
    return lista_linhas
#--------------------------------------------------------------------------------------------------------------------------------
#-- COMBINACOES DE LINHAS
#--------------------------------------------------------------------------------------------------------------------------------
def combinacoesLinhas(m):
    ret = []
    for lin in range(len(m)):
        for col in range(lin + 1, len(m)):
            ret.append([lin, col])
    return ret
#--------------------------------------------------------------------------------------------------------------------------------
#-- DIVISAO
#--------------------------------------------------------------------------------------------------------------------------------
def divisao(a, b):
    if a == 0 and b == 0:
        return "indeterminado"
    elif b == 0:
        return "infinito"
    else:
        return a / b
#--------------------------------------------------------------------------------------------------------------------------------
#-- DIVISAO DE UM VETOR POR OUTRO
#--------------------------------------------------------------------------------------------------------------------------------
def divDumVetorPorOutro(x, y):
    ret = []
    for i in range(len(x) - 1):
        ret.append(divisao(x[i], y[i]))
    return ret
#--------------------------------------------------------------------------------------------------------------------------------
#-- CHECAR IGUAL
#--------------------------------------------------------------------------------------------------------------------------------
def checkIgual(vet):
    for pos in range(len(vet)):
        vetComp = vet[pos]
        if all(i == vetComp[0] for i in vetComp):
            return True
        return False
#--------------------------------------------------------------------------------------------------------------------------------
#-- HA ZERO NA DIAGONAL
#--------------------------------------------------------------------------------------------------------------------------------
def haZeroNaDiagonal(m, permL, permC):
    for pos in range(len(m)):
        if m[permL[pos]][permC[pos]] == 0:
            return True
    return False
#--------------------------------------------------------------------------------------------------------------------------------
#-- POE UM NA DIAGONAL PRINCIPAL NA LINHA
#--------------------------------------------------------------------------------------------------------------------------------
def poeUmNaDiagonalPrincipalNaLinha(lin, m, permL, permC):
    divisor = m[permL[lin]][permC[lin]]
    for col in range(len(m)):
        m[permL[lin]][permL[col]] = divisao(m[permL[lin]][permL[col]], divisor)
    m[permL[lin]][len(m)] = divisao(m[permL[lin]][len(m)], divisor)
#--------------------------------------------------------------------------------------------------------------------------------
#-- COLOLOCAR ZERO NA COLUNA
#--------------------------------------------------------------------------------------------------------------------------------
def colocarZeroNaColuna(m, col, permL, permC):
    vetorMult = []

    for pos in range(len(m) + 1):
        vetorMult.append(m[permL[col]][pos])

    vetorMult.append(m[permL[col]][len(m)])

    for lin in range(0, len(m)):
        mult = m[permL[lin]][permC[col]]
        if lin != col:
            for rec in range(len(m) + 1):
                m[permL[lin]][rec] = m[permL[lin]][rec] - (mult * vetorMult[rec])
#--------------------------------------------------------------------------------------------------------------------------------
#-- COMO SE LIVRAR DE ZEROS NA DIAGONAL
#--------------------------------------------------------------------------------------------------------------------------------
def comoSeLivrarDeZerosNaDiagonal(matriz):
    perms = permutacoes(list(range(len(matriz))))
    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(matriz, perms[i], perms[j]):
                return [perms[i], perms[j]]

    return None
#--------------------------------------------------------------------------------------------------------------------------------
#-- CONTEM ALGO ALEM DE ZERO NA COLUNA
#--------------------------------------------------------------------------------------------------------------------------------
def contemAlgoAlemDeZeroNaColuna(matriz, col, permL, permC):
    for i in range(len(matriz)):
        if matriz[permL[i]][permC[col]] != 0:
            return True
    return False
#--------------------------------------------------------------------------------------------------------------------------------
#-- CHECAR SE E POSSIVEL SOLUCIONAR
#--------------------------------------------------------------------------------------------------------------------------------
def checagem():
    comb = combinacoesLinhas(OriginalMatriz)
    check = []
    for pos in range(len(OriginalMatriz)):
        check.append(divDumVetorPorOutro(
            OriginalMatriz[comb[pos][0]], OriginalMatriz[comb[pos][1]]))

    if checkIgual(check):
        print("Não é possivel solucionar a Matriz")
        return False
    else:
        return True
#--------------------------------------------------------------------------------------------------------------------------------
#-- DIVISAO
#--------------------------------------------------------------------------------------------------------------------------------
def programa(perm): 
    permL = perm;permC = perm

    if checagem():
        if haZeroNaDiagonal(OriginalMatriz, permL, permC):
            vetorPerms = comoSeLivrarDeZerosNaDiagonal(OriginalMatriz)
            permL = vetorPerms[0]
            permC = vetorPerms[1]

        for pos in range(len(OriginalMatriz)):
            poeUmNaDiagonalPrincipalNaLinha(pos, OriginalMatriz, permL, permC)

            if contemAlgoAlemDeZeroNaColuna(OriginalMatriz, pos, permL, permC):
                colocarZeroNaColuna(OriginalMatriz, pos, permL, permC)

        variables2 = 0
        linhas = len(OriginalMatriz)

        for var2 in range(linhas):
            print(f"{OriginalMatriz[var2]}: {OriginalMatriz[var2][linhas]}")
            variables2 += 1

#--------------------------------------------------------------------------------------------------------------------------------
#-- DIVISAO
#--------------------------------------------------------------------------------------------------------------------------------
programa(listaOrdenadaGenerica(OriginalMatriz))
