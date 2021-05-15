"""
Un peaje de la ciudad quiere que usted sistematice el control de pago de los peajes, por este pasan 3 vehiculos automotores:

1) Vehiculos
2) Camiones
3) Tractomulas

No se sabe cuantos de estos pasan al dia por el peaje, pero cuando el dia finaliza se registra un tipo de automotor cero 0. El cobro por cada tipo de automotor es el siguiente:

Tipo Valor:
1) Vehiculo $ 3.50
2) Camion $12.00
3) Tractomula $16.00

Desarrolle un programa en python donde conociendo el tipo de automotor determinar:
    - El valor a pagar por cada automotor que pase por el peaje
    - Total recaudado en el peaje ese dia
    - Total recaudado por cada tipo de automotor
    - Cual es el tipo de Automotor que mas transita por el peaje
"""

#    - El valor a pagar por cada automotor que pase por el peaje

automotores = ["vehiculo", "camion", "tractomula"]
precio = [3.50, 12.00, 16.00]

#    - Total recaudado en el peaje ese dia

totalRecaudadoDia =[0,0,0]

#    - Total recaudado por cada tipo de automotor

totalRecaudadoAutomotores = [0,0,0]

#    - Cual es el tipo de Automotor que mas transita por el peaje

contadorTransita = [0,0,0]

######## Inicio Programa

iniciarDia = "no"

while iniciarDia == "no" or iniciarDia == "n":
    
    print("Bienvenido al programa de peajes")

    print("Que Automotor esta Transitando?")

    print("Vehiculo")
    print("Camion")
    print("Tractomula")

    tipoAutomotor = input("Ingrese Tipo de Automotor: ").lower()

    if tipoAutomotor in automotores:
        
        posicionAutomotor = automotores.index(tipoAutomotor)
        
        precioAutomotor = precio[posicionAutomotor]
        
        print("El valor a pagar es de: {}$".format(precioAutomotor))
        
        totalRecaudadoDia[posicionAutomotor] += precioAutomotor
        totalRecaudadoAutomotores[posicionAutomotor] += precioAutomotor
        contadorTransita[posicionAutomotor] += 1

    elif tipoAutomotor in automotores:
        
        posicionAutomotor = automotores.index(tipoAutomotor)
        
        precioAutomotor = precio[posicionAutomotor]
                
        print("El valor a pagar es de: {}$".format(precioAutomotor))
        
        totalRecaudadoDia[posicionAutomotor] += precioAutomotor
        totalRecaudadoAutomotores[posicionAutomotor] += precioAutomotor
        contadorTransita[posicionAutomotor] += 1
        
    elif tipoAutomotor in automotores:
        
        posicionAutomotor = automotores.index(tipoAutomotor)
        
        precioAutomotor = precio[posicionAutomotor]
        
        print("El valor a pagar es de: {}$".format(precioAutomotor))

        totalRecaudadoDia[posicionAutomotor] += precioAutomotor
        totalRecaudadoAutomotores[posicionAutomotor] += precioAutomotor
        contadorTransita[posicionAutomotor] += 1
        
    else:
        
        print("Ingrese un Vehiculo Valido")
    
    iniciarDia = input("El dia a Finalizado? Si(s) o No(n): ")
    
else:
    
    print("Dia Finalizado")
    
#    - Total recaudado en el peaje ese dia

sumaTotalDia = sum(totalRecaudadoDia)

print("El Total Recaudado en el dia es de: {}$".format(sumaTotalDia))

#    - Total recaudado por cada tipo de automotor

print("El Total Recaudado por Vehiculo es de: {}$".format(totalRecaudadoAutomotores[0]))

print("El Total Recaudado por Camion es de: {}".format(totalRecaudadoAutomotores[1]))

print("El Total Recaudado por Tractomula es de: {}$".format(totalRecaudadoAutomotores[2]))

#    - Cual es el tipo de Automotor que mas transita por el peaje

maximoTransita = max(contadorTransita)

posicionMasTransita = contadorTransita.index(maximoTransita)

automotorMasTransita = automotores[posicionMasTransita]

print("El tipo de automotor que mas transito fue: {}".format(automotorMasTransita))