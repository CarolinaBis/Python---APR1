# 5. Faça um programa em Python que leia uma matriz A de números inteiros com
# dimensões NxM (N e M fornecidos pelo usuário). Em seguida, o programa deverá
# criar e mostrar a matriz transposta(At) de A. Lembre-se que a matriz transposta Até
# obtida a partir da matriz A, trocando-se ordenadamente as linhas por colunas (ou as
# colunas por linhas), como no exemplo a seguir:

valor=0
matriz=[]
contador=1
matriz_transposta=[]

#Pedir para o usuário as dimensões
linhas_n=int(input("Digite a quantidade de linhas da matriz(N): "))
colunas_m=int(input("Digite a quantidade de colunas da matriz(M): "))

#Matriz original
for linhas in range(linhas_n):
    lista=[]
    for colunas in range(colunas_m):
        lista.append(contador)
        contador+=1
    matriz.append(lista)
    print(f"A matriz é: {matriz[linhas]}")

#Matriz transposta
for colunas_transposta in range(colunas_m):
    lista=[]
    for linhas_transposta in range(linhas_n):
        lista.append(matriz[linhas_transposta][colunas_transposta])
    matriz_transposta.append(lista)
    print(f"A matriz transposta é: {matriz_transposta[colunas_transposta]}")