"""
Iternado strings com while
"""

nome = 'Renato Moreira'
# indice, acumula o valor de cada letra todas as vezes que o loop é executado
indice = 0
# novo_nome, acumula o valor de cada letra e o asterisco todas as vezes que 
# o loop é executado
novo_nome = ''
while indice < len(nome):    
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1
novo_nome += '*'
print(novo_nome)
