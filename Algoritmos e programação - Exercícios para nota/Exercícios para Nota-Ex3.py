# 3. Faça um programa em Python que leia N números inteiros, sendo N fornecido
# pelo usuário. Em seguida, o programa deverá solicitar do usuário um número X
# qualquer e:
# I) Mostrar quantas vezes o número X aparece na lista
# II) Mostrar quantos elementos da lista são maiores que X e quantos são menores
# que X
# III) Criar uma segunda lista, cujos elementos serão os elementos da lista original
# multiplicados pelo número X (lido anteriormente).


lista_numeros=[]
lista_multiplicada=[]


quantidade_numeros=int(input("Digite a quantidade de números (N): "))
x=int(input("Digite o número (X): "))
for valor in range(quantidade_numeros):
    valores=int(input("Digite os valores: "))
    lista_numeros.append(valores)
#Criar uma segunda lista, cujos elementos serão os elementos da lista original multiplicados pelo número X (lido anteriormente).
    multiplicacao=valores*x
    lista_multiplicada.append(multiplicacao)

cont_maior=0
cont_menor=0
cont_igual=0
cont_vezes=0

for vezes in (lista_numeros):
    #Mostrar quantas vezes o número X aparece na lista
    if vezes == x:
        cont_igual+=1
    #Mostrar quantos elementos da lista são maiores que X e quantos são menores que X    
    if vezes > x:
        cont_maior+=1
        
    if vezes < x:
        cont_menor+=1

print(f"Quantidade de vezes que o número (X) aparece: {cont_maior}")
print(f"Elementos maior que X: {cont_maior}")
print(f"Elementos menor que X: {cont_menor}")
print(f"A lista multiplicada pelo número (X) é: {lista_multiplicada}")


    



