#Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aprobaron y cuantos no aprobaron
aprobados = 0
reprobados = 0

for i in range(1, 16):
    calificacion = float(input(f"Ingrese la calificación del alumno {i}: "))
    if calificacion >= 8:
        aprobados += 1
    else:
        reprobados += 1

print()
print(f"Alumnos aprobados: {aprobados}")
print(f"Alumnos reprobados: {reprobados}")

