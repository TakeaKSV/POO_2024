# 2.- 
# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

lista = []

while len(lista) < 120:
    lista.append(len(lista) + 1)

print("Lista con 120 elementos:")
for elemento in lista:
    print(elemento, end=" ")