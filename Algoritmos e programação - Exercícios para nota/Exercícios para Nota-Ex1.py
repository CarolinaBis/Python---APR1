# 1. Uma progressão aritmética é definida em termos de seu valor inicial e a razão da
# progressão. Exemplo: na sequência abaixo o valor inicial é 5 e a razão é 3:
# PA = 5, 8, 11, 14, 17, 20, 23, ....
# Escreva um programa em Python que solicite ao usuário o valor inicial, a razão da
# progressão e a quantidade total de termos para serem mostrados. Mostre a sequência
# gerada na tela.

valor_inicial = int(input("Digite o valor inicial: "))
razao = int(input("Digite a razão da progressão: "))
total = int(input("Digite o total de termos: "))

for x in range(total):
    print(f"{valor_inicial}")
    valor_inicial+=razao
    


