# Escribir un programa que permita el ingreso de dos numeros y muestre por pantalla True si el primer numero es divisible para el segundo, de no serlo muestre False

num1 = int(input("Ingrese el Primer Numero: "))

num2 = int(input("Ingrese el Segundo Numero: "))

residuo = num1 % num2


if residuo == 0:
    
    print("El numero:", num1, " y el numero:", num2)
    
    print("Son Divisibles")
    
else:
    
    print("El numero:",num1, " y el numero: ",num2)
    
    print("No son Divisibles")