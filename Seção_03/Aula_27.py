"""
Fatiamento de cordas
012345678
Olá mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd
de caracteres da str
"""
variavel  =  'Olá mundo'
print ( variavel [: 2 ])
print (len( variavel [ 1 : 5 ]))
print ( variavel [ 3 ])
print ( variavel [: 5 ])
print ( variavel [ 5: ])
print ( variavel [ -8 : -2 ])
print (len( variavel [ 3 ]))
print( variavel [0: len(variavel):1])
print( variavel [0: 9: 1])
print( variavel [0: 9: 2])
print( variavel [0: 9: 3])
print( variavel [: : -1]) # Escreve a palavra ao contrário
print( variavel [-1:-10 : -1]) # Escreve a palavra ao contrário