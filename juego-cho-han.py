"""
"Cho Han"

El juego tradicional japones "Cho han" consiste en el lanzamiento de 2 dados en un vaso para luego colocarlo sobre el suelo con la abertura hacia abajo, ocultando los dados. Los jugadores deben de adivinar si la suma de los dados da cho (par) o Han (impar).
Simule el juego "Cho Han" en python donde el un jugador ingresara cuanto dinero desea apostar en cada turno (asuma que el jugador comienza con $10 en su billetera)
    Si adivina: Gana el doble de lo que aposto, por ejemplo: si en la billetera tiene $10 y apuesta $2, entonces tendra $12 
    Si no adivina: pierde lo que aposto por ejemplo: si en la billetera tiene $10 y apuesta $2 entonces tendra $8 
    
El juego termina cuando el usuario se queda sin dinero o ingrese que no desea continuar 
Se debera mostrar el resultado de cada ronda, el dinero que tiene en la billetera y al finalizar todas las rondas se debera mostrar la cantidad de partidas que gano el jugador
"""
import random as rd

billeteraJugador = 10
partidasGanadas = 0
condicionJugador = "si"

while billeteraJugador > 0 and condicionJugador.startswith("s"):
    
    print("\nBienvenido al Juego de Cho Han")
    
    print("\nEn la Billetera Tiene: {}$".format(billeteraJugador))
    
    apuestaJugador = int(input("\nIngrese Cuanto Dinero desea Apostar: "))
    
    if apuestaJugador <= billeteraJugador and apuestaJugador > 0:
        
        dado1 = rd.randint(1,6)
        dado2 = rd.randint(1,6)
        sumaDados = dado1 + dado2
        
        print("\nAdivine la Suma de los 2 Dados")
        
        desicionJugador = input("\nLa suma de los 2 dados es Par o Impar?: ").lower()
        
        if sumaDados%2 == 0 and desicionJugador == "par":
            
            print("\nLa suma de: {} + {} = {}".format(dado1, dado2, sumaDados))
            
            print("\nHa Adivinado, el Numero es Par")
            
            billeteraJugador += apuestaJugador
            
            partidasGanadas += 1
            
        elif sumaDados%2 != 0 and desicionJugador == "impar":
            
            print("\nLa suma de: {} + {} = {}".format(dado1, dado2, sumaDados))
            
            print("\nHa adivinado, el Numero es impar")
            
            billeteraJugador += apuestaJugador
            
            partidasGanadas += 1
            
        else:
            
            print("\nLa suma de: {} + {} = {}".format(dado1, dado2, sumaDados))
            
            print("\nNo ha adivinado el Numero.... Ha perdido")
            
            billeteraJugador -= apuestaJugador
            
        if billeteraJugador != 0:
            
            condicionJugador = input("\nDesea Volver a Jugar? Si(si) o No(no): ")
        
    else:
        
        print("\nNo posee Dinero Suficiente en la cuenta")
            
else:
    
    print("\nGano: {} veces".format(partidasGanadas))
    
    print("\nGracias Por Jugar\n")