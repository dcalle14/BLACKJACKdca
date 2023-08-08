class Punto:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

if __name__ == "__main__":
    pe: Punto = Punto(1,10)

    print("coordenadas:", pe.x, "," ,pe.y)

