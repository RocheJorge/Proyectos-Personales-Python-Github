"""
Crear un cajero automático con Python, que en principio tendrá 1000$ de saldo en la cuenta ficticia , además deberá contener el siguiente menú:

1.- Ingresar dinero en cuenta.
2,- Retirar dinero de la cuenta.
3,- Mostrar dinero disponible.
4,- Salir.

Las condiciones para este ejercicio, son la solicitud de datos al usuario, actualizar el monto de la cuenta de acuerdo con la operación  realizar.

Realizado por: Jorge Roche 24743191
Curso de python Ingenieria Digital
"""
print("\nBienvenido al Cajero Automatico\n")

nombreUsuario = input("Ingrese Su Nombre: ")
print()
cedulaUsuario = input("Ingrese Su Cedula: ")
print()
claveUsuario = input("Ingrese Su Clave del Cajero: ")
print()

saldoCuenta = 1000

print("Bienvenido", nombreUsuario,"\n")
print("En tu cuenta hay un saldo de:", saldoCuenta,"$\n")

print("Que Deseas Realizar con tu Cuenta?: ")
print()

print("1. Ingresar dinero en cuenta\n")
print("2. Retirar dinero de la cuenta\n")
print("3. Mostrar dinero disponible\n")
print("4. Salir\n")

opcionCliente = int(input("¿Que Opcion Deseas Realizar: 1, 2, 3, 4?: "))
print()
#el cliente elige las opciones y entra al ciclo while mientras que la opcion sea igual o diferente de 4
while opcionCliente != 4:

    if opcionCliente == 1:
    
        print("Ingreso de Dinero en Cuenta\n")
        #el usuario ingresa el monto que desea en la cuenta
        sumarDinero = float(input("¿Cuanto Dinero Desea Ingresar en la Cuenta?: "))
        print()
        #aqui validamos si el usuario ingresa un monto invalido como -1, -2, -1000 etc..., Si lo hace se le emitira un mensaje de error
        if sumarDinero < 0:
            print("Ingrese un Monto Valido, Intente Nuevamente\n")
        else:
            #De lo contrario si ingresa un monto valido se sumara el nuevo monto con el monto anterior
            saldoCuenta += sumarDinero
            print("El Saldo en su Cuenta fue Actualizado Exitosamente\n")
            print("El Nuevo Monto es de: ", saldoCuenta,"$\n")

    elif opcionCliente == 2:
        
        print("Retiro Dinero de la Cuenta\n")
        #Aqui el usuario ingresara el monto que desea retirar
        restarDinero = float(input("¿Cuanto Dinero Desea Retirar de la Cuenta?: "))
        print()
        #si el monto que desea retirar es mayor al que posee en la cuenta se le emitira un mensaje de error y se le mostrara el monto que tiene disponible, ejem, posee solo 1000 pero desea retirar 2000, es invalido
        if saldoCuenta - restarDinero < 0:
            print("Saldo Invalido, Intente Nuevamente\n")
            print("Tu Saldo es de: ", saldoCuenta,"$\n")
        else:
            #De lo contrario si el monto es menor al que tiene en la cuenta se le restara el monto y se le imprimira por pantalla el nuevo monto
            saldoCuenta -= restarDinero
    
            print("El Saldo en su Cuenta fue Actualizado Exitosamente\n")
            print("El Nuevo Monto es de: ", saldoCuenta,"$\n")

    elif opcionCliente == 3:
    #se le mostrara el dinero disponible
        print("Mostrar Dinero Disponible\n")
        print("En Su Cuenta Bancaria hay un Monto de: ", saldoCuenta,"$\n")
        
    else:
        print("Gracias Por usar nuestro Cajero Automatico\n")
        
    input("Presione Enter para continuar.......")
    
    print()
    print("Que Deseas Realizar con tu Cuenta?: ")
    print()
    
    print("1. Ingresar dinero en cuenta\n")
    print("2. Retirar dinero de la cuenta\n")
    print("3. Mostrar dinero disponible\n")
    print("4. Salir\n")

    opcionCliente = int(input("Que Opcion Deseas Realizar: 1, 2, 3, 4?: "))
    print()
    #el ciclo se repetira mientras el usuario presione las opciones 1, 2, 3. Se saldra del ciclo solo si el usuario presiona 4 o un numero superior
else:
    print("Gracias Por usar nuestro Cajero Automatico\n")