# 2. Elabore um programa em Python que leia idade, peso e altura de algumas
# pessoas. O programa deve ser encerrado quando uma idade negativa for informada
# pelo usuário. Ao final do programa mostre:
# I) A média das idades das pessoas;
# II) O valor da menor altura;
# III) A quantidade de pessoas com peso superior a 90 Kg ou altura inferior a 1.50 m;
# IV) O percentual de pessoas com idade entre 10 e 30 anos entre as pessoas que
# medem mais de 1.90 m de altura.

contador = 0
lista_idade=[]
lista_altura=[]
lista_peso=[]
idade=0
soma=0

while idade >=0:
    contador+=1
    idade=int(input(f"Digite a {contador}º idade: "))
    if idade < 0:
        print("Programa encerrado")
    else:
        peso=float(input(f"Digite o {contador}º peso: "))
        altura=float(input(f"Digite a {contador}º altura: "))
        print("-------------------------")
        lista_idade.append(idade)
        lista_altura.append(altura)
        lista_peso.append(peso)

# A média das idades das pessoas;
for x in lista_idade:
    soma += x 
media = soma/len(lista_idade)
print(f"A média das idades das pessoas é: {media}")

#O valor da menor altura
menor_altura=lista_altura[-1]

for elemento_altura in (lista_altura):
    if elemento_altura < menor_altura:
        menor_altura=elemento_altura
print(f"A menor altura é: {menor_altura}")

#A quantidade de pessoas com peso superior a 90 Kg ou altura inferior a 1.50 m
quantidade_peso_altura=0
for indice in range(len(lista_peso)):
    if lista_peso[indice] > 90 or lista_altura[indice]<1.50:
        quantidade_peso_altura+=1
print(f"A quantidade de pessoas com peso superior a 90 Kg ou altura inferior a 1.50 m é:{quantidade_peso_altura}")

#O percentual de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1.90 m de altura.
quantidade_altura=0
for indice_altura in range(len(lista_altura)):
    if 30 >= lista_idade[indice_altura] >= 10 and lista_altura[indice_altura] > 1.90:
        quantidade_altura+=1
    percentual=quantidade_altura/len(lista_idade)
print(f"O percentual de pessoas com idade entre 10 e 30 anos entre as pessoas que medem mais de 1.90 m de altura: {percentual*100}%")




