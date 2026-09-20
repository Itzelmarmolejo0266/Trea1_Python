class CalculadoraDescuento:
    """Calcula descuentos según el volumen de compra."""

    def __init__(self):
        self.historial = []  # totales facturados

    def calcular_descuento(self, cantidad):
        if cantidad >= 50:
            return 20
        elif cantidad >= 10:
            return 10
        else:
            return 0

    def calcular_total(self, precio_unitario, cantidad):
        subtotal = precio_unitario * cantidad
        descuento = self.calcular_descuento(cantidad)
        total = subtotal * (1 - descuento / 100)
        self.historial.append(total)
        return total

    def procesar_pedidos(self, *pedidos):
        totales = []
        for precio, cantidad in pedidos:
            totales.append(self.calcular_total(precio, cantidad))
        return totales

    def total_facturado(self):
        return sum(self.historial)


cd = CalculadoraDescuento()
totales = cd.procesar_pedidos((10, 60), (5, 5), (20, 15))
print(f"Totales: {totales}")
print(f"Total facturado: {cd.total_facturado()}")