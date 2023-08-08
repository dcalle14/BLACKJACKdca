#Cree una clase Circulo que tenga las propiedades centro y radio,
#las cuales se inicializan con parámetros en el constructor.
#Defina métodos en la clase para calcular el área,
#el perímetro e indicar si un punto pertenece al círculo o no.
import math
class Circulo:

    def __init__(self, centro: int, radio: int):
    self.centro: int = centro
    self.radio: int = radio

    def calcular_area(self, radio: int):
        r = float(input())
        a = math.pi * (r*r)
        print("el area del circulo con radio ",r, " Es: ",round(a, 2))

    def calcular_perimetro(self, radio: int):
        r = float(input())
        p = math.pi * (r+r)
        print("el perimetro del circulo con radio ", r, " Es: ", round(a, 2))

        radio = float(input('Ingresa el valor de radio: '))
        circunferencia = 2.0 * math.pi * radio
        perimetro = circunferencia
        area = math.pi * radio * radio
        print('Valor de area: ' + repr(area))
        print('Valor de circunferencia: ' + repr(circunferencia))
        print('Valor de perimetro: ' + repr(perimetro))
        print()
