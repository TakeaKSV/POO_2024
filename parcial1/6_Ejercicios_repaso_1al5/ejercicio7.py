#Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario
numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

if numero1 > numero2:
        numero1, numero2 = numero2, numero1

print(f"Numeros impares entre {numero1} y {numero2}:")

for numero in range(numero1, numero2 + 1):
        if numero % 2 != 0:
            print(numero)
