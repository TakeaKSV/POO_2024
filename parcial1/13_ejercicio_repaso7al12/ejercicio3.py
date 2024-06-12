# 3.- 

# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas

lista = []

if not lista:
    print("La lista esta vacia, por favor añade palabras o frases")

    while True:
        entrada = input("Introduce una palabra o frase (o escribe 'salir' para terminar): ")

        if entrada.lower() == 'salir':
            break

        try:
            float(entrada)
            print("Error: No se pueden ingresar numeros, por favor introduce una palabra o frase")
        except ValueError:
            lista.append(entrada)
            print(f"'{entrada}' ha sido añadido a la lista")

print("Contenido de la lista en mayusculas:")
for elemento in lista:
    print(elemento.upper())     