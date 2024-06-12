import os
import math

def solicitarDatos():
    global n1, n2
    n1 = float(input("Número #1: "))
    n2 = float(input("Número #2: "))

def getCalculadora(num1, num2, operacion):
    if operacion == "1" or operacion == "+" or operacion == "SUMA":
        resultado = f"{num1} + {num2} = {num1 + num2}"
    elif operacion == "2" or operacion == "-" or operacion == "RESTA":
        resultado = f"{num1} - {num2} = {num1 - num2}"
    elif operacion == "3" or operacion == "*" or operacion == "MULTIPLICACION":
        resultado = f"{num1} * {num2} = {num1 * num2}"
    elif operacion == "4" or operacion == "/" or operacion == "DIVISION":
        resultado = f"{num1} / {num2} = {num1 / num2}"
    elif operacion == "5" or operacion == "^" or operacion == "POTENCIA":
        resultado = f"{num1} ^ {num2} = {num1 ** num2}"
    elif operacion == "6" or operacion == "RAIZ" or operacion == "RAÍZ":
        resultado = f"√{num1} = {math.sqrt(num1)}"
    else:
        resultado = "Opción inválida, por favor vuelve a intentarlo"
    return resultado

def esperaTecla():
    print("Presiona cualquier tecla para continuar...")
    input()

opcion = True
while opcion:
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.- Multiplicación \n 4.- División \n 5.- Potencia \n 6.- Raíz \n 7.- SALIR ")
    opcion = input("\t Elige una opción: ").upper()

    if opcion != "7":
        solicitarDatos()
        print(getCalculadora(n1, n2, opcion))
        esperaTecla()
    else:
        opcion = False
        print("Gracias por utilizar el sistema ...")