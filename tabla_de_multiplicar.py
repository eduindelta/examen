numero = int(input("Introduce un número: "))

print(f"--- Tabla de Multiplicar del {numero} ---")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")