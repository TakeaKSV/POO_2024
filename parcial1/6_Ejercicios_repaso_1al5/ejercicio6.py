# Mostrar todas las tablas del 1 al 10. Mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
contador = 1
while contador<=10:
    print(f"Tabla de multiplicar del {contador}:")
    i = 1
    while i <= 10:
        resultado = contador * i
        print(f"{contador} * {i} = {resultado}")
        i += 1
    print() 
    contador += 1