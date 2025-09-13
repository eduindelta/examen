cliente = {
    "nombre": "Eduin",
    "edad": 36,
    "ciudad": "Maracaibo"
}

nuevos_datos = {
    "raza": "blanco",               
    "cedula": "12345678"  
}

cliente.update(nuevos_datos)
print(cliente)