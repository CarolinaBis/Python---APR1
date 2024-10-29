# 6. Após o desfile das escolas de samba, ocorre a apuração dos votos para definir
# a escola campeã. As M escolas de samba recebem notas (de 0.0 a 10.0) em N
# categorias segundo avaliação de K jurados. Faça um programa em Python que leia
# quantidade de escolas de samba (M), a quantidade de categorias avaliadas (N) e a
# quantidade de jurados (K). Em seguida,
# I) Leia e armazene em uma matriz as notas obtidas para cada escola, em cada
# categoria, dada por cada jurado. Por exemplo, a matriz abaixo (MxNxK) armazena as
# notas para 4 escolas de samba(M), em 3 categorias (N), dadas por 2 jurados (K):
# notas = [[[10.0,10.0], [9.0,8.5], [9.0,9.5]],
#  [[10.0,9.5], [9.5,9.0], [8.5,9.0]],
#  [[9.0,9.5], [8.5,9.0], [9.0,9.0]],
#  [[9.5,9.5], [9.5,9.0], [8.5,8.5]]]
# II) Calcule e mostre a soma dos pontos para cada escola de samba. No exemplo dado
# anteriormente, é possível verificar que a primeira escola de samba obteve o total de
# 56 pontos (10.0+10.0+9.0+8.5+9.0+9.5 = 56)
# III) Calcule e mostre a média dos pontos por categoria para cada escola de samba.
# Ainda no nosso exemplo, a primeira escola de samba obteve a média 10.0 na
# primeira categoria, média 8.75 na segunda categoria e média 9.25 na terceira
# categoria.

matriz=[]

#Pedir as variaveis ao usuario
escolas_m=int(input("Digite a quantidade de escolas de samba: "))
categoria_n=int(input("Digite a quantidade de categorias avaliadas: "))
jurados_k=int(input("Digite a quantidade de jurados: "))

#Leia e armazene em uma matriz as notas obtidas para cada escola, em cada
# categoria, dada por cada jurado.
for m in range(escolas_m):
    lista=[]
    for n in range(categoria_n):
        lista_notas=[]
        for k in range(jurados_k):
            notas=float(input("Digite as notas das escolas de samba: "))
            lista_notas.append(notas)
        lista.append(lista_notas)
    matriz.append(lista)
print(f"A matriz é: {matriz}")

# Calcule e mostre a soma dos pontos para cada escola de samba.
lista_soma=[]

for m in range(escolas_m):
    nota_total=0
    for n in range(categoria_n):
        for k in range(jurados_k):
            nota_total+=matriz[m][n][k]
    lista_soma.append(nota_total)
print(f"A soma dos pontos de cada escola de samba é: {lista_soma}")
            
# Calcule e mostre a média dos pontos por categoria para cada escola de samba.
categoria_media=[]

for m in range(escolas_m):
    for n in range(categoria_n):
        categoria_soma=0
        for k in range(jurados_k):
            categoria_soma+=matriz[m][n][k]
        categoria_media.append(categoria_soma/categoria_n)
print(f"A média dos pontos por categoria para cada escola de samba é: {categoria_media}")

