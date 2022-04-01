#nuestra primera función

def songs():
    print("no te pares frente a mi")
    print("con esa mirada tan hiriente")

songs()
print(type(songs))

#las funciones se puede utilizar también dentro de otras funciones

def chorus():
    songs()
    songs()

chorus()