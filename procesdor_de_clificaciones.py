print("Procesador de calificaciones")
print("Falla por Inasistencia: Si la asistencia es < 80%, ¡reprobado directo! ")
print("Falla por Nota: Si la calificación es < 70, ¡reprobado!")
print("Cuadro de Honor: Si la calificación es >= 95 (y la asistencia es suficiente), ¡a la lista de honor Y a la de aprobados!")
print("Aprobado Regular: Si pasa los filtros anteriores, ¡está aprobado!")

calificaciones = int(input("Introduce tu calificacion: "))
inasistencias = int(input("Introduce la cantidad de inasistencia: "))