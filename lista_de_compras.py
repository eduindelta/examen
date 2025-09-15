
lista_compras = ["Leche", "Pan", "Huevos", "Manzanas", "Queso"]
print(f"Lista original con 5 artículos: {lista_compras}")

del lista_compras[1]
print(f"Lista después de eliminar el segundo artículo: {lista_compras}")

print("\nLista de Compras Final")

for articulo in lista_compras:
    print(f"- {articulo}")