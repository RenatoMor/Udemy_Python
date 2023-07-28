# Quando o argumento é *
def multiplicar(*args):
    total = 1

    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(2,4,7,3,5)
print(multiplicacao)

#-----------------------------------------------

def par_impar(numero):
    multiplos_de_dois = numero % 2 == 0

    if multiplos_de_dois:
        return f'{numero} é PAR!'
    return f'{numero} é ÍMPAR!'
numero = int(input('Informe o número: '))

def main():
    resultado = par_impar(numero)
    print('O número', resultado)

main()

    





     