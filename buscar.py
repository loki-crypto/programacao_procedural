def buscar(estoque, nome):
    nome = nome.strip().lower()
    for item in estoque:
        if item["produto"].lower() == nome:
            return item
    return None
