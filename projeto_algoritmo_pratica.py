matriz = [[4,0,2,24],\
          [2,3,0,16],\
          [0,3,2,28]]

table = []

def haZeroNaDiagonal (m):
    qtdDeZeros=0
    posicao=0
    while posicao<len(m):
        if m[posicao][posicao]==0: qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
    
def poeUmNaDiagonalPrincipalNaLinha (lin,m):
    divisor=m[lin][lin]
    col=0
    while col<=len(m):
        m[lin][col]/=divisor
        col+=1

def multiplicarLinhasafimdezerar(m,t,n1,n2,v1,v2):
    valornegativo = -(m[n1][n2])
    col=0
    while col<=len(m):
        value = m[v1][col] * valornegativo
        table.append(value)
        col+=1

    val=0
    while val<=len(m):
        m[v2][val] += t[val]
        val+=1


poeUmNaDiagonalPrincipalNaLinha(0,matriz)
multiplicarLinhasafimdezerar(matriz,table,1,0,0,1)
table = []
poeUmNaDiagonalPrincipalNaLinha(1,matriz)
multiplicarLinhasafimdezerar(matriz,table,2,1,1,2)
print(matriz)
#print (haZeroNaDiagonal(matriz))