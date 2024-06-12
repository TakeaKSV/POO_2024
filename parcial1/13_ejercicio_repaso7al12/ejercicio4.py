#  4.- 

#  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
#   y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones

def imprimir_tipo(variable):
    """Función que imprime el tipo de dato de la variable y un mensaje asociado."""
    if isinstance(variable, list):
        print("Esta variable es una lista.")
    elif isinstance(variable, str):
        print("Esta variable es una cadena.")
    elif isinstance(variable, int):
        print("Esta variable es un entero.")
    elif isinstance(variable, bool):
        print("Esta variable es un valor lógico (booleano).")
    else:
        print("Esta variable es de un tipo no reconocido.")

lista = [1, 2, 3, 4, 5]
cadena = "El mas olvidao do mundo"
entero = 42
logico = True

print(type((lista)))
print(type((cadena)))
print(type((entero)))
print(type((logico)))