while True:
    entrada_usuario = input("Por favor, introduce un número entre 1 y 10: ")
    
    if entrada_usuario.isdigit():
        numero = int(entrada_usuario)
        
        if 1 <= numero <= 10:
            print(f"¡Gracias! El número {numero} es válido.")
            break
        else:
            print("Error: El número debe estar entre 1 y 10.")
    else:
        print("Error: Debes introducir un número entero válido.")

print("...El programa puede continuar.")