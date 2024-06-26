class Figura:
    def __init__(self, x, y, visible):
        self._x = x
        self._y = y
        self._visible = visible

    def getX(self):
        return self.x

    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y

    def setY(self, y):
        self.y = y

    def getVisible(self):
        return self.visible

    def setVisible(self, visible):
        self.visible = visible

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible = True

    def ocultar(self):
        self.visible = False

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def getInfo(self):
      return f"Figura en ({self.x}, {self.y}) - Visible: {self.visible}"

class Rectangulo(Figura):
    def __init__(self, x, y, ancho, alto, visible):
        super().__init__(x, y, visible)
        self.__ancho = ancho
        self.__alto = alto

    def getAncho(self):
        return self.__ancho

    def setAncho(self, ancho):
        self.__ancho = ancho

    def getAlto(self):
        return self.__alto

    def setAlto(self, alto):
        self.__alto = alto

    def calcularArea(self):
        return self.__ancho * self.__alto

    def getInfo(self):
      return (f"Rectángulo en ({self.x}, {self.y}) - Ancho: {self.ancho}, "
              f"Alto: {self.alto} - Visible: {self.visible}")

class Circulo(Figura):
    def __init__(self, x, y, radio, visible):
        super().__init__(x, y, visible)
        self.__radio = radio

    def getRadio(self):
        return self.__radio

    def setRadio(self, radio):
        self.__radio = radio

    def calcularArea(self):
        import math
        return math.pi * (self.__radio ** 2) #Libreria para que use el valor completo de Pi y no solo 3.1416  

    def getInfo(self):
      return (f"Círculo en ({self.x}, {self.y}) - Radio: {self.radio} - "
              f"Visible: {self.visible}")

