matriz = [[4,0,2,24],\
          [2,3,0,16],\
          [0,3,2,28]]

table = []
#--------------------------------------------------------------------------------------------------------------------------------
#-- VERIFICAR SE TEM ZERO NA DIAGONAL
#--------------------------------------------------------------------------------------------------------------------------------
def haZeroNaDiagonal (m):
    qtdDeZeros=0
    posicao=0
    while posicao<len(m):
        if m[posicao][posicao]==0: qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
#--------------------------------------------------------------------------------------------------------------------------------
#-- COLOCAR NUMERO UM NA DIAGONAL
#--------------------------------------------------------------------------------------------------------------------------------
def poeUmNaDiagonalPrincipalNaLinha (lin,m):
    divisor=m[lin][lin]
    col=0
    while col<=len(m):
        m[lin][col]/=divisor
        col+=1
#--------------------------------------------------------------------------------------------------------------------------------
#-- ALTERAR OS VALORES DAS LINHAS PARA TORNAR ZERO
#--------------------------------------------------------------------------------------------------------------------------------
def change_lines_value(m,t1,t2,v1,v2):
    valornegativo = -(m[t1][t2])
    col=0
    while col<=len(m):
        value = m[v1][col] * valornegativo
        table.append(value)
        col+=1

    val=0
    while val<=len(m):
        m[v2][val] += table[val]
        val+=1
     
    
if not haZeroNaDiagonal(matriz):    
    poeUmNaDiagonalPrincipalNaLinha(0,matriz)
    change_lines_value(matriz,1,0,0,1)
    table = []
    poeUmNaDiagonalPrincipalNaLinha(1,matriz)
    change_lines_value(matriz,2,1,1,2)

    table = []
    poeUmNaDiagonalPrincipalNaLinha(2, matriz)
    change_lines_value(matriz,0,2,2,0)

    table = []
    change_lines_value(matriz, 1, 2, 2, 1)
#--------------------------------------------------------------------------------------------------------------------------------
#-- EXIBIR A MATRIZ
#--------------------------------------------------------------------------------------------------------------------------------
    for num in matriz:
        print(num)

    print(f"Valor do x = {matriz[0][3]}, Valor do y = {matriz[1][3]}, Valor do z = {matriz[2][3]}")