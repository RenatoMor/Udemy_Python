"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
qtd_linhas = 5
qtd_colunas = 3

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
# f-string -> Formatação de string
# {linha=} -> = Adiciona o valor da variável linha na string
        print(f'{linha=} - {coluna=}')
        coluna += 1
    linha += 1


print('Acabou')