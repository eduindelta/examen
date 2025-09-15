contrasena = input("Crea tu contraseña: ")

if len(contrasena) >= 8:
    print("¡Contraseña válida!")
else:
    print("La contraseña es demasiado corta. Necesita al menos 8 caracteres.")