from estoque import ESTOQUE_BAIXO
from formatar import formatar_real


def produto_maior_quantidade(estoque):
    """Devolve o produto com mais unidades em estoque (ou None se vazio)."""
    if not estoque:
        return None

    maior = estoque[0]
    for item in estoque:
        if item["qtd"] > maior["qtd"]:
            maior = item
    return maior


def produto_menor_quantidade(estoque):
    """Devolve o produto com menos unidades em estoque (ou None se vazio)."""
    if not estoque:
        return None

    menor = estoque[0]
    for item in estoque:
        if item["qtd"] < menor["qtd"]:
            menor = item
    return menor


def produto_mais_caro(estoque):
    """Devolve o produto de maior preço unitário (ou None se vazio)."""
    if not estoque:
        return None

    caro = estoque[0]
    for item in estoque:
        if item["valor"] > caro["valor"]:
            caro = item
    return caro


def listar_estoque_baixo(estoque):
    """Monta o texto com os produtos que têm menos de ESTOQUE_BAIXO unidades."""
    baixos = []
    for item in estoque:
        if item["qtd"] < ESTOQUE_BAIXO:
            baixos.append(item)

    if not baixos:
        return f"Nenhum produto com menos de {ESTOQUE_BAIXO} unidades."

    linhas = [f"Produtos com estoque baixo (menos de {ESTOQUE_BAIXO} unidades):"]
    for item in baixos:
        linhas.append(f"- {item['produto']}: {item['qtd']} unidade(s).")
    return "\n".join(linhas)


def montar_relatorios(estoque):
    """Junta os quatro relatórios extras em um texto só."""
    if not estoque:
        return "O estoque está vazio, não há relatórios para mostrar."

    maior = produto_maior_quantidade(estoque)
    menor = produto_menor_quantidade(estoque)
    caro = produto_mais_caro(estoque)

    return "\n".join([
        f"Maior quantidade: {maior['produto']} ({maior['qtd']} unidade(s)).",
        f"Menor quantidade: {menor['produto']} ({menor['qtd']} unidade(s)).",
        f"Produto mais caro: {caro['produto']} ({formatar_real(caro['valor'])}).",
        "",
        listar_estoque_baixo(estoque),
    ])
