
texto = "clase de Programacion"

mayusculas = 0
minusculas = 0

for caracter in texto:
    if caracter.isupper():
        mayusculas += 1
    elif caracter.islower():
        minusculas += 1

print(f"Texto: '{texto}'")
print(f"Cantidad de Myusculas: {mayusculas}")
print(f"Cantidad de minúsculas: {minusculas}")

