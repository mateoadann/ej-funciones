# Requerir al usuario que ingrese un número entero e informar si es primo o no,
# utilizando una función booleana que lo decida.

def primo(num, esPrimo=False):
        if num % num == 0:
            esPrimo = False
            return esPrimo, 'El número no es primo.'
        elif num % num != '0':
            esPrimo = True
            return esPrimo, 'El número es primo.'


print(primo(int(input('Ingrese un número: '))))
