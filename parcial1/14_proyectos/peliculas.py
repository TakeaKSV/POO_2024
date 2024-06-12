import os
from varias_funciones import *

def mostrar_menu():
    """Muestra el menú de opciones al usuario."""
    print("\nGestión de Películas")
    print("1. Agregar película")
    print("2. Remover película")
    print("3. Consultar películas")
    print("4. Buscar película")
    print("5. Actualizar película")
    print("6. Vaciar lista de películas")
    print("7. Salir")

def main():
    peliculas = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese el nombre de la película: ")
            anio = input("Ingrese el año de lanzamiento: ")
            genero = input("Ingrese el género: ")
            agregar_pelicula(peliculas, nombre, anio, genero)
        elif opcion == '2':
            nombre = input("Ingrese el nombre de la película a remover: ")
            confirmar = input(f"¿Está seguro de que desea remover la película '{nombre}'? (s/n): ")
            if confirmar.lower() == 's':
                remover_pelicula(peliculas, nombre)
            else:
                print("Acción cancelada.")
        elif opcion == '3':
            consultar_peliculas(peliculas)
        elif opcion == '4':
            nombre = input("Ingrese el nombre de la película a buscar: ")
            buscar_pelicula(peliculas, nombre)
        elif opcion == '5':
            nombre = input("Ingrese el nombre de la película a actualizar: ")
            nueva_nombre = input("Ingrese el nuevo nombre de la película: ")
            nuevo_anio = input("Ingrese el nuevo año de lanzamiento: ")
            nuevo_genero = input("Ingrese el nuevo género: ")
            actualizar_pelicula(peliculas, nombre, nueva_nombre, nuevo_anio, nuevo_genero)
        elif opcion == '6':
            confirmar = input("¿Está seguro de que desea vaciar la lista de películas? (s/n): ")
            if confirmar.lower() == 's':
                vaciar_peliculas(peliculas)
            else:
                print("Acción cancelada.")
        elif opcion == '7':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()