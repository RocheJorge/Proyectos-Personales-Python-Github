"""
Solicitar al usuario: la estación, y a través de condicionales anidados el mes, de forma tal de mostrar en pantalla si esta en el inicio, mitad o fin de esa estación. Por ejemplo, si la estación es primavera y el mes es octubre, entonces el usuario se encuentra en la mitad de la estación.
"""
print("\nBienvenido al Programa para determinar su estacion del año\n")
# el usuario ingresa los datos de la estacion en la que se encuentra y se guarda en la variable estacion
estacion = input("Ingrese la Estacion del Año en la que se encuentra: Otoño (ot), Invierno(in), Primavera(pri), Verano(ve): ")
print()
if estacion == "ot":
    #el usuario ingresa los datos del mes en el que se encuentra y se guarda en la variable estacionMes
    estacionMes = input("Ingrese en cual Mes del Año se encuentra: Marzo(mar), Abril(abr), Mayo(may): ")
    print()
    #se evaluan las condicionales para imprimir el resultado por pantalla
    if estacionMes == "mar":
        print("Se encuentra al Inicio en la Estacion de Otoño")
    elif estacionMes == "abr":
        print("Se encuentra en la Mitad de la Estacion Otoño")
    elif estacionMes == "may":
        print("Se encuentra al Final en la Estacion de Otoño")
    else:
        #si el usuario ingresa un valor invalido se le imprimira un mensaje por pantalla de error
        print("El valor que ingreso no se encuentra dentro de los parametros establecidos, intente de nuevo")
        
elif estacion == "in":
    estacionMes = input("Ingrese en cual Mes del Año se encuentra: Junio(jun), Julio(jul): ")
    print()
    if estacionMes == "jun":
        print("Se encuentra al Inicio en la Estacion de Invierno")
    elif estacionMes == "jul":
        print("Se encuentra al Final de la Estacion de Invierno")
    else:
        print("El valor que ingreso no se encuentra dentro de los parametros establecidos, intente de nuevo")
        
elif estacion == "pri":
    estacionMes = input("Ingrese en cual Mes del Año se encuentra: Septiembre(sep), Octubre(oc), Noviembre(nov): ")
    print()
    if estacionMes == "sep":
        print("Se encuentra al Inicio en la Estacion de Primavera")
    elif estacionMes == "oc":
        print("Se encuentra en la Mitad de la Estacion de Primavera")
    elif estacionMes == "nov":
        print("Se encuentra al Final de la Estacion de Primavera")
    else:
        print("El valor que ingreso no se encuentra dentro de los parametros establecidos, intente de nuevo")

elif estacion == "ve":
    estacionMes = input("Ingrese en Cual Mes del Año se encuentra: Diciembre(dic), Enero(en), Febrero(feb): ")
    print()
    if estacionMes == "dic":
        print("Se encuentra al Inicio en la Estacion de Verano")
    elif estacionMes == "en":
        print("Se encuentra en la Mitad de la Estacion de Verano")
    elif estacionMes == "feb":
        print("Se encuentra en el Final de la Estacion de Verano")
    else:
        print("El valor que ingreso no se encuentra dentro de los parametros establecidos, intente de nuevo")
#este else pertenece al primer if del programa donde se le indica al usuario que ingrese la estacion del año en la que se encuentra, si el usuario ingresa un valor invalido, se le imprimira un mensaje de error por pantalla
else:
    print("El valor que ingreso no se encuentra dentro de los parametros establecidos, intente de nuevo")