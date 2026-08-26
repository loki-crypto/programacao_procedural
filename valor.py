def valor_total(estoque):
    total = 0
    for item in estoque:
        total += item["valor"] * item["qtd"]
    return total
