# Solicitar al usuario que ingrese su dirección email. Imprimir un mensaje indicando si la dirección es válida o no,
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".

def validacion(mail):
    for validar in mail:
        if validar != '@':
            continue
        elif validar == '@':
            return print('La dirección de mail es valida.')
        else:
            return print('La dirección es incorrecta. ')



print(validacion(input('Ingrese su correo electrónico: ')))