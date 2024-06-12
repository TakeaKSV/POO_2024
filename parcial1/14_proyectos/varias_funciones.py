def agregar_pelicula(lista, nombre, anio, genero):
    pelicula = {'nombre': nombre, 'anio': anio, 'genero': genero}
    lista.append(pelicula)
    print(f"Película '{nombre}' agregada exitosamente.")

def remover_pelicula(lista, nombre):
    for pelicula in lista:
        if pelicula['nombre'] == nombre:
            lista.remove(pelicula)
            print(f"Película '{nombre}' removida exitosamente.")
            return
    print(f"No se encontró la película '{nombre}'.")

def consultar_peliculas(lista):
    if not lista:
        print("No hay películas registradas.")
    else:
        print("Lista de películas:")
        for pelicula in lista:
            print(f"Nombre: {pelicula['nombre']}, Año: {pelicula['año']}, Genero: {pelicula['genero']}")

def buscar_pelicula(lista, nombre):
    for pelicula in lista:
        if pelicula['nombre'] == nombre:
            print(f"Película encontrada: {pelicula}")
            return pelicula
    print(f"No se encontró la película '{nombre}'.")

def vaciar_peliculas(lista):
    lista.clear()
    print("Lista de películas vaciada correctamente.")

def actualizar_pelicula(lista, nombre, nueva_nombre, nuevo_anio, nuevo_genero):
    for pelicula in lista:
        if pelicula['nombre'] == nombre:
            pelicula['nombre'] = nueva_nombre
            pelicula['anio'] = nuevo_anio
            pelicula['genero'] = nuevo_genero
            print(f"Película '{nombre}' actualizada exitosamente.")
            return
    print(f"No se encontró la película '{nombre}'.")