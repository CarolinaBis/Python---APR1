# 1) Escreva uma função recursiva que receba como argumento uma lista de
# listas de números inteiros e devolve a quantidade de números pares existentes nas
# sublistas.
# Por exemplo, no caso da lista [[4,6,5,1],[5,3,9],[],[4,0,10]] a função deve
# devolver 5.
# Se achar necessário, pode criar funções auxiliares, desde que sejam funções
# recursivas.

def numeros_pares (lista):
    # Se a lista estiver vazia, não há números pares
    if len(lista) == 0:
        return 0
    # Primeira sublista da lista
    sublista=lista[0]
    # Restante das sublistas
    resto_sublista=lista[1:]
    # Chama recursivamente a função para contar os pares na sublista atual e nas sublistas restantes
    return(contar_pares(sublista)+numeros_pares(resto_sublista)) 
    
def contar_pares(sublista):
    # Se a sublista estiver vazia, não há números pares
    if len(sublista) == 0:
        return 0
    # Primeiro número da sublista
    elemento=sublista[0]
    # Restante dos números da sublista 
    resto_elemento=sublista[1:]
    # Retorna 1 se o elemento for par, caso contrário, retorna 0, e chama recursivamente a função para o resto da sublista
    return(1 if elemento % 2 == 0 else 0) + contar_pares(resto_elemento)

def main():
    #Pede ao usuário os valores e cria a lista e as sublistas
    lista=[]
    quantidade_sublistas=int(input("Digite a quantidade de sublistas: "))
    for valores in range(quantidade_sublistas):
        sublista=[]
        quantidade_numeros=int(input("Digite a quantidade de valores da sublista: "))
        for numero in range(quantidade_numeros):
            numeros=int(input("Digite os números da sublista: "))
            sublista.append(numeros)
        lista.append(sublista)
    # Chama a função para contar os números pares e imprime o resultado
    print(f"A quantidade de números pares: {numeros_pares(lista)}")
    return 
main()