#Elabore un programa en python que pida al usuario una cantidad de segundos y muestre cuantas horas, minutos, segundos son

segundos = int(input("Ingrese Cantidad de Segundos: "))

horas = segundos // 3600 # 1 # // division entera

sobrante1 = segundos % 3600 # 65

minutos = sobrante1 // 60 # // division entera

sobrante2 = sobrante1 % 60 # 5

print("Horas")

print(horas)

print("Minutos")

print(minutos)

print("Segundos")

print(sobrante2)