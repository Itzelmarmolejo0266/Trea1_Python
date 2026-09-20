class ConvertidorTemperatura:
    """Convierte temperaturas entre Celsius y Fahrenheit."""

    def __init__(self):
        self.historial = []  # (valor_original, unidad, resultado)

    def celsius_a_fahrenheit(self, c):
        resultado = c * 9 / 5 + 32
        self.historial.append((c, "C", resultado))
        return resultado

    def fahrenheit_a_celsius(self, f):
        resultado = (f - 32) * 5 / 9
        self.historial.append((f, "F", resultado))
        return resultado

    def convertir_multiples(self, unidad_origen, *valores):
        resultados = []
        for valor in valores:
            if unidad_origen == "C":
                resultados.append(self.celsius_a_fahrenheit(valor))
            else:
                resultados.append(self.fahrenheit_a_celsius(valor))
        return resultados


ct = ConvertidorTemperatura()
print(ct.convertir_multiples("C", 0, 100))
print(f"Historial: {ct.historial}")