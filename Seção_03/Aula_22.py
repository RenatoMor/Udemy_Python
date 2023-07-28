"""
!  Operadores Lógicos
? and (e) or (ou) not (não)
* or (ou)
Qualquer condição verdadeira avalia
toda a expressão com verdadeira.
Se qualquer expressão for considerada verdadeiro,
a expressão inteira será avaliada naquele valor.
São consideradas falsy 0 0.0 '' False
Também existe o tipo none usado para representar 
um valor não.
"""

# entrada = input('[E]ntradar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '221267'
# if (entrada == 'E' or entrada =='e') and senha_digitada == senha_permitida:   
#     print('Entrar')
# else: 
#     print('Sair')

# Avaliação de curto circuito
print(True or False)
print(True or False or 0)
print(0 or False or 0 or 'ABC')
senha = 0 or False or 0 or 'ABC'
print(senha)
senha = input('Digite a senha: ') or 'senha vazia'
print(senha)