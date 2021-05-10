#Cree un programa en python que solicite un numero de 3 digitos y un segundo numero de 1 digito por teclado y muestre por pantalla True si cumple las siguientes condiciones, False caso contrario:

#1) Los dos ultimos digitos del primer numero es divisible para el segundo numero

#2) El cuadrado del segundo numero es menor que los dos ultimos digitos del primer numero

num1 = int(input("Ingrese un numero con una cantidad de 3 digitos: ")) # 860

num2 = int(input("Ingrese un numero con una cantidad de 1 digito: ")) # 2

ulti2 = num1 % 100 # nos dara los 2 ultimos digitos del numero ingresado # 60

#1) Los dos ultimos digitos del primer numero es divisible para el segundo numero

cond1 = ulti2 % num2 == 0 # si es divisible arrojara 0 # 0

#2) El cuadrado del segundo numero es menor que los dos ultimos digitos del primer numero

cuadrado = num2**2 # 4

cond2 = cuadrado < ulti2 # 4 es menor que 60

#se cumplen las condiciones?

if cond1 and cond2:
    
    print("Se Cumplieron las 2 Condiciones")
    
else:
    
    print("No se Cumplieron las 2 Condiciones")