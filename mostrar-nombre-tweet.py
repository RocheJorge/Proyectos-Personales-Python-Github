# Usted cuenta con una cadena de caracteres que simula un tweet donde se mencionan ayudantes de una materia en especifico. Ejemplo:

# tweet = "El dia de ayer hubo ayudantias con #Joel de FP y #Kevin de CUV ya se divirtieron los pollos, ahora le toca a los gallos con #Axell B"

#Asumir que los # solo contienen nombres de ayudantes.

# a) Mostrar el nombre del primer ayudante
# b) Mostrar el nombre del segundo ayudante
# c) Mostrar el nombre del ultimo ayudante

tweet = "El dia de ayer hubo ayudantias con #Joel de FP y #Kevin de CUV ya se divirtieron los pollos, ahora le toca a los gallos con #Axell B"

## Buscando primer ayudante

posicionPrimerHashtag = tweet.index("#") # Buscara la posicion del primer hashtag..................

subtweetPrimerHashtag = tweet[posicionPrimerHashtag + 1:] # Me mostrara a partir de Joel......

posicionEspacioPrimerHashtag = subtweetPrimerHashtag.index(" ") #Me mostrara la posicion del primer espacio despues del primer hashtag

ayudante1 = subtweetPrimerHashtag[:posicionEspacioPrimerHashtag] #Me mostrar lo que esta antes del espacio y despues del primer hashtag en este caso Joel

print(ayudante1)

## Buscando Segundo ayudante

posicionSegundoHashtag = subtweetPrimerHashtag.index("#") # Buscara la posicion del primer hashtag despues de #Joel

subtweetSegundoHashtag = subtweetPrimerHashtag[posicionSegundoHashtag + 1 :] # Me mostrara a partir de Kevin......

posicionEspacioSegundoHashtag = subtweetSegundoHashtag.index(" ") # Me mostrara la posicion del espacio despues del segundo hashtag

ayudante2 = subtweetSegundoHashtag[:posicionEspacioSegundoHashtag] # Me mostrar lo que esta antes del espacio y despues del segundo hashtag en este caso Kevin

print(ayudante2)

## Buscando Ultimo ayudante

tweetInvertido = tweet[::-1] # Me mostrara el tweet alreves

print(tweetInvertido)

posicionUltimoHashtag = tweetInvertido.index("#") # Determino la posicion del ultimo hashtag

subtweetUltimoHashtag = tweetInvertido[:posicionUltimoHashtag]

subtweetUltimoHashtagInvertido = subtweetUltimoHashtag[::-1]

posicionUltimoEspacio = subtweetUltimoHashtagInvertido.index(" ")

ultimoAyudante = subtweetUltimoHashtagInvertido[:posicionUltimoEspacio]

print(ultimoAyudante)