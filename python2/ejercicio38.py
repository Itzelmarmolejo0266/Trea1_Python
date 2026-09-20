class Playlist:
    """Gestiona una playlist de canciones con su duración."""

    def __init__(self):
        self.canciones = []  # (titulo, duracion_segundos)

    def agregar_cancion(self, titulo, duracion):
        self.canciones.append((titulo, duracion))

    def duracion_total(self):
        return sum(d for _, d in self.canciones)

    def canciones_largas(self, limite):
        return [t for t, d in self.canciones if d > limite]

    def eliminar_cancion(self, titulo):
        self.canciones = [c for c in self.canciones if c[0] != titulo]


pl = Playlist()
pl.agregar_cancion("Canción A", 180)
pl.agregar_cancion("Canción B", 300)
print(f"Duración total: {pl.duracion_total()} segundos")
print(f"Largas (>200s): {pl.canciones_largas(200)}")