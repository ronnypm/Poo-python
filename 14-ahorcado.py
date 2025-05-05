print('Bienvenid al juego del ahorcado.\n')

def numero_intentos():

    intentos = int(input('Ingrese el numero de intentos: '))

    if intentos <= 0 :
        print('No puede ingresar un numro menor a 1')


    return intentos


numero_intentos()
