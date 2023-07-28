"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
# O contador vale 0, então a condição é verdadeira e o loop é executado
contador = 0
# O contador vale 0, então a condição é verdadeira e o loop é executado
# O contador é incrementado em 1, e o loop é executado novamente
# O contador continua sendo incrementado até que a condição seja falsa
# ou seja, até que o contador seja maior que 10.
while contador <= 10:
# O contador é incrementado em 1, e o loop é executado novamente
    contador = contador + 1
# Se eu inverter a ordem do print e do contador, o contador será incrementado
# antes de ser impresso, e o valor impresso será 1 a mais que o valor do contador
    print(contador)

print('Acabou')