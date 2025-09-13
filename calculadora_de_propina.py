print("-----calculadora de propina-----")
comida = input("Introduce alimentos consumidos: ")
bebida = input("Introduce bebidas consumidas: ")

cocacola = 2
pizza = 5

total = (cocacola + pizza)
propina = total + (total * 0.15)

if bebida == "cocacola" and comida == "pizza":
    print(f"Tu monto a pagar mas el 15% de propina es {propina} ")
