''' Calculadora While '''
while True:

    numero_1 = (input('Digite o primeiro número: '))
    numero_2 = (input('Digite o segundo número: '))
    operador = input('Digite o operador ( + - * / ): ')
    print('-----------------------------------------------')

#-----------------------------------------------
# Declaração de variáveis - flag para o loop    
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
#-----------------------------------------------
# Tentar converter os números para float
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)   
# Se der certo, numeros_validos recebe True
        numeros_validos = True  
# No except, vou garantir que numeros_validos continue sendo None.
    except:
        numeros_validos = None 
#-----------------------------------------------
# Volta para o início do loop caso algum número seja inválido.
    if numeros_validos is None:
        print('Você digitou algum número inválido!')
        continue            
#----------------------------------------------- 
# Condições para os operador       
    operadores_permitidos = '+-*/'
    if operador not in operadores_permitidos:
        print('Operador inválido!')
        continue

    if len(operador) > 1:
         print('Digite apenas um operador!')
         continue  
#-----------------------------------------------
# Operação 
    print('Realizando seu cálculo! Confira o resultado abaixo: ')
    print('-----------------------------------------------')
    if operador == '+':
        print(f'{num_1_float:.2f} + {num_2_float:.2f} =',num_1_float + num_2_float)
    elif operador =='-' :   
        print(f'{num_1_float:.2f} - {num_2_float:.2f} =',num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float:.2f} / {num_2_float:.2f} =',num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float:.2f} * {num_2_float:.2f} =',num_1_float * num_2_float)
    else:
        print('Calculo inválido!')
    print('-----------------------------------------------')

#-----------------------------------------------
# Saída do programa  
# Função lower() converte a string para minúscula   
# Função startswith() verifica se a string começa com o caractere passado ('s')    
    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    print(sair)

    if sair:
        break