class CalculadorDistancia:
    def __init__(self):
        self.distancias_calculadas = []
    def distancia_euclidiana(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        self.distancias_calculadas.append(distancia)
        return distancia
    def punto_mas_cercano(self, referencia, *puntos):
        mas_cercano = None
        menor_distancia = float("inf")
        for punto in puntos:
            d = self.distancia_euclidiana(referencia, punto)
            if d < menor_distancia:
                menor_distancia = d
                mas_cercano = punto
        return mas_cercano
calculador = CalculadorDistancia()
punto1 = (2, 3)
punto2 = (5, 7)
print("Distancia:", calculador.distancia_euclidiana(punto1, punto2))
referencia = (0, 0)
puntos = (3, 4), (1, 2), (6, 5), (8, 1)
print("Punto más cercano:", calculador.punto_mas_cercano(referencia, *puntos))
#ENTRADA
# Recibimos puntos representados como tuplas (x, y).
# Ejemplo:
# punto1 = (2, 3)
# punto2 = (5, 7)
# También recibimos un punto de referencia y varios
# puntos para encontrar cuál está más cerca.

#PROCESO
# 1. distancia_euclidiana() separa las coordenadas x e y.
# 2. Aplica la fórmula de distancia entre dos puntos.
# 3. Guarda cada distancia calculada en una lista.
# 4. punto_mas_cercano() revisa varios puntos.
# 5. Compara las distancias y conserva la menor.

#SALIDA
#Se obtiene:
#La distancia entre dos puntos.
#El punto más cercano a una referencia.

# BOSQUEJO:
# Punto 1 = (2, 3)
# Punto 2 = (5, 7)
# Distancia = 5.0

# Referencia = (0, 0)
# Puntos:
# (3, 4) -> 5.0
# (1, 2) -> 2.24
# (6, 5) -> 7.81
# (8, 1) -> 8.06
# El punto más cercano es (1, 2).
# VERIFICACIÓN:
# Punto       Distancia desde (0,0)
# (3,4)       5.0
# (1,2)       2.24
# (6,5)       7.81
# (8,1)       8.06
# Menor distancia -> 2.24
# Punto más cercano -> (1,2)