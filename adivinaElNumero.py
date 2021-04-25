#Este el es juego de adivinar el numero
import random #importamos el modulo random el cual genera un numero aleatorio para que el usuario adivine

intentosRealizados = 0 #aqui guardamos los intentos del usuario

print('¿Hola como es tu nombre?: ')
miNombre = input() #Aqui le decimos al usuario que ingresa su nombre

numero = random.randint(1, 100) #rango del numero
print('Bueno ' + miNombre + ' Estoy pensando en un numero entre 1 y 100')
print('Solo posees 5 intentos...Usalos Sabiamente...')

while intentosRealizados < 5: #solo tenemos 6 intentos

    print('Intenta adivinar: ')
    estimacion = input() #colocamos el numero y lo guardamos en la variable
    estimacion = int(estimacion) #luego lo pasamos a numero entero

    intentosRealizados = intentosRealizados + 1 #sumamos los intenos porque si no se vuelve un bucle infinito

    if estimacion < numero:
        print('Upss Es muy bajo')

    if estimacion > numero:
        print('Te pasaste xd')

    if estimacion == numero:
        break #si el numero es igual lo tranca aqui y sigue a la siguiente sentencia del codigo

if estimacion == numero:
    intentosRealizados = str(intentosRealizados) #str transforma los numeros a caracter para ser mostrados por la pantalla
    print('Lo lograste ' + miNombre + ' Has adivinado el numero en ' + intentosRealizados + ' intentos')

if estimacion != numero:
    numero = str(numero)
    print('No lo lograste, el numero en que pensaba era: ' + numero)