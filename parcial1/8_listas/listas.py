"""


List (Array)
son colecciones o conjuntos de datos/variables bajo uun mismo nombre, para acceder a los valores se hace con un indice numerico

nota: sus valores si son modificables

la lista es una coleccion ordenada y modificable, permite miembros duplicados

"""

import os

os.system("cls")

##Ejemplo 1 crear  ununa lista con datos numericos e imprimir el contenido

lista=[23, 34]

print(lista)

##recorrer lista con ciclo for

for i in lista:
    print(i)

##recorrer lista con while

while i<=len(lista)-1:
    print(lista[i])
    i+=1

##Ejemplo 2 crear una lista de palabras, solicitar una palabra y buscar una coincidencia en la lista, indicar si la encontro o no y en que posicion

palabras=["hola", "20", "bye", "UTD"]

palabra_buscar=input("Ingresa la palabra a buscar: ")

encontre=True
for i in palabras:
    if palabra_buscar==i:
        if i != -1:
            print (f"He encontrado la palabra: {i}, en la posicion: {palabras.index(i)}")
        encontre=False
        
if encontre:
    print(f"No encontre la palabra")

##con while >:(

ind=0

while ind< len(palabras):
    if palabras_buscar==palabras[ind]:
        print(f"Encontre la palabra: {palabra_buscar}, en la posicion: {ind}")
        encontre=False  
        ind += 1

if not encontre:
    print(f"No encontre la palabra")

##ejemplo 3 agregar y eliminar elementos de una lista

numeros=[23, 24]

print(numeros)

##agrega elemento

numeros.append(100)
print(numeros)
numeros.insert(3, 200)
print(numeros)

##el##eliminar un elemetos

numeros.remove(100) ##se indica el elmelemento a borrar
print(numeros)
numeros.pop(2) ##indica la posicion a borrar
print(numeros)

#ejemplo 4 crear una lista multidimensional (matriz) para almacenar los contactos telefonicos 

agenda={
    ["Carlos", 6182334567],
    ["Karin", 6182334568],
    ["Leon", 6182334569],
    ["Pedro", 6182334569],
}

print(agenda)

for i in agenda:
    print(f"{agenda.index(i)+1}.-{i}")

#ejemplo 5 crear un programa que permita gestionar peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas.
#notas:
#1. Utilizar funciones y mandar a llamar desde otro archivo
#2. Utilizar listas para almacenar los nombres de peliculas

from peliculas import *

def mostrar_menu():
            """Muestra el menú de opciones al usuario."""
            print("Gestión de Películas")
            print("1. Agregar película")
            print("2. Remover película")
            print("3. Consultar películas")
            print("4. Salir")

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
                    print("Saliendo del programa.")
                    break
                else:
                    print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
            main()
