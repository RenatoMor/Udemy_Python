"""
' Argumentos nomeados e não nomeados em funções Python
* Argumento nomeado tem nome com sinal de igual
* Argumento não nomeado recebe apenas o argumento (valor)
|----------------Parâmetro e Argumento-------------------
#! Parâmetro é a variável que recebe o argumento.
#! Argumento é o valor passado para o parâmetro que é uma variável.
"""
def soma(x, y, z):
    # Definição
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)


soma(1, 2, 3)
#! Argumentos nomeados = nome do parâmetro junto com o argumento
soma(1, y=2, z=5)
#! sep - separador
print(1, 2, 3, sep='-') 