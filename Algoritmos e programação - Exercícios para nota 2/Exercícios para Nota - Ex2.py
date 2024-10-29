# 2) Faça um programa que possua as funções:
# I) criar_matriz(N,M): deverá criar e retornar uma matriz NxM contendo
# valores inteiros fornecidos pelo usuário.
# II) somar_diagonal(matriz): recebe uma matriz e retorna a soma dos
# elementos de sua diagonal principal.
# III) mostrar_matriz(matriz): deverá mostrar a matriz formatada.
# IV) calcular_media(matriz): deverá calcular a média aritmética para cada uma
# das N linhas da matriz. A função retorna, então, uma lista de tamanho N, onde cada
# elemento i da lista representa a média da linha i da matriz.
# Exemplo: para a matriz (2 linhas X 3 colunas) [[10,20,30], [2,4,6]], a função
# deverá retornar a lista [20, 4]. Repare que o primeiro elemento da lista (20) é a média
# da primeira linha da matriz (10,20,30). O segundo elemento da lista (4) é a média da
# segunda linha da matriz (2,4,6). E assim por diante.

# Deverá criar e retornar uma matriz NxM contendo valores inteiros fornecidos pelo usuário
def criar_matriz(n,m):
    matriz=[]
    for linhas in range(n):
        linhas=[]
        for quantidades in range(m):
            n=int(input("Digite os valores da matriz: "))
            linhas.append(n)
        matriz.append(linhas)
    return matriz

# Recebe uma matriz e retorna a soma dos elementos de sua diagonal principal
def somar_diagonal(matriz):
    soma=0
    for indice in range(len(matriz)):
        soma+=matriz[indice][indice]
    return soma

# Deverá mostrar a matriz formatada
def mostrar_matriz(matriz):
    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            print(matriz[linha][coluna], end=" ")
        print()

# Deverá calcular a média aritmética para cada uma das N linhas da matriz
def calcular_media(matriz):
    lista_medias=[]
    for linha in (matriz):
        soma=0
        for elemento in (linha):
            soma+=elemento
        media=soma/len(linha)
        lista_medias.append(media)
    return lista_medias

# Pedir o tamanho da matriz para o usuário e imprimir os valores
def main():
    quantidade_n=int(input("Digite a quantidade de linhas(N) da matriz: "))
    quantidade_m=int(input("Digite a quantidade de colunas(M) da matriz: "))

    matriz=criar_matriz(quantidade_n,quantidade_m)
    
    mostrar_matriz(matriz)
    print(f"A soma da diagonal principal é: {somar_diagonal(matriz)}")
    print(f"A média aritmética de cada uma das N linhas da matriz: {calcular_media(matriz)}")
main()
