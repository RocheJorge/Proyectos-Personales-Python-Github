import random #importando los modulos, la funcion random provera la funcion random.randint()
import time #importamos el modulo tiempo que nos dara segundos, minutos, horas
#se crea la funcion que sera llamada mas adelante en el programa
#ojo: las funciones tienen que ser definidas antes de ser llamadas
def mostrarIntroduccion(): 
    print('Estas en una tierra llena de dragones. Frente a ti')
    print('Hay dos cuevas. En una de ellas, el dragon es generoso y')
    print('amigable y compartira su tesoro contigo. El otro dragon')
    print('es codicioso y esta hambriento, y te devorara inmediatamente')
    print()
#esta funcion asegura que el jugadora haya respondido 1 o 2 y no otra cosa. Seguira ejecutandose hasta que el jugador ingrese 1 o 2, esto se llama: validacion de entrada
def elegirCueva():
    cueva='' #esta variable guarda una cadena vacia
    while cueva != '1' and cueva !='2':
        print('¿A cual quieres entrar? (1 o 2)')
        cueva = input()

    return cueva #retorna el valor que le asignemos y se pasara como
    
def explorarCueva(cuevaElegida):
    print('Te aproximas a la cueva....')
    time.sleep(2) #2 segundos
    print('Es oscura y espeluznante....')
    time.sleep(2)
    print('Un dragon aparece subitamente frente a ti! Abre su boca')
    print()
    time.sleep(2)
#decidiendo que cueva tiene el dragon amigable
    cuevaAmigable = random.randint(1, 2)

    if cuevaElegida == str(cuevaAmigable):
        print('Te regala un tesoro')
    else:
        print('Te come')

jugarDeNuevo = 'si'
while jugarDeNuevo == 'si' or jugarDeNuevo == 's':

    mostrarIntroduccion()
    
    numeroDeCueva = elegirCueva()

    explorarCueva(numeroDeCueva)

    print('Quieres jugar de nuevo? (si o no)')
    jugarDeNuevo = input()