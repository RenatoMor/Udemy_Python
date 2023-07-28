"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
condicao = True
# Enquanto o valor da variável for verdadeiro, o loop será executado
while condicao:
    nome = input('Qual o seu nome: ')
    print(f'Seu nome é {nome}')
# condicao = False
    if nome == 'sair':
        break

print('Acabou')