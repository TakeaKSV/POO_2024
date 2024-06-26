def main():
    rectangulo = Rectangulo(5, 3)
    print(f"Área del rectángulo: {rectangulo.CalcularArea()}")

    circulo = Circulo(4)
    print(f"Área del círculo: {circulo.CalcularArea()}")

    triangulo = Triangulo(4, 6)
    print(f"Área del triángulo: {triangulo.CalcularArea()}")

if __name__ == "__main__":
    main()