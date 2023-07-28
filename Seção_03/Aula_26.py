"""
Formatação básica de f-Strings
s - string
d e int = int
f - float
x e X - hexadecimal (ABCDEF0123456789)
(Caractere) (>< ^) (quantidade) 
> - Esquerda
< - Direita
^ - Centro
= - Força o número aparecer antes dos zeros
Sinal - + ou -
Ex.: 0 >-  100, .1f
Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel:#^10}')
print(f'{1000.4852136526656:0=+10,.1f}')
print(f'O hexadecimal de 1500 é{1500:08X}')
print(f'{variavel!r}')