print("--- Registro de Gastos Simple ---")
print("Escribe 'salir' en el concepto para terminar.")

gastos = {}

while True:
    concepto = input("Concepto del gasto: ")
    
    if concepto.lower() == 'salir':
        break
        
    monto = float(input(f"Monto para '{concepto}': "))
    
    gastos[concepto] = monto

print("\n--- Resumen de Gastos ---")

for concepto, monto in gastos.items():
    print(f"- {concepto}: {monto}")

total = sum(gastos.values())
print("--------------------")
print(f"Gasto Total: {total}")