# 3) (Para resolver este exercício, utilize como exemplo o programa “agenda de
# contatos”, estudado durante a aula. Embora este exercício aborde arquivos, o foco
# é: função, passagem de parâmetros, retorno de função, dicionário e tupla.)
# Faça um programa que armazene no arquivo “notas_apr1.txt”: o prontuário, o
# nome e as notas dos alunos da disciplina APR1. O arquivo deverá estar no seguinte
# formato:
# SC1111 Manoel 7.5 8.0 9.0
# SC2222 José 6.0 5.5 7.5
# SC3333 Maria 9.0 8.5 9.5
# - Utilize o separador ‘\t’ para separar as colunas.
# - O programa deverá conter o seguinte MENU PRINCIPAL, apresentado via
# a função exibir_menu(), contendo as opções:
# 1 - Cadastrar aluno e notas:
# Quando esta opção do menu for selecionada, ela deverá chamar 3 funções:
# i) uma função para ler via teclado os dados do aluno. Faça validação das notas,
# não permitindo que o usuário digite números fora do intervalo 0-10 (Utilize uma
# outra função para esta validação). Os dados lidos deverão ser retornados em uma
# tupla.
# ii) em seguida, outra função deverá inserir os dados armazenados na tupla em
# um dicionário, onde o prontuário é a chave e o seu valor é formado por uma lista
# contendo o restante dos dados. Exemplo: ‘SC1111’: [‘Manoel’, 7.5, 8.0, 9.0].
# iii) por fim, uma terceira função será responsável por inserir os dados (tupla)
# no final do arquivo “notas_apr1.txt”. ATENÇÂO: para gravar dados no arquivo,
# estes devem ser do tipo str. Portanto, faça a conversão necessária entre str e int
# quando lidar com as notas dos alunos
# 2 - Mostrar alunos e notas:
# Esta função deverá mostrar para cada aluno o seu nome, as suas notas, a média
# aritmética das suas notas e sua situação (“Aprovado, “IFA” ou “Reprovado”).
# DICA: crie funções separadas, cada qual realizando uma tarefa específica: crie
# uma para calcular e retornar a média, outra para retornar a situação do aluno
# (“Aprovado”, “IFA” ou “Reprovado”) e uma terceira para mostrar o que se está
# pedindo. Isso facilita a leitura e o reuso do código.
# 3 - Pesquisar aluno: crie uma função que receba o prontuário do aluno e, se
# ele estiver cadastrado, mostre seu nome, suas notas, a média aritmética das notas e
# sua situação (“Aprovado”, “IFA” ou “Reprovado”). Caso o prontuário não seja
# encontrado, mostre a mensagem “Aluno não cadastrado”.

# Menu principal
def exibir_menu():
    print("MENU PRINCIPAL")
    # Formatação estético
    print("--------------")
    print("1 - Cadastrar aluno e notas")
    print("2 - Mostrar alunos e notas")
    print("3 - Pesquisar aluno")
    print("4 - Sair")
    # Espaço print (formatação)
    print(" ")
    return input("Escolha uma opção: ")


# Ler via teclado os dados do aluno
def ler_dados():
    lista_notas=[]
    # Espaço print (formatação)
    print(" ")

    nome=input("Digite o nome do aluno: ")
    prontuario=input("Digite o prontuário do aluno: ")

    for contator in range(3):
        nota=float(input(f"Digite a nota {contator + 1}º: "))

        # Validação de notas
        while not validar_notas(nota):
            print("Nota inválida! Digite um valor de 0 a 10.")
            nota=float(input(f"Digite a nota {contator + 1}º: "))
        lista_notas.append(nota)

        # Dados lidos deverão ser retornados em uma tupla. 
        aluno=(prontuario,nome,lista_notas)

    # Espaço print (formatação)
    print(" ")
    return aluno

# Faça validação das notas,não permitindo que o usuário digite números fora do intervalo 0-10
def validar_notas(nota):
    return nota<=10 and nota>=0

# Função que deverá inserir os dados armazenados na tupla em um dicionário
def dados_dicionario (dicionario,dados):
    prontuario, nome, lista_notas = dados
    dicionario[prontuario] = (nome,lista_notas,)
    salvar_dados_no_arquivo(dicionario)
    return dicionario 
    
def salvar_dados_no_arquivo(dados):
    if len(dados):
        arquivo = open("arquivo.txt", "w")
        for informacoes in dados:
            prontuario = informacoes
            dados_prontuario = dados[prontuario]
            #print("dados: ",dados_prontuario)
            nome = dados_prontuario[0]
            notas = dados_prontuario[1]
            nota_1 = notas[0]
            nota_2 = notas[1]
            nota_3 = notas[2]
            linha = prontuario + "\t" + nome + "\t" + str(nota_1) +  "\t" + str(nota_2) +  "\t" + str(nota_3) + "\n"  
            arquivo.write(linha)
        arquivo.close()

def exite_arquivo(nome):
    import os
    if os.path.exists(nome):
        return True
    else:
        return False

def ler_dados_arquivo(dados):
    if exite_arquivo("arquivo.txt"):
        arquivo = open("arquivo.txt", "r")
        for linha in arquivo:
            linha = linha[:len(linha)-1]
            linha_formatada = linha.split("\t")
            prontuario = linha_formatada[0]
            nome = linha_formatada[1]
            notas = []
            notas.append(float(linha_formatada[2]))
            notas.append(float(linha_formatada[3]))
            notas.append(float(linha_formatada[4]))
            dados[prontuario] = (nome, notas,)
        arquivo.close()

# Calcular média
def calcular_media(lista_notas):
    soma=0
    for valores in lista_notas:
        for valor in valores:
            soma+=valor
    media=soma/len(valores)
    return(media)

# Retornar a situação do aluno
def situacao_aluno(media):
    if media < 4:
        return "Reprovado"
    elif media >= 4 and media <6:
        return "IFA"
    else:
        return "Aprovado"

# Mostra as informações do aluno
def mostrar_aluno (dicionario):
    for prontuario, dados in dicionario.items():
        nome = dados[0]
        lista_notas = dados[1:]
        media = calcular_media(lista_notas)
        situacao = situacao_aluno(media)

        print(f"Nome: {nome} ")
        print(f"Prontuário: {prontuario}")
        print(f"Notas: {lista_notas[0][0]} {lista_notas[0][1]} {lista_notas[0][2]}")
        print(f"Média: {media}")
        print(f"{situacao}")
        # Espaço print (formatação)
        print(" ")

# Crie uma função que receba o prontuário do aluno e mostre todas as informações do aluno
def informacoes_aluno_prontuario (dicionario,prontuario):
    if prontuario in dicionario:
        dados = dicionario[prontuario]
        nome = dados[0]
        lista_notas = dados[1:]
        media = calcular_media(lista_notas)
        situacao = situacao_aluno(media)

        print(f"Nome: {nome} ")
        print(f"Notas: {lista_notas}")
        print(f"Média: {media} ")
        print(f"{situacao}")
        # Espaço print (formatação)
        print(" ")
    else:
        print("Aluno não cadastrado.")

def main():
    dicionario={}
    ler_dados_arquivo(dicionario)
    while True:
        opcao=exibir_menu()
        if opcao == "1":
            info = ler_dados()
            dicionario=dados_dicionario(dicionario,info)
        elif opcao == "2":
            mostrar_aluno(dicionario)        
        elif opcao == "3":
            prontuario=input("Digite o prontuário do aluno: ")
            informacoes_aluno_prontuario(dicionario,prontuario)
        elif opcao == "4":
            print("Programa encerrado")
            break
        else:
            print(" ")
            print("Opção inválida!")
            print(" ")
main()
