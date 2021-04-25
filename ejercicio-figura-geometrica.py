"""
Hallar el volumen de un cilindro, con datos ingresados por teclado, solicitar radio y altura e indicarle al usuario el tipo de cilindro que tiene segun las siguientes especificaciones:

1) Si el volumen del cilindro es menor que 10cm cubicos, es un cilindro de poca capacidad
2) Si el volumen se encuentra dentro del rango entre 11 y 20cm cubicos es de mediana capacidad
3) Si es mayor que 21cm cubicos es un cilindro de mayor capacidad 

Mostrar en pantalla el tipo de cilindro de acuerdo con las condiciones establecidas 

formula
V = pi x r^2 x h
"""
print("\nBienvenido al Programa para hallar el volumen de un cilindro\n")
print("La formula que se usara para determinar el valor del volumen es: V = pi.r^2.h \n")

print("Tomando en cuenta lo siguiente:")
print("pi= 3.1416")
print("r = radio")
print("h = altura")
print()

print("Ingrese los datos que se le piden a continuacion:\n")
radio = float(input("Ingrese el Radio del Cilindro: "))
print()

altura = float(input("Ingrese la Altura del Cilindro: "))
print()

PI = 3.1416
radio = radio**2

volumen = float(PI * radio * altura)

volumenRedondeado = round(volumen,2)

print("El Volumen del Cilindro es: ", volumenRedondeado, "cm^3")
print()

cilindroMenor = volumen < 10
print("1) El cilindro es de poca capacidad: ", cilindroMenor)
print()

cilindroMedianaCapacidad = volumen >= 11 and volumen <= 20
print("2) El Cilindro es de Mediana Capacidad: ", cilindroMedianaCapacidad)
print()

cilindroMayorCapacidad = volumen > 21
print("3) El Cilindro es de Mayor Capacidad: ", cilindroMayorCapacidad)