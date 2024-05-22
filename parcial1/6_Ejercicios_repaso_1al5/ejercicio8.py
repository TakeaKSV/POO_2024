#Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?
numero = float(input("Ingrese el numero: "))
porcentaje = float(input("Ingrese el porcentaje: "))

resultado = (numero * porcentaje) / 100


print(f"El {porcentaje}% de {numero} es: {resultado}")
