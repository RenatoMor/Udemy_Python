"""
! Operador in e not in
Strings são iteráveis
0 1 2 3 4 5 
R e n a t o
-6 -5 -4 -3 -2 -1
"""
# nome = 'Renato'
# print(nome[2])
# print(nome[-4])
# print('t' in nome)
# print('z' in nome) 
# print(10 * '-')
# print('to' in nome)
# print('rio' in nome)
# print(10 * '-')
# print('to' not in nome)
# print('rio' not in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')   

if encontrar in nome:
    print(f'{encontrar} está em {nome}')  
else:
    print(f'{encontrar} não está em {nome}')

# nome = 'Maria Carmo'
 
# if ' ' in nome:
#     print(f'O nome {nome} tem espaços.')
# else:
#     print(f'O nome {nome} NÃO tem espaços.')