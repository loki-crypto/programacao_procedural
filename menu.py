from estoque import estoque
from cadastrar import cadastrar_produto
from listar import listar_produtos
from buscar import buscar_produto
from movimentar import entrada_estoque, saida_estoque
from valor import detalhar_valor_estoque
from relatorios import montar_relatorios
from formatar import formatar_real


def ler_numero(mensagem, inteiro=True):
    """Pede um número ao usuário e só devolve quando ele digitar algo válido."""
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            if inteiro:
                return int(texto)
            return float(texto)
        except ValueError:
            print("Valor inválido, digite apenas números.")


def mostrar_menu():
    """Exibe o menu principal e devolve a opção escolhida pelo usuário."""
    return input(
        "\n"
        "===== SISTEMA DE ESTOQUE =====\n"
        "\n"
        "1 - Cadastrar produto\n"
        "2 - Listar produtos\n"
        "3 - Buscar produto\n"
        "4 - Entrada de estoque\n"
        "5 - Saída de estoque\n"
        "6 - Mostrar valor total do estoque\n"
        "7 - Relatórios do estoque\n"
        "0 - Sair\n"
        "\n"
        "Qual a sua escolha (obs: coloque apenas numeros): "
    ).strip()


def opcao_cadastrar(estoque):
    """Pergunta os dados do produto novo e manda cadastrar."""
    nome = input("Qual o nome do seu novo produto: ")
    valor = ler_numero("Qual o valor do novo produto: ", inteiro=False)
    qtd = ler_numero("Quantas unidades você tem: ")

    deu_certo, mensagem = cadastrar_produto(estoque, nome, valor, qtd)
    print(mensagem)


def opcao_buscar(estoque):
    """Pergunta o nome e mostra o produto, se ele existir."""
    busca = input("Qual o produto que quer procurar: ")
    item = buscar_produto(estoque, busca)

    if item is None:
        print(f"O produto '{busca}' não está no estoque.")
    else:
        print(
            f"Seu item está em estoque!! "
            f"{item['produto']} - {formatar_real(item['valor'])} - "
            f"{item['qtd']} unidade(s)."
        )


def opcao_entrada(estoque):
    """Pergunta o produto e a quantidade que entrou."""
    produto = input("Em qual produto quer dar entrada: ")
    qtd = ler_numero("Quantas unidades entraram: ")

    deu_certo, mensagem = entrada_estoque(estoque, produto, qtd)
    print(mensagem)


def opcao_saida(estoque):
    """Pergunta o produto e a quantidade que saiu."""
    produto = input("De qual produto quer dar saída: ")
    qtd = ler_numero("Quantas unidades saíram: ")

    deu_certo, mensagem = saida_estoque(estoque, produto, qtd)
    print(mensagem)


def main():
    """Ponto de entrada: mostra o menu até o usuário escolher a opção 0."""
    print("Olá amigo!! bem vindo ao estoque pessoal do luis")
    nome = input("Para começar insira o seu nome aqui: ")
    print(f"Olá {nome}!!, como vai o dia??, as opções sao as seguintes")

    while True:
        escolha = mostrar_menu()

        if escolha == "1":
            opcao_cadastrar(estoque)
        elif escolha == "2":
            print(listar_produtos(estoque))
        elif escolha == "3":
            opcao_buscar(estoque)
        elif escolha == "4":
            opcao_entrada(estoque)
        elif escolha == "5":
            opcao_saida(estoque)
        elif escolha == "6":
            print(detalhar_valor_estoque(estoque))
        elif escolha == "7":
            print(montar_relatorios(estoque))
        elif escolha == "0":
            print(f"Até mais, {nome}!! Volte sempre.")
            break
        else:
            print("Opção inválida, escolha um número de 0 a 7.")


if __name__ == "__main__":
    main()
