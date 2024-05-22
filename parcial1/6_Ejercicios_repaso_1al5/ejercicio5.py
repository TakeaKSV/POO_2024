numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Los números entre {numero1} y {numero2} son:")
for numero in range(numero1 + 1, numero2):
    print(numero)
