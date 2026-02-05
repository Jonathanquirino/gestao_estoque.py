"""
💼 O Pedido do Cliente: "O Sistema de Gerenciamento de Estoque da Padaria"
"Oi, desenvolvedor! Seguinte: eu tenho uma padaria e estou perdendo o controle do que tenho nas prateleiras. Eu preciso que você crie um programa que guarde o nome do produto e a quantidade que eu tenho no estoque.
Mas tem um detalhe:
Eu quero conseguir consultar quanto de 'Pão Francês' eu ainda tenho.
Se eu vender 5 pães, o sistema tem que me deixar atualizar esse valor.
Se eu começar a vender um produto novo (tipo 'Bolo de Cenoura'), eu quero conseguir adicionar ele na lista.
No final do dia, eu quero ver uma lista completa de tudo o que eu tenho e as quantidades."
🎯 Seu Desafio Técnico:
Para resolver isso para mim, você vai precisar usar um dicionário em Python.
Regras do Desafio:
Crie o dicionário com pelo menos 3 produtos iniciais.
Mostre como você atualiza a quantidade de um deles.
Mostre como você adiciona um novo.
Use um laço de repetição (for) para me mostrar o relatório final.

"""
print("-" * 50)
print("Estoque Padaria")
print("-" * 50)

banco_padaria = {}

while True:
    try:
        print("-" * 50)
        digito = int(input(
            "Digite (1) para cadastrar um novo item: \n"
            "Digite (2) para adicionar a um item existente: \n"
            "Digite (3) para remover um item: \n"
            "Digite (4) para consultar saldo do item: \n"
            "Digite (5) para olhar o relatório geral: "
        ))
        if digito == 1:  # Cadastra um novo item
            nome_item = input("Digite o nome do produto ou 'sair' para sair: ").lower().strip()
            if nome_item == "sair":  # Condição para sair
                print("-" * 50)
                print("Saindo do cadastro...")
                print("-" * 50)
                break
            else:
                codigo_produto = int(input("Digite o código do produto: "))
                valor_produto = float(input("Digite o valor do produto: "))
                quantidade_produto = int(input("Digite a quantidade de entrada: "))
                banco_padaria[codigo_produto] = {  # Inicia os dados dentro do banco
                    "codigo": codigo_produto,
                    "nome": nome_item,
                    "valor": valor_produto,
                    "quantidade": quantidade_produto
                }
                nome_produto = banco_padaria[codigo_produto]["nome"]
                print("-" * 50)
                print(f"O Produto {nome_produto} foi cadastrado com sucesso!")
                print("-" * 50)
        elif digito == 2:  # Adicionando quantide
            print("-" * 50)
            adicionar_item = int(input("Digite o código do produto: "))
            print("-" * 50)
            quantidade_adicionar = int(input('Digite a quantidade que pretende adicionar: '))
            print("-" * 50)
            novo_valor = float(input("Digite o valor do produto: "))
            print("-" * 50)
            if adicionar_item in banco_padaria:
                item_adicionar = banco_padaria[adicionar_item]["quantidade"]
                valor_adicionar = banco_padaria[adicionar_item]['valor']
                nome_produto = banco_padaria[adicionar_item]["nome"]
                valor_medio = banco_padaria[adicionar_item]['valor']
                item_adicionado = quantidade_adicionar + item_adicionar
                valor_atualizado = novo_valor * quantidade_adicionar
                valor_novo = valor_adicionar + valor_atualizado
                novo_valor_medio = valor_novo / item_adicionado
                banco_padaria[adicionar_item]["quantidade"] = item_adicionado
                banco_padaria[adicionar_item]["valor"] = valor_novo
                print("-" * 50)
                print(f"O produto {nome_produto}")
                print("-" * 50)
                print(f"Foi alterado para {item_adicionado}")
                print("-" * 50)
                print(f"O valor total é de {valor_novo}")
                print("-" * 50)
                print(f"O novo valor médio do produto é de {novo_valor_medio}")
                print("-" * 50)
            else:
                print("-" * 50)
                print("Item não encontrado")
                print("-" * 50)
        elif digito == 3:  # remoção de quantidades
            print("-" * 50)
            remover_item = int(input("Digite o código do produto: "))
            print("-" * 50)
            quantidade_remover = int(input("Digite a quantidade que deseja remover: "))
            print("-" * 50)
            if remover_item in banco_padaria:
                item_remover = banco_padaria[remover_item]["quantidade"]
                nome_produto = banco_padaria[remover_item]["nome"]
                valor_banco = banco_padaria[remover_item]["valor"]
                nova_quantidade = item_remover - quantidade_remover
                novo_valor_unitario = valor_banco / item_remover
                valor_remover = novo_valor_unitario * quantidade_remover
                novo_valor_remover = valor_banco - valor_remover
                banco_padaria[remover_item]["quantidade"] = nova_quantidade
                banco_padaria[remover_item]["valor"] = novo_valor_remover
                print("-" * 50)
                print(f"A quantidade do produto {nome_produto}")
                print("-" * 50)
                print(f"Foi atualizada para {nova_quantidade} com sucesso!")
                print("-" * 50)
                print(f"Novo valor geral de {novo_valor_remover}")
                print("-" * 50)
            else:
                print("-" * 50)
                print("Item não encontrado")
                print("-" * 50)
        elif digito == 4:  # Consulta de produtos
            print("-" * 50)
            consulta_produto = int(input("Digite o código do produto: "))
            if consulta_produto in banco_padaria:
                print("-" * 50)
                consulta_nome = banco_padaria[consulta_produto]['nome']
                consulta_quantidade = banco_padaria[consulta_produto]["quantidade"]
                consulta_valor = banco_padaria[consulta_produto]["valor"]
                print("-" * 50)
                print(f"O saldo do item {consulta_nome}")
                print("-" * 50)
                print(f"é de {consulta_quantidade}")
                print("-" * 50)
                print(f"avaliado em {consulta_valor}")
                print("-" * 50)
            else:
                print("Item não encontrado")
        elif digito == 5:  # Consulta saldo geral
            print("-" * 50)
            for codigo in banco_padaria:
                p = banco_padaria[codigo]
                print(f"Produto: {p['nome']} | Quantidade: {p['quantidade']} | Valor: {p['valor']}")
            print("-" * 50)
    except ValueError:
        print("-" * 50)
        print("Digite um caractér válido!")
        print("-" * 50)
