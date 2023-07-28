"""
Interpolação básica de Strings
s - string
d e int = int
f - float
x e X - hexadecimal (ABCDEF0123456789)
"""
nome = 'Renato'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel) 
print('O hexadecimal de %d é %x' % (15, 15))
print('O hexadecimal de %d é %04x' % (15, 15))
print('O hexadecimal de %d é %08X' % (1500, 15))
print('O hexadecimal de %d é %04X' % (15, 15))