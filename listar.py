from formatar import formatar_real


def listar_produtos(estoque):
    """Monta o texto com todos os produtos do estoque.

    Devolve uma string pronta para o menu imprimir.
    """
    if not estoque:
        return "O estoque está vazio."

    linhas = ["Produtos em estoque:"]
    for numero, item in enumerate(estoque, start=1):
        linhas.append(
            f"{numero}. {item['produto']} - {formatar_real(item['valor'])} - "
            f"{item['qtd']} unidade(s)."
        )
    return "\n".join(linhas)
