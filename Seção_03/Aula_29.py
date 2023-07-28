"""
?nome = input('Digite seu nome: ').strip()
?idade = input('Digite sua idade: ')   

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    #!  print(f'Seu nome contém (ou não) espaços: {nome.isspace()}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')   
else:
    print('Preencha todos os campos!')
"""
nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print('Seu nome é: {}'.format(nome)) 
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')   
    print('Seu nome invertido é: {}'.format(nome[::-1]))       
    print('Seu nome tem {} letras'.format(len(nome)))   
    print('A primeira letra do seu nome é: {}'.format(nome[0]))
    print('A última letra do seu nome é: {}'.format(nome[-1]))
else:   
    print('Preencha todos os campos!')