#Escriba un programa que permita al usuario ingresar las medidas del cateto a y b de un triangulo rectangulo, su programa debera calcular la hipotenusa del triangulo a partir de la formula del teorema de pitagoras 

# c = (a^2 + b^2)^1/2

cateto1 = float(input("Ingrese Cateto a: "))

cateto2 = float(input("Ingrese Cateto b: "))

valor1 = (cateto1**2)

valor2 = (cateto2**2)

hipotenusa = (valor1 + valor2)**(1/2)

print("La hipotenusa es: {:.3f}".format(hipotenusa)) #mostrara 3 decimales