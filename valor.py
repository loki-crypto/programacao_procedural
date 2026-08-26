from formatar import formatar_real


def calcular_valor_estoque(estoque):
    """Soma preço x quantidade de todos os produtos.

    Devolve o valor total do estoque.
    """
    total = 0
    for item in estoque:
        total += item["valor"] * item["qtd"]
    return total


def detalhar_valor_estoque(estoque):
    """Monta o texto com o valor de cada produto e o total geral.

    Devolve uma string pronta para o menu imprimir.
    """
    if not estoque:
        return "O estoque está vazio. Valor total: " + formatar_real(0)

    linhas = []
    for item in estoque:
        subtotal = item["valor"] * item["qtd"]
        linhas.append(f"{item['produto']}: {formatar_real(subtotal)}")

    linhas.append("")
    linhas.append(f"Valor total do estoque: {formatar_real(calcular_valor_estoque(estoque))}")
    return "\n".join(linhas)
