def formatar_real(valor):
    """Formata um número no padrão brasileiro de moeda: R$ 1.200,00."""
    texto = f"{valor:,.2f}"
    return "R$ " + texto.replace(",", "#").replace(".", ",").replace("#", ".")
