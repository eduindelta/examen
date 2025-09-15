frutas = ["manzana", "banana", "cereza", "naranja"]
elemento_a_buscar = "cereza"

if elemento_a_buscar in frutas:
    posicion = frutas.index(elemento_a_buscar)
    print(f"El elemento '{elemento_a_buscar}' se encuentra en la posición: {posicion}")
else:
    print(f"El elemento '{elemento_a_buscar}' no está en la lista.")