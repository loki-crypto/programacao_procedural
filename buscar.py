def buscar_produto(estoque, nome):
    """Procura um produto pelo nome, ignorando maiúsculas e espaços.

    Devolve o dicionário do produto ou None se não encontrar.
    """
    nome = nome.strip().lower()
    for item in estoque:
        if item["produto"].lower() == nome:
            return item
    return None
