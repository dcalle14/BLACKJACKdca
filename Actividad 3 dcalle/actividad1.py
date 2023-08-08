class Vehiculo:
    def __init__(self, velocidad_maxima: int, kilometraje: int):
        self.velocidad_maxima: int = velocidad_maxima
        self.kilometraje: int = kilometraje


if __name__ == "__main__":

    vk: Vehiculo = Vehiculo (100, 2500)

    print("velocidad_maxima", vk.velocidad_maxima, "km,h")
    print("kilometraje", vk.kilometraje, "km")


