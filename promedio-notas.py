nota1 = float(input("Ingrese la Nota 1: "))

nota2 = float(input("Ingrese la Nota 2: "))

promedio = (nota1 + nota2) / 2

print("El promedio es: ",promedio)

if promedio >= 60:
    
    print("Aprobo la Materia")
    
else:
    
    print("Reprobo la Materia")