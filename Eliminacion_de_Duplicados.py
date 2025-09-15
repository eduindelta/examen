lista_duplicados = [10, 20, 20, 30, 40, 40, 40, 50]
print(f"Lista Original: {lista_duplicados}")

conjunto= set(lista_duplicados)

lista_sin_duplicados = list(conjunto)
print(f"Lista Final (sin duplicados): {lista_sin_duplicados}")