matriz = [[0,1,0,20],\
          [0,0,4,16],\
          [6,3,0,28]]

table = []
#--------------------------------------------------------------------------------------------------------------------------------
#-- VERIFICAR SE TEM ZERO NA DIAGONAL | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def haZeroNaDiagonal (m,ordemL,ordemC):
    qtdDeZeros=0
    posicao=0
    while posicao<len(m):
        if m[ordemL[posicao]][ordemC[posicao]]==0: qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
#--------------------------------------------------------------------------------------------------------------------------------
#-- VERIFICAR SE TEM ZERO NA DIAGONAL | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
# def haZeroNaDiagonal (m):
#     qtdDeZeros=0
#     posicao=0
#     while posicao<len(m):
#         if m[posicao][posicao]==0: qtdDeZeros+=1
#         posicao+=1
#     return qtdDeZeros>0
#--------------------------------------------------------------------------------------------------------------------------------
#-- COLOCAR NUMERO UM NA DIAGONAL | PROFESSOR
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
#--------------------------------------------------------------------------------------------------------------------------------
#-- PEGAR A MATRIZ DO .TXT | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def carregaMatriz (nomeArq):
    arq     = open(nomeArq,"r")
    qtdLins = int (arq.readline())
    
    ret = []
    for lin in range(qtdLins):
        texto = arq.readline().split()
        
        linha = []
        for col in range(qtdLins+1): linha.append(float(texto[col])) 
            
        ret.append(linha)
        
    arq.close()
    return ret
print(carregaMatriz("sistema.txt"))
#--------------------------------------------------------------------------------------------------------------------------------
#-- PEGAR A MATRIZ DO .TXT | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def divisao (a,b):
    if a==0 and b==0:
        return "indeterminado"
    elif b==0:
        return "infinito"
    else:
        return a/b
        
def divDumVetorPorOutro (x,y):
    ret=[]
    for i in range(len(x)-1): ret.append(divisao(x[i],y[i]))
    return ret

def paresDeLinhas(m):
    ret = []
    for lin in range(len(m)):
        for col in range(lin+1,len(m)):
            ret.append([lin,col])
    return ret

print(paresDeLinhas(matriz))
    
#print(divDumVetorPorOutro([1,0,2,0],[0,0,4,2]))
#--------------------------------------------------------------------------------------------------------------------------------
#-- FAZ A PERMUTACAO PARA ACHAR AS POSSIVEIS COMBINAÇÕES | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
# função auxiliar  recursivo que, de fato, gera as permutacoes
# NÃO USE DIRETAMENTE ESTA FUNÇÃO; USE A FUNÇÃO permutacoes
# recebe uma lista com os valores a serem permutados (linha),
# uma lista com os itens na permutação sendo gerada (perm) e
# uma lista com as permutações geradas (perms) 
def permuta (linha, perm, perms):
    if linha==[]:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin]+linha[lin+1:len(linha)],perm+[linha[lin]],perms)

# função principal para gerar permutações;
# USA A FUNÇÃO permuta, QUE NÃO DEVE SER USADA DIRETAMENTE;
# recebe uma lista com os valores a serem permutados (linha)
# retorna as permutações geradas
def permutacoes (linha):
    perms=[]
    permuta(linha,[],perms)
    return perms
    
#print(permutacoes([0,1,2,3]))
#--------------------------------------------------------------------------------------------------------------------------------
#-- ALTERAR AS ORDENS PARA TIRAR OS ZEROS DA DIAGONAL | PROFESSOR
#--------------------------------------------------------------------------------------------------------------------------------
def comoSeLivrarDeZerosNaDiagonal(m):
    perms = permutacoes(list(range(len(m))))

    for i in range(len(perms)):
        for j in range(len(perms)):
            if not haZeroNaDiagonal(m,perms[i],perms[j]):
                return [perms[i],perms[j]]
    return None
#--------------------------------------------------------------------------------------------------------------------------------
#-- MAIN
#--------------------------------------------------------------------------------------------------------------------------------       
# if not haZeroNaDiagonal(matriz):    
#     poeUmNaDiagonalPrincipalNaLinha(0,matriz)
#     change_lines_value(matriz,1,0,0,1)
#     table = []
#     poeUmNaDiagonalPrincipalNaLinha(1,matriz)
#     change_lines_value(matriz,2,1,1,2)

#     table = []
#     poeUmNaDiagonalPrincipalNaLinha(2, matriz)
#     change_lines_value(matriz,0,2,2,0)

#     table = []
#     change_lines_value(matriz, 1, 2, 2, 1)
print(comoSeLivrarDeZerosNaDiagonal(matriz))
#--------------------------------------------------------------------------------------------------------------------------------
#-- EXIBIR A MATRIZ
#--------------------------------------------------------------------------------------------------------------------------------
    # for num in matriz:
    #     print(num)

    # print(f"Valor do x = {matriz[0][3]}, Valor do y = {matriz[1][3]}, Valor do z = {matriz[2][3]}")