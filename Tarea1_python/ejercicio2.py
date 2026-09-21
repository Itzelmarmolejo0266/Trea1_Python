class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas = set()
        self.orden_palabras = []

    def agregar_palabra(self, palabra):
        # Entrada:
        # Recibe colores individuales mediante agregar_palabra()
        # o varios colores mediante agregar_multiples(*args).

        if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)

        # Proceso:
        # Guarda los colores en un conjunto para evitar duplicados
        # y en una lista para mantener el orden de llegada.
        # Después cuenta cuántos colores únicos existen.

    def contar_palabras(self):
        return len(self.palabras_unicas)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


at = AnalizadorTexto()

at.agregar_multiples("rojo", "azul", "verde", "rojo", "amarillo")

print(at.palabras_unicas)
print(at.orden_palabras)
print(at.contar_palabras())

