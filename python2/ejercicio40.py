class PromedioPonderado:
    """Calcula promedio ponderado de notas con distintos pesos."""

    def __init__(self):
        self.notas = []  # (nota, peso)

    def agregar_nota(self, nota, peso):
        self.notas.append((nota, peso))

    def calcular_promedio(self):
        if not self.notas:
            return 0
        suma_ponderada = sum(nota * peso for nota, peso in self.notas)
        suma_pesos = sum(peso for _, peso in self.notas)
        return suma_ponderada / suma_pesos

    def aprobado(self, nota_minima):
        return self.calcular_promedio() >= nota_minima


pp = PromedioPonderado()
pp.agregar_nota(90, 0.4)  # examen, 40%
pp.agregar_nota(80, 0.3)  # tareas, 30%
pp.agregar_nota(70, 0.3)  # proyecto, 30%
print(f"Promedio ponderado: {pp.calcular_promedio()}")
print(f"¿Aprobado (>=70)?: {pp.aprobado(70)}")