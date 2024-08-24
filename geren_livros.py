#funções
def cadastrar_livro(id):
    '''
    Função para cadastrar livro
    Recebe três inputs sobre o livro
    Armzena em um dicionário
    Adiciona uma cópia em uma lista
    '''
    print('-' * 48)
    print(' ' * 13,"CADASTRAR LIVRO")
    
    print(f"Id do livro: {id}")

    nome = input("Digite o nome do livro: ").upper()
    autor = input("Digite o autor do livro: ").upper()
    editora = input("Digite a editora do livro: ").upper()
    
    cadastro = {'Id': id,'Nome': nome, 'Autor': autor, 'Editora': editora}
    
    lista_livro.append(cadastro.copy())

def consultar_livro():
    '''
    Função para consulta do(s) livro(s) cadastrado(s)
    Recebe um input para seleção de uma opção
    Condiciona a escolha
    Filtra os dados conforme a escolha
    Retorna os dados para o usuário   
    '''
    while True:
        print('-' * 48)
        print(' ' * 13,"CONSULTAR LIVRO")
        print("Opções")
        print("1 - Consultar todos")
        print("2 - Consultar por id")
        print("3 - Consultar por autor")
        print("4 - Retornar ao menu principal")

        opc = input()

        if (opc == '1'):
            print('-' * 48)
            for d in lista_livro:
                [print(f"{key}: {value}") for key, value in d.items()]#List comprehension
                print('\n')

        elif (opc == '2'):
            chave = int(input("Digite a id do livro: "))
            print('-' * 48)
            
            for d in lista_livro:
                for item in d.values():
                    if item == chave:
                        [print(f"{key}: {value}") for key, value in d.items()]
                        print('\n')

        elif (opc == '3'):
            chave = input("Digite o autor do livro: ").upper()
            print('-' * 48)

            for d in lista_livro:
                for item in d.values():
                    if item == chave:
                        [print(f"{key}: {value}") for key, value in d.items()]
                        print('\n')

        elif (opc == '4'):
            return

        else:
            print('Opção inválida')
            continue

def remover_livro():
    '''
    Função para remover item na lista
    Recebe um input
    Compara o input com a lista
    Deleta o dicionário 
    '''
    id_remover = int(input("Digite a id do livro a ser removido: "))

    for i in range(len(lista_livro)):
        if lista_livro[i]['Id'] == id_remover:
            del lista_livro[i]
            break

#Mensagem
print("Bem-vindo a Livraria do Gustavo Oliveira")

#Programa Principal
lista_livro = list()
id_global = 0

while True:
    print('-' * 48 )
    print(' ' * 13, "MENU PRINCIPAL")
    print("Opções")
    print("1 - Cadastrar livro")
    print("2 - Consultar livro")
    print("3 - Remover livro")
    print("4 - Sair")

    opc = input()

    if (opc == '1'):
        id_global += 1
        cadastrar_livro(id_global)
    
    elif (opc == '2'):
        consultar_livro()

    elif (opc == '3'):
        remover_livro()

    elif (opc == '4'):
        break

    else:
        print("Opção inválida!")
        continue