numero_secreto = 42

print("¡Adivina el Número Secreto!")
print("Te daré pistas si estás cerca o lejos.")

while True:
    numero_del_usuario = int(input("Introduce tu número (1-100): "))

    if numero_del_usuario < numero_secreto:
        print("El número secreto es más GRANDE.")
        
        diferencia = numero_secreto - numero_del_usuario
        
        if diferencia <= 5:
            print("¡Pero estás muy CERCA! (Caliente)")
        elif diferencia > 20:
            print("Y estás muy LEJOS... (Frío)")
            
    elif numero_del_usuario > numero_secreto:
        print("El número secreto es más PEQUEÑO.")
        
        diferencia = numero_del_usuario - numero_secreto
        
        if diferencia <= 5:
            print("¡Pero estás muy CERCA! (Caliente)")
        elif diferencia > 20:
            print("Y estás muy LEJOS... (Frío)")
            
    else:
        print("¡Felicidades! ¡Has adivinado!")
        break