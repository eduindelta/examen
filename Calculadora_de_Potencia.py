base = int(input("Introduce el número base: "))
exponente = int(input("Introduce el exponente: "))

resultado = 1

for _ in range(exponente):
    resultado = resultado * base

print(f"El resultado de {base} elevado a {exponente} es: {resultado}")