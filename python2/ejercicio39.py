class ConvertidorLongitud:
    """Convierte longitudes entre metros y pies."""

    def __init__(self):
        self.historial = []  # (valor_original, unidad, resultado)

    def metros_a_pies(self, metros):
        resultado = metros * 3.281
        self.historial.append((metros, "m", resultado))
        return resultado

    def pies_a_metros(self, pies):
        resultado = pies / 3.281
        self.historial.append((pies, "ft", resultado))
        return resultado

    def convertir_multiples(self, unidad_origen, *valores):
        resultados = []
        for valor in valores:
            if unidad_origen == "m":
                resultados.append(self.metros_a_pies(valor))
            else:
                resultados.append(self.pies_a_metros(valor))
        return resultados


cl = ConvertidorLongitud()
print(cl.convertir_multiples("m", 1, 10))
print(f"Historial: {cl.historial}")