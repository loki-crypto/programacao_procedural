from buscar import buscar_produto


def entrada_estoque(estoque, nome, qtd):
    """Soma unidades a um produto que já existe no estoque.

    Devolve uma dupla (deu_certo, mensagem).
    """
    if qtd <= 0:
        return False, "A quantidade da entrada precisa ser maior que zero."

    item = buscar_produto(estoque, nome)
    if item is None:
        return False, f"Produto '{nome}' não encontrado no estoque."

    item["qtd"] += qtd
    return True, f"Entrada registrada. '{item['produto']}' agora tem {item['qtd']} unidade(s)."


def saida_estoque(estoque, nome, qtd):
    """Retira unidades de um produto que já existe no estoque.

    Não permite retirar mais do que a quantidade disponível.
    Devolve uma dupla (deu_certo, mensagem).
    """
    if qtd <= 0:
        return False, "A quantidade da saída precisa ser maior que zero."

    item = buscar_produto(estoque, nome)
    if item is None:
        return False, f"Produto '{nome}' não encontrado no estoque."

    if qtd > item["qtd"]:
        return False, (
            f"Estoque insuficiente: existem apenas {item['qtd']} "
            f"unidade(s) de '{item['produto']}'."
        )

    item["qtd"] -= qtd
    return True, f"Saída registrada. '{item['produto']}' agora tem {item['qtd']} unidade(s)."
