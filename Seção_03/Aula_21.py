"""
!  Operadores Lógicos
? and (e) or (ou) not (não)
* and 
Todas as condições precisam ser verdadeiras
Se qualquer valor for considerado falso, a expressão
inteira será avaliada naquele valor.
São consideradas falsy 0 0.0 '' False
Também existe o tipo none usado para representar 
um valor não.
"""
# entrada = input('[E]ntrada [S]air: ')
# senha_digitada = input(' Digite a senha: ')
# senha_permitida = '221267'
# if entrada == 'E' and senha_digitada == senha_permitida:
#     print('Entrar')
# elif senha_permitida != senha_digitada:
#     print('Senha inválida')
# else:
#     print('Sair')

# Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)
print(bool(0))
print(bool('')) # string vazia tb é False
print(bool(' ')) # string com espaço é True pq não é considerada vazia