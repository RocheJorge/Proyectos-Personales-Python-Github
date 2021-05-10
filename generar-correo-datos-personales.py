#Cree un programa que genere un correo empresarial a partir del ingreso de los siguientes datos:

# a) Web empresarial (asumir que la URL siempre iniciara con www. y terminara con .com)
# b) Primer Nombre
# c) Segundo Nombre
# d) Primer Apellido
# e) Año de Naciemiento

#El correo debera tener la siguiente estructura:
# primera letra del primer nombre + primera letra del segundo nombre + primer apellido + 2 ultimos numeros del año de nacimiento + @ + nombre de la empresa + .com

## Pedir Datos al Usuario

sitioWeb = input("Ingrese URL Empresarial: ")

primerNombre = input("Ingrese Su Primer Nombre: ")

segundoNombre = input("Ingrese Su Segundo Nombre: ")

primerApellido = input("Ingrese Su Primer Apellido: ")

fechaNacimiento = input("Ingrese Su Fecha de Nacimiento: ")

## Condiciones

letraPrimerNombre = primerNombre[0]

letraSegundoNombre = segundoNombre[0]

ultimosNumeroNacimiento = fechaNacimiento[2:]

nombreEmpresa = sitioWeb[4:-4]

print("{}{}{}{}@{}.com".format(letraPrimerNombre,letraSegundoNombre,primerApellido,ultimosNumeroNacimiento,nombreEmpresa))