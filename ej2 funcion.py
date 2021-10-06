# Solicitar números al usuario hasta que ingrese el cero.
# Por cada uno, mostrar la suma de sus dígitos (utilizando una función que realice dicha suma).

def funcion(num):
    while num != 0:
        suma = num + num
        print('La suma del número mas el mismo número es:', suma)
        num = int(input('Ingrese un número: '))
    else:
        return 'Fin del programa.'



print(funcion(int(input('Ingrese un número: '))))