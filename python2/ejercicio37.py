class AnalizadorClima:
    """Analiza temperaturas registradas por día."""

    def __init__(self):
        self.temperaturas = {}  # {dia: temp}

    def registrar_temperatura(self, dia, temp):
        self.temperaturas[dia] = temp

    def dia_mas_caluroso(self):
        if not self.temperaturas:
            return None
        return max(self.temperaturas, key=self.temperaturas.get)

    def dia_mas_frio(self):
        if not self.temperaturas:
            return None
        return min(self.temperaturas, key=self.temperaturas.get)

    def promedio_semanal(self):
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas.values()) / len(self.temperaturas)


acl = AnalizadorClima()
acl.registrar_temperatura("Lunes", 25)
acl.registrar_temperatura("Martes", 30)
acl.registrar_temperatura("Miércoles", 18)
print(f"Más caluroso: {acl.dia_mas_caluroso()}")
print(f"Más frío: {acl.dia_mas_frio()}")
print(f"Promedio: {acl.promedio_semanal()}")