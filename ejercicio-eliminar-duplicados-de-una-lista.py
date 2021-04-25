
"""
Con la siguiente lista:

Lista = [1, 2, 3, 4, 5, 1, 6, 7, 9, 4, 5, 1, 8, 4, 1, 5]

a partir de alli, debes desarrollar un codigo que permita eliminar los valores repetidos y muestre en otra lista los elementos que no han sido eliminados, es decir, los que no se repiten

Realizado por Jorge Roche 24743191
"""
print("\nBienvenido al Programa donde se Eliminan los Numeros Duplicados\n")

Lista = [1, 2, 3, 4, 5, 1, 6, 7, 9, 4, 5, 1, 8, 4, 1, 5]

print("La Lista posee los Siguientes Numeros: ")
print()
print(Lista)

Lista = list(set(Lista))
print()

print("Se eliminaron los numeros repetidos obteniendo el siguiente resultado: ")
print()
print(Lista)