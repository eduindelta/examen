numeros = [15, 8, 27, 4, 12]

if not numeros:
    print("La lista está vacía.")
else:
    maximo_encontrado = numeros[0]
    for numero in numeros:
        if numero > maximo_encontrado:
            maximo_encontrado = numero
    print(f"De la lista {numeros}, el número más grande es: {maximo_encontrado}")