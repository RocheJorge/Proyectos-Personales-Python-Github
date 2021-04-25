"""
Con las siguientes listas:

Lista1 = [{2, 5, 89.3, “hola”}, {96, 1.2, 6, “adios”}, {“hora”, 7, 9, 96, 1.3}, {“adios”, 2, 1.2}]
Lista2 = [{1.2, “Venezuela”, 2}, {“hola”, 96, 8}, {42, 6.9, 96, 3, “hora”}, {12, 89.3, 8, 45, “te”}]

crear cuatro listas nuevas con las siguientes condiciones sin que existan elementos duplicados en las nuevas colecciones a crear, (por ejemplo si en ambas listas se repite el número 2 solo debes mostrarlo una vez) :
-	La primera lista llevara los elementos que se repiten en ambas listas (Lista1 y Lista2).
-	La segunda lista mostrara los elementos que aparecen en la primera lista (Lista1), pero no en la segunda lista (Lista2).
-	La tercera lista mostrara los elementos que aparecen en Lista2, pero no en Lista1.
-	La cuarta lista mostrara los elementos que no se repiten en ninguna de las dos listas.

Realizado por Jorge Roche 24743191
"""

print("\nBienvenido al programa Conjunto de Listas\n")

Lista1 = [{2, 5, 89.3, "hola"}, {96, 1.2, 6, "adios"}, {"hora", 7, 9, 96, 1.3}, {"adios", 2, 1.2}]

Lista2 = [{1.2, "Venezuela", 2}, {"hola", 96, 8}, {42, 6.9, 96, 3, "hora"}, {12, 89.3, 8, 45, "te"}]

print("Poseemos las Listas: ")

print()

print("Lista 1= ", Lista1)

print()

print("Lista 2= ", Lista2)

#sin elementos duplicados lista 1

NuevaLista1 = set()

for s in Lista1:
    NuevaLista1 = NuevaLista1|s

print("\nMostramos la Nueva Lista con los elementos sin duplicar en la lista 1\n")

print(NuevaLista1)

#sin elementos duplicados lista 2

NuevaLista2 = set()

for s in Lista2:
    NuevaLista2 = NuevaLista2|s

print("\nMostramos la Nueva Lista con los elementos sin duplicar en la lista 2\n")

print(NuevaLista2)

print()

print("\nDebemos cumplir las Siguientes Condiciones:\n")

#1) La primera lista llevara los elementos que se repiten en ambas listas (Lista1 y Lista2). (interseccion)

interseccionLista1 = NuevaLista1
interseccionLista2 = NuevaLista2

interseccion = interseccionLista1&interseccionLista2

print("1) La primera lista llevara los elementos que se repiten en ambas listas (Lista1 y Lista2). (interseccion)\n")

print(interseccion)

print()
#2) La segunda lista mostrara los elementos que aparecen en la primera lista (Lista1), pero no en la segunda lista (Lista2). (diferencia)

diferenciaLista1 = NuevaLista1 - NuevaLista2

print("2) La segunda lista mostrara los elementos que aparecen en la primera lista (Lista1), pero no en la segunda lista (Lista2). (diferencia)\n")

print(diferenciaLista1)

print()
#3) La tercera lista mostrara los elementos que aparecen en Lista2, pero no en Lista1.(diferencia)

diferenciaLista2 = NuevaLista2 - NuevaLista1

print("3) La tercera lista mostrara los elementos que aparecen en Lista2, pero no en Lista1.(diferencia)\n")

print(diferenciaLista2)

print()
#4) La cuarta lista mostrara los elementos que no se repiten en ninguna de las dos listas.(union)

Lista1Lista2 = NuevaLista1|NuevaLista2

print("4) La cuarta lista mostrara los elementos que no se repiten en ninguna de las dos listas.(union)\n")

print(Lista1Lista2)