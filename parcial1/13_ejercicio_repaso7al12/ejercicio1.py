# 1.- 

#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

def mostrar_lista(lista):
  return " ".join(str(num) for num in lista)

def main():
  # Lista de 8 numeros original
  lista = [8, 3, 5, 1, 9, 6, 7, 2]

  # Imprimir lista original
  print("Lista original:", lista)

  # Devuelve string
  lista_str = mostrar_lista(lista)
  print("Lista como string:", lista_str)

  # Ordenarla y imprimirla
  lista_ordenada = sorted(lista)
  print("Lista ordenada:", lista_ordenada)

  # Longitud de la lista
  print("Longitud de la lista:", len(lista))

  # Buscar
  elemento = int(input("Introduce el numero a buscar: "))
  if elemento in lista:
      print(f"El numero {elemento} esta en la lista en la posicion {lista.index(elemento)}.")
  else:
      print(f"El numero {elemento} no se encuentra en la lista.")

if __name__ == "__main__":
  main()