paises= ["Mexico", "USA", "Brasil", "Japon"]
numeros= [23, 34, 12.56, 0.100, 23]
texto= ["Hola", True, 23, 3.141516]

# Ordenar una lista :0

print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)

# Anadir elementos >:0

print(texto)
texto.insert(len(texto), "True")
print(texto)
texto.insert(len(texto), True)
print(texto)
texto.append(False)
print(texto)

# Eliminar elementos >:/

print(numeros)
numeros.remove(23)
print(numeros)
numeros.pop(0)
print(numeros)

#Dar vuelta a una lista

print(numeros)
numeros.reverse() #Da la vuelta a la lista de manera 
print(numeros)

#Buscar un dato dentro de una lista

respuesta='Brasil' in paises
print(respuesta)

#Cuantas veces aparece un valor dentro de una lista

print(numeros)
numeros.append(23)
cuantos=numeros.count(23)
print(f'El numero 23 se encontro: {cuantos}')

#Unir listas 

print(paises)
paises.extend(numeros)
print(paises)