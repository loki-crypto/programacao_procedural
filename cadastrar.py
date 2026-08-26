from buscar import buscar


def cadastrar(estoque, nome, valor, qtd):
    nome = nome.strip()

    if not nome:
        return False, "O nome do produto não pode ficar em branco."
    if buscar(estoque, nome) is not None:
        return False, f"O produto '{nome}' já está cadastrado."
    if valor < 0:
        return False, "O valor não pode ser negativo."
    if qtd < 0:
        return False, "A quantidade não pode ser negativa."

    estoque.append({"produto": nome, "valor": valor, "qtd": qtd})
    return True, f"Produto '{nome}' cadastrado com sucesso."
