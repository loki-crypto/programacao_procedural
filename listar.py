def listar(estoque):
    if not estoque:
        return "O estoque está vazio."

    linhas = ["Produtos em estoque:"]
    for numero, item in enumerate(estoque, start=1):
        linhas.append(
            f"{numero}. {item['produto']} - R$ {item['valor']:.2f} - "
            f"{item['qtd']} unidade(s)."
        )
    return "\n".join(linhas)
