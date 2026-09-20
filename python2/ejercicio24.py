class AnalizadorResenas:
    """Analiza reseñas de 1 a 5 estrellas."""

    def __init__(self):
        self.resenas = []

    def agregar_resena(self, estrellas):
        if 1 <= estrellas <= 5:
            self.resenas.append(estrellas)
            return True
        return False

    def promedio_estrellas(self):
        if not self.resenas:
            return 0
        return sum(self.resenas) / len(self.resenas)

    def resenas_por_estrella(self, n):
        return self.resenas.count(n)

    def porcentaje_positivas(self):
        if not self.resenas:
            return 0
        positivas = [r for r in self.resenas if r >= 4]
        return len(positivas) / len(self.resenas) * 100


ar = AnalizadorResenas()
for e in [5, 4, 3, 5, 1]:
    ar.agregar_resena(e)
print(f"Promedio: {ar.promedio_estrellas()}")
print(f"Con 5 estrellas: {ar.resenas_por_estrella(5)}")
print(f"% positivas: {ar.porcentaje_positivas()}")