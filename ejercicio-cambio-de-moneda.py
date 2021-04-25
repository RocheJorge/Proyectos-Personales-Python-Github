"""
crear un programa que a traves del uso de funciones puedas efectuar el cambio entre tu moneda local y el dolar y viceversa, de manera que el usuario pueda ingresar la cantidad en cualquiera de las dos monedas y obtener como resultado la respectiva conversion

Realizado por Jorge Roche 24743191
"""

#inicio del programa

print("\nBienvenido al Programa Conversor de Monedas\n")

#declaramos las funciones de las conversiones con parametros con retorno

def bolivaresDolares(a):
    bolivaresDolares = a / 2360816.00
    return bolivaresDolares

def dolaresBolivares(b):
    dolaresBolivares = b * 2360816.00
    return dolaresBolivares

def dolaresPesos(c):
    dolaresPesos = c * 3643.00
    return dolaresPesos

def pesosDolares(d):
    pesosDolares = d / 3643.00
    return pesosDolares

#Le Indicamos al usuario la opcion que desea relizar

print("¿Que Desea Realizar?\n")

print("1: Convertir Bolivares a Dolares\n")
print("2: Convertir Dolares a Bolivares\n")
print("3: Convertir Dolares a Pesos\n")
print("4: Convertir Pesos a Dolares\n")
print("5: Salir\n")

opcionUsuario = int(input("Elija la opcion que desea realizar: ¿1, 2, 3, 4, 5?: "))
print()

while opcionUsuario != 5:

#a traves de la condicional if realizamos las operaciones que el usuario indique

    if opcionUsuario == 1:
        
        a = float(input("Ingrese la Cantidad de Bolivares que desea Convertir: "))
        print()
        
        #llamamos a la funcion para que realize la operacion y retorne el resultado

        montoConvertido = bolivaresDolares(a)
        
        #Convertimos el monto a 2 decimales a traves de la funcion round()
        
        montoRedondeado = round(montoConvertido,2)
        
        #imprimimos el mensaje al usuario y la operacion realizada 
        
        print("1 bolívar venezolano Es igual a 0.00 dólar estadounidense\n")
        
        print("El Monto Fue convertido, el resultado es: ", montoRedondeado,"Dolares")
        
    elif opcionUsuario == 2:
        
        b = float(input("Ingrese la Cantidad de Dolares que desea Convertir: "))
        print()
        
        montoConvertido = dolaresBolivares(b)
        montoRedondeado = round(montoConvertido,2)
        
        print("1 dólar estadounidense Es igual a 2,360,816.00 bolívar venezolano\n")
        print("El Monto Fue convertido, el resultado es: ", montoRedondeado,"Bolivares")
        
    elif opcionUsuario == 3:
        
        c = float(input("Ingrese la Cantidad de Dolares que Desea Convertir: "))
        print()
        
        montoConvertido = dolaresPesos(c)
        montoRedondeado = round(montoConvertido,2)
        
        print("1 dólar estadounidense Es igual a 3,643.00 peso colombiano\n")
        
        print("El Monto Fue convertido, el resultado es: ", montoRedondeado,"Pesos Colombianos")

    elif opcionUsuario == 4:
        
        d = float(input("Ingrese la Cantidad de Pesos que Desea Convertir: "))
        print()
        
        montoConvertido = pesosDolares(d)
        montoRedondeado = round(montoConvertido,2)
        
        print("1 peso colombiano Es igual a 0.00028 dólar estadounidense\n")
        
        print("El Monto Fue convertido, el resultado es: ", montoRedondeado,"Dolares")
        
    else:
        
        #Si el usuario indica un numero no valido se saldra del ciclo
        print("Ingrese un Valor Valido, Intente Nuevamente....\n")
        break
        
    input("\nPresione Enter para continuar.......\n")
        
    print("\n¿Que Desea Realizar?\n")

    print("1: Convertir Bolivares a Dolares\n")
    print("2: Convertir Dolares a Bolivares\n")
    print("3: Convertir Dolares a Pesos\n")
    print("4: Convertir Pesos a Dolares\n")
    print("5: Salir\n")

    opcionUsuario = int(input("Elija la opcion que desea realizar: ¿1, 2, 3, 4, 5?: "))
    print()
    
else:
    
    print("Gracias por usar nuestro programa")