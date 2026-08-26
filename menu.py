from estoque import estoque
from cadastrar import cadastrar
from listar import listar
from buscar import buscar
from movimentar import entrada, saida
from valor import valor_total


def ler_numero(mensagem, inteiro=True):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            if inteiro:
                return int(texto)
            return float(texto)
        except ValueError:
            print("Valor inválido, digite apenas números.")


def mostrar_menu():
    return input(
        "\n"
        "(1) Cadastrar produtos \n"
        "(2) Listar todos os produtos \n"
        "(3) Buscar um produto pelo nome \n"
        "(4) Realizar entrada de estoque \n"
        "(5) Realizar saída de estoque \n"
        "(6) Calcular o valor total do estoque \n"
        "(7) Sair do sistema \n"
        "\n"
        "Qual a sua escolha (obs: coloque apenas numeros): "
    ).strip()


print("Olá amigo!! bem vindo ao estoque pessoal do luis")
nome = input("Para começar insira o seu nome aqui: ")
print(f"Olá {nome}!!, como vai o dia??, as opções sao as seguintes")

while True:
    escolha = mostrar_menu()

    if escolha == "1":
        novo_produto = input("Qual o nome do seu novo produto: ")
        novo_valor = ler_numero("Qual o valor do novo produto: ", inteiro=False)
        nova_qtd = ler_numero("Quantas unidades você tem: ")

        deu_certo, mensagem = cadastrar(estoque, novo_produto, novo_valor, nova_qtd)
        print(mensagem)

    elif escolha == "2":
        print(listar(estoque))

    elif escolha == "3":
        busca = input("Qual o produto que quer procurar: ")
        item = buscar(estoque, busca)

        if item is None:
            print(f"O produto '{busca}' não está no estoque.")
        else:
            print(
                f"Seu item está em estoque!! "
                f"{item['produto']} - R$ {item['valor']:.2f} - {item['qtd']} unidade(s)."
            )

    elif escolha == "4":
        produto = input("Em qual produto quer dar entrada: ")
        qtd = ler_numero("Quantas unidades entraram: ")

        deu_certo, mensagem = entrada(estoque, produto, qtd)
        print(mensagem)

    elif escolha == "5":
        produto = input("De qual produto quer dar saída: ")
        qtd = ler_numero("Quantas unidades saíram: ")

        deu_certo, mensagem = saida(estoque, produto, qtd)
        print(mensagem)

    elif escolha == "6":
        print(f"O valor total do seu estoque é de R$ {valor_total(estoque):.2f}.")

    elif escolha == "7":
        print(f"Até mais, {nome}!! Volte sempre.")
        break

    else:
        print("Opção inválida, escolha um número de 1 a 7.")
