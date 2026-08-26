# Procedural_prog — Controle de Estoque

Sistema simples de controle de estoque feito em Python puro, rodando no terminal.
Projeto da disciplina de Programação Procedural: sem classes, sem bibliotecas
externas, só funções e listas de dicionários.

## Como rodar

Precisa apenas de Python 3 instalado.

```bash
python3 menu.py
```

## O que dá pra fazer

| Opção | Ação |
|-------|------|
| 1 | Cadastrar um produto novo |
| 2 | Listar todos os produtos |
| 3 | Buscar um produto pelo nome |
| 4 | Dar entrada de unidades no estoque |
| 5 | Dar saída de unidades do estoque |
| 6 | Calcular o valor total do estoque |
| 7 | Sair |

## Estrutura

```
menu.py        # ponto de entrada: menu interativo e leitura das opções
estoque.py     # lista inicial de produtos (dados em memória)
cadastrar.py   # cadastro de produto novo, com as validações
listar.py      # monta o texto com todos os produtos
buscar.py      # busca de produto pelo nome (ignora maiúsculas/minúsculas)
movimentar.py  # entrada() e saida() de unidades
valor.py       # valor_total() do estoque
```

Cada produto é um dicionário no formato:

```python
{"produto": "10g Puro", "valor": 20, "qtd": 10}
```

As funções que alteram o estoque devolvem uma dupla `(deu_certo, mensagem)`,
para o `menu.py` só precisar imprimir a mensagem.

## Observações

- Os dados ficam só na memória: ao fechar o programa, tudo volta ao estado
  inicial definido em `estoque.py`.

## Licença

MIT — veja o arquivo [LICENSE](LICENSE).
