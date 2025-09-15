print("---------- Clasificador de numeros ----------")
print("Veremos si tu numero es positivo, negativo o cero")
num = float(input("Introduce un numero: "))

if num == 0:
    print("Tu numero es cero")
elif num >= 1:
    print("Tu numero es positivo")
else:
    print("Tu numero es negativo")