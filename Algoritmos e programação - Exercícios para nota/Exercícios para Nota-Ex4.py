# 4. Escreva um programa em Python que implementa o Crivo de Eratóstenes. Este
# é um método simples e prático para encontrar números primos de 2 até um valor
# limite N (fornecido pelo usuário). Funciona da seguinte forma:
# Por exemplo, para encontrar todos os números primos entre 2 e 30 (N=30), basta
# dispor os números deste intervalo em uma lista:
# [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# Em seguida, para cada número da lista, basta eliminar os seus números múltiplos.
# Inicialmente, pegue o primeiro número da lista, 2, e remova todos os números
# múltiplos dele, deixando o número 2. A lista ficará assim:
# [2, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# Em seguida, pegue o próximo número, 3, e remova todos os múltiplos de 3. A
# lista ficará assim:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 25, 29]
# Na próxima etapa, pegue o número 5 e remova todos os seus múltiplos. A lista
# ficará assim:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# E assim por diante. No final do processo, a lista conterá somente os números
# primos entre 2 e N.

lista_numeros=[]
primeira_lista=[]
num=0

#Pedir ao usuário os números
numero=int(input("Digite o número de parada (Verificação de números primos): "))

#Adicionar em uma lista
for num in range(2,numero+1):
    lista_numeros.append(num)
print(f"{lista_numeros}")

#Eliminar os múltiplos do primeiro número
for elemento in (lista_numeros):
    for proximo_elemento in (lista_numeros):
        if proximo_elemento!=elemento and proximo_elemento%elemento == 0:
            lista_numeros.remove(proximo_elemento)
print(lista_numeros)