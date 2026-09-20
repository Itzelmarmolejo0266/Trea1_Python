class RastreadorGastos:
    """Rastrea gastos agrupados por categoría."""

    def __init__(self):
        self.gastos = {}  # {categoria: [montos]}

    def registrar_gasto(self, categoria, monto):
        if categoria not in self.gastos:
            self.gastos[categoria] = []
        self.gastos[categoria].append(monto)

    def total_por_categoria(self, categoria):
        return sum(self.gastos.get(categoria, []))

    def gasto_total(self):
        total = 0
        for montos in self.gastos.values():
            total += sum(montos)
        return total

    def categoria_mayor_gasto(self):
        if not self.gastos:
            return None
        return max(self.gastos, key=lambda c: sum(self.gastos[c]))


rg = RastreadorGastos()
rg.registrar_gasto("Comida", 20)
rg.registrar_gasto("Comida", 15)
rg.registrar_gasto("Transporte", 10)
print(f"Comida: {rg.total_por_categoria('Comida')}")
print(f"Total: {rg.gasto_total()}")
print(f"Mayor gasto: {rg.categoria_mayor_gasto()}")