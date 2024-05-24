def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def clasificar_composicion(imc):

    if imc < 18.5:
        return "Peso inferior al normal"
    elif 18.5 <= imc < 25.0:
        return "Normal"
    elif 25.0 <= imc < 30.0:
        return "Peso superior al normal"
    else:
        return "Obesidad"

def main():
    contador_calculos = 0

    while True:
        try:
            peso = float(input("Ingresa tu peso en kg: "))
            altura = float(input("Ingresa tu altura en metros: "))
            imc = calcular_imc(peso, altura)
            composicion = clasificar_composicion(imc)

            print(f"Tu IMC es {imc:.2f}. Clasificacion: {composicion}")

            contador_calculos += 1
            continuar = input("Deseas realizar otro calculo? (s/n): ").lower()
            if continuar != "s":
                break
        except ValueError:
            print("Por favor, ingresa valores numericos validos.")

    print(f"Se realizaron {contador_calculos} calculos de IMC.")

if __name__ == "__main__":
    main()
