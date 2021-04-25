#Calcular area de un rectangulo
# area = base * altura

print("\nBienvenido al Programa para calcular el Area de un Rectangulo...\n")

altura = float(input("Ingrese la altura del rectangulo: "))
print()

base = float(input("Ingrese el valor de la base del rectangulo: "))
print()

area = base * altura

areaRedondeada = round(area, 2)

print("El area del rectangulo es: ", areaRedondeada)