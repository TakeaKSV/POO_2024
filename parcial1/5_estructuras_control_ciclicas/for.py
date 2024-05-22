#Este ciclo es un ciclo iterativo y se ejecuta x veces de acuerdo a los valores 
#numericos, enteros establecidos

# sintaxis: 
# # for variable in elemento-iterable(lista,rango, etc.):
# bloque de instrucciones

# ejemplo 1 crear un programa que imprima 5 veces el caracter @

contador=1
for contador in range(1, 6):
  print("@")

# ejercicio 2 crear un programa que imprima los numeros del 1 al 5, los sume y al final
# imprima el resultado
suma=0
for numero in range(1,6):
  print(numero)
suma+=numero
print(f"La suma es: {suma}")

#ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la
#tabla de multiplicar correspondiente

numeros=int(input("Ingresa un numero: "))

multi=0
for i in range(1,11):
  multi=i*numeros
  print(f"{numeros} X {i} = {multi}")


  
  
