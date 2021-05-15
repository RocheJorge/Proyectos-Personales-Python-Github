"""
Cree un programa que simule el juego del ahorcado,
su programa debe seleccionar una palabra aleatoria de una lista de palabras,
ejemplo si la palabra es "POLLOS" entonces muestre una lista "P_ _ _ _ S"
El usuario debe ingresar una palabra y si es igual a la palabra aleatoria
entonces el programa mostrara True, caso contrario False
"""
import random as rd

palabrasAhorcado = ["Capuchino", "Cafe", "Oreo", "Pollos", "Programacion"]

longitudPalabras = len(palabrasAhorcado) # 5
#print(longitudPalabras)

#                                      4
indicePalabras = rd.randint(0, longitudPalabras - 1) # 0 1 2 3 4
#print(indicePalabras)

mostrarPalabra = palabrasAhorcado[indicePalabras] # Pollos
#print(mostrarPalabra)

mostrarPalabraMayuscula = mostrarPalabra.upper() # "POLLOS"
#print(mostrarPalabraMayuscula)

########## mostrar primera y ultima letra solamente

primeraLetraPalabra = mostrarPalabraMayuscula[0] # P
#print(primeraLetraPalabra)

ultimaLetraPalabra = mostrarPalabraMayuscula[-1] # S
#print(ultimaLetraPalabra)

########## Mostrar guiones al usuario

n = len(mostrarPalabraMayuscula) - 2
#print(n)

subGuionesPalabra = n * " _ " # cuando se multiplica una cadena con una cadena, la cadena se repite n veces

pista = primeraLetraPalabra + subGuionesPalabra + ultimaLetraPalabra
print(pista)

########## Mostrar al usuario si adivino la palabra

palabraUsuario = input("Adivine la Palabra: ").upper()

if palabraUsuario == mostrarPalabraMayuscula:
    
    print("Felicidades ha Adivinado la Palabra")
    
else:
    
    print("No ha Logrado Adivinar la Palabra Intente de Nuevo....")