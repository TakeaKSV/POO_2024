# class Figura:
#     def __init__(self, area, lados):
#         self.area=area 
#         self.lados=area 


from math import pi

class Figura:
    def CalcularArea(self):
        raise NotImplementedError("Este método debe ser sobrescrito por la subclase")

class Rectangulo(Figura):
    def __init__(self, largo=0.0, ancho=0.0):
        self._largo = largo
        self._ancho = ancho

    def getLargo(self):
        return self._largo

    def setLargo(self, largo):
        self._largo = largo

    def getAncho(self):
        return self._ancho

    def setAncho(self, ancho):
        self._ancho = ancho

    def CalcularArea(self):
        return self._largo * self._ancho

class Circulo(Figura):
    def __init__(self, radio=0.0):
        self._radio = radio

    @property
    def getRadio(self):
        return self._radio

    @radio.setter
    def setRadio(self, radio):
        self._radio = radio

    def CalcularArea(self):
        return pi * (self._radio ** 2)

class Triangulo(Figura):
    def __init__(self, altura=0.0, ancho=0.0):
        self._altura = altura
        self._ancho = ancho

    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, altura):
        self._altura = altura

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def CalcularArea(self):
        return (self._altura * self._ancho) / 2

