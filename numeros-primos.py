"""
Cree un programa que permita identificar si un numero ingresado por el usuario es primo

Un numero primo es:
    - Un numero natural
    - Mayor que 1
    - Divisible solo para si mismo y para 1
"""

evaluarNumero = int(input("Ingrese un Numero: "))

if evaluarNumero > 1:
    
    contadorNumPrimo = 0
    i = 2
    
    while i < evaluarNumero and contadorNumPrimo == 0:
        
        restoNumero = evaluarNumero%i
        
        print(restoNumero)
        
        if restoNumero == 0:
            
            contadorNumPrimo += 1
            
        i += 1
        
    if contadorNumPrimo == 0:
        
        print("El numero {} es un numero Primo".format(evaluarNumero))
        
    else:
        
        print("El numero {} no es un numero Primo".format(evaluarNumero))         
        
else:
    
    print("El {} no es un numero primo".format(evaluarNumero))