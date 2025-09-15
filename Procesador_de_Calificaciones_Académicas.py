registros_estudiantes = [
    ('Ana Garcia', 'Matematicas', 98, 90),
    ('Luis Perez', 'Historia', 65, 85),
    ('Marta Diaz', 'Biologia', 88, 75),
    ('Javier Soto', 'Matematicas', 96, 95),
    ('Carla Nunez', 'Historia', 85, 100),
    ('Pedro Rivas', 'Biologia', 72, 81)
]

aprobados = []
reprobados = []
cuadro_de_honor = []

for estudiante in registros_estudiantes:
    nombre = estudiante[0]
    calificacion = estudiante[2]
    asistencia = estudiante[3]
    if asistencia < 80:
        reprobados.append(nombre)  
    elif calificacion < 70:
        reprobados.append(nombre) 
    elif calificacion >= 95:
        cuadro_de_honor.append(nombre) 
        aprobados.append(nombre)       
    else:
        aprobados.append(nombre) 

print("--- Reporte de Calificaciones ---")

print("\nCUADRO DE HONOR:")
print(cuadro_de_honor)

print("\nESTUDIANTES APROBADOS:")
print(aprobados)

print("\nESTUDIANTES REPROBADOS:")
print(reprobados)