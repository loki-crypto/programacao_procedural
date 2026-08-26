# Sistema de Controle de Estoque

Atividade prática de **Programação Procedural**. Sistema de controle de estoque
em Python puro, rodando no terminal: sem classes e sem bibliotecas externas, só
funções, listas e dicionários.

## Como rodar

Precisa apenas de Python 3 instalado.

```bash
python3 menu.py
```

## Menu

```
===== SISTEMA DE ESTOQUE =====

1 - Cadastrar produto
2 - Listar produtos
3 - Buscar produto
4 - Entrada de estoque
5 - Saída de estoque
6 - Mostrar valor total do estoque
7 - Relatórios do estoque
0 - Sair
```

O menu fica repetindo até o usuário escolher a opção **0**.

## Estrutura

```
menu.py        # ponto de entrada: menu principal e conversa com o usuário
estoque.py     # lista inicial de produtos e a constante ESTOQUE_BAIXO
cadastrar.py   # cadastro de produto novo, com as validações
listar.py      # texto com todos os produtos
buscar.py      # busca de produto pelo nome
movimentar.py  # entrada e saída de unidades
valor.py       # cálculo do valor do estoque
relatorios.py  # relatórios extras (desafio adicional)
formatar.py    # formatação de dinheiro no padrão brasileiro
```

Cada produto é um dicionário com **nome, preço e quantidade**:

```python
{"produto": "10g Puro", "valor": 20, "qtd": 10}
```

Todos eles ficam guardados em uma **lista** (`estoque`), que é passada como
parâmetro para as funções.

## Explicação das funções

### Funcionalidades obrigatórias

**`cadastrar_produto(estoque, nome, valor, qtd)`** — [cadastrar.py](cadastrar.py)
Adiciona um produto novo à lista. Antes disso valida quatro coisas: o nome não
pode estar em branco, o produto não pode já existir, o preço não pode ser
negativo e a quantidade também não. Devolve `(deu_certo, mensagem)`.

**`listar_produtos(estoque)`** — [listar.py](listar.py)
Percorre a lista com um `for` e monta um texto numerado com nome, preço e
quantidade de cada produto. Se o estoque estiver vazio, avisa isso.

**`buscar_produto(estoque, nome)`** — [buscar.py](buscar.py)
Procura um produto pelo nome, ignorando maiúsculas/minúsculas e espaços sobrando
(`"  MOUSE "` acha `"Mouse"`). Devolve o dicionário do produto, ou `None` se não
encontrar. É reaproveitada pelo cadastro e pelas movimentações.

**`entrada_estoque(estoque, nome, qtd)`** — [movimentar.py](movimentar.py)
Soma unidades a um produto que já existe. Recusa quantidade zero ou negativa, e
recusa produto inexistente.

**`saida_estoque(estoque, nome, qtd)`** — [movimentar.py](movimentar.py)
Retira unidades de um produto. Além das validações da entrada, **não deixa
retirar mais do que a quantidade disponível** — nesse caso devolve
"Estoque insuficiente" e não altera nada.

**`calcular_valor_estoque(estoque)`** — [valor.py](valor.py)
Percorre a lista somando `preço × quantidade` de cada produto e devolve o total.

**`detalhar_valor_estoque(estoque)`** — [valor.py](valor.py)
Monta o texto mostrando o valor de cada produto separadamente e, no fim, o total
geral vindo de `calcular_valor_estoque`.

### Desafio adicional — [relatorios.py](relatorios.py)

**`produto_maior_quantidade(estoque)`** — percorre a lista guardando o produto
com mais unidades e devolve ele.

**`produto_menor_quantidade(estoque)`** — mesma ideia, mas para o de menos
unidades.

**`produto_mais_caro(estoque)`** — devolve o produto de maior preço unitário.

**`listar_estoque_baixo(estoque)`** — monta a lista dos produtos com menos de 5
unidades (a constante `ESTOQUE_BAIXO`, definida em [estoque.py](estoque.py)).

**`montar_relatorios(estoque)`** — junta os quatro relatórios acima em um texto
só, que é o que a opção 7 imprime.

### Apoio

**`main()`** — [menu.py](menu.py)
Dá as boas-vindas, pergunta o nome do usuário e roda o `while` que mostra o menu
até a opção 0 ser escolhida. Cada opção só chama a função responsável por ela.

**`mostrar_menu()`** — imprime o menu e devolve a opção digitada.

**`ler_numero(mensagem, inteiro=True)`** — pede um número e fica repetindo até o
usuário digitar algo válido, evitando que o programa quebre com letras. Aceita
vírgula como separador decimal.

**`opcao_cadastrar`, `opcao_buscar`, `opcao_entrada`, `opcao_saida`** — cada uma
cuida de perguntar os dados daquela opção e chamar a função correspondente,
para o `while` do `main()` não virar um bloco gigante.

**`formatar_real(valor)`** — [formatar.py](formatar.py)
Converte um número para o padrão brasileiro de moeda (`R$ 1.200,00`).

## Regras da atividade atendidas

- Uso de funções, com **uma responsabilidade cada** ✔
- Parâmetros em **todas** as funções principais ✔
- `return` em todas as funções dos módulos ✔
- **Lista** para armazenar os dados ✔
- Estruturas **condicionais** (`if/elif/else`) e de **repetição** (`while`, `for`) ✔
- Menu principal em loop até a opção 0 ✔
- Mais de seis funções (são 20) ✔
- Saída de estoque bloqueada quando a quantidade é maior que a disponível ✔

## Observações

Os dados ficam só na memória: ao fechar o programa, tudo volta ao estado inicial
definido em [estoque.py](estoque.py).

## Licença

MIT — veja o arquivo [LICENSE](LICENSE).
