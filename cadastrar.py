from buscar import buscar_produto


def cadastrar_produto(estoque, nome, valor, qtd):
    """Adiciona um produto novo à lista de estoque.

    Devolve uma dupla (deu_certo, mensagem).
    """
    nome = nome.strip()

    if not nome:
        return False, "O nome do produto não pode ficar em branco."
    if buscar_produto(estoque, nome) is not None:
        return False, f"O produto '{nome}' já está cadastrado."
    if valor < 0:
        return False, "O valor não pode ser negativo."
    if qtd < 0:
        return False, "A quantidade não pode ser negativa."

    estoque.append({"produto": nome, "valor": valor, "qtd": qtd})
    return True, f"Produto '{nome}' cadastrado com sucesso."
