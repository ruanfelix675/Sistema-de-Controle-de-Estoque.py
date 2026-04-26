'''1. cadastrar_produtos()
• Recebe os nomes dos produtos
• Armazena os produtos e quantidades em um dicionário
• Retorna o dicionário final'''
def cadastrar_produtos():
    produtos = {}
    while True:
        print('digite fim para encerar')
        nome_produto = input('digite o nome do produto:')
        if nome_produto == 'fim':
            break
        if nome_produto in produtos:
            print('produto ja registrado')
        else:
            qtd = int(input('digite a quantidade:'))
            produtos.update({nome_produto:qtd})
            print(produtos)
    return produtos    

lista = cadastrar_produtos()

'''2. calcular_total(estoque)
• Recebe o dicionário
• Soma todas as quantidades cadastradas
• Retorna o total de produtos'''
def calcular_total():
    print(f'soma {sum(lista.values())}')
    print(f'total de produtos registrados {len(lista)}')
calcular_total()

'''3. maior_estoque(estoque)
• Retorna o produto com maior quantidade
'''
def maior_estoque():
    print(f'produto com maior quantidade {max(lista,key=lista.get)}')
maior_estoque()

'''4. menor_estoque(estoque)
• Retorna o produto com menor quantidade
'''
def menor_estoque():
    print(f'produto com menor quantidade {min(lista,key=lista.get)}')
    
menor_estoque()

'''5. remover_produto(estoque)
• Remove um produto do sistema caso ele não seja mais vendido
    '''
def remover_produto() :
    while True:
        print('quais produtos deseja remover?')
        print(lista)
        print('digite fim para encerar')
        opc = input('digite o produto a ser removido:')
        if opc == 'fim':
            break
        if opc in lista:
            lista.pop(opc)
            print('produto removido')
            print('lista atual')
            print(lista)
        else:
            print('produto nao existe ou ocorreu um erro de digitaçao')
remover_produto() 

'''6. atualizar_estoque(estoque)
• Permite alterar a quantidade de um produto já cadastrado
'''
def atualizar_estoque():
    while True:
        print('produtos disponiveis', lista)
        print('digite fim para terminar')
        produto = input('digite o produto que deseja alterar:')
        if produto == 'fim':
            break
        if produto in lista:
            nova_qtd = int(input('digite a nova quantidade:'))
            lista [produto] = nova_qtd
            print('atualizaçao')
            print(lista)
        else:
            print('produto nao encontrado no estoque')
atualizar_estoque()
