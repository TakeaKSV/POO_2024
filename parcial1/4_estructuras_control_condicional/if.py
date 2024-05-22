"""
Existe una estructura de condicion llamada If, la cual evalua una condicion para 
encontrar el valor del verdadero o se cumple la condicion se 

ejecuta la linea o lineas de codigo

Tienes 3 variantes del if

1. if simple
2. if condicional
3. if anidado
4. if y elif

"""

# Ejemplo 1 If simple

color="rojo"
if color=="rojo" :
  print("Soy el color rojo")

# Ejemplo 2 If compuesto

color="rojo"
if color=="rojo" :
  print("Soy el color rojo")
else:
  print("No soy el color rojo")

# Ejemplo 3 If anidado

color = "rojo"
if color == "rojo":
    print("Soy el color rojo")
    if color != "rojo":
        print("Soy otro color")
else:
    print("No soy el color rojo")
    if color != "rojo":
        print('Soy otro color')

# Ejemplo 4 If y elif

color = "rojo"
if color=="rojo":
  print("Soy el color rojo")
elif color=="negro":
  print("Soy el color negro")
elif color=="verde":
  print("Soy el color verde")
else:
  print("No soy rojo, ni negro, ni verde")


