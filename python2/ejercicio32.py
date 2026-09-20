class Estacionamiento:
    """Gestiona el ingreso y salida de vehículos según capacidad."""

    def __init__(self, capacidad_total):
        self.capacidad_total = capacidad_total
        self.vehiculos = []  # placas dentro del estacionamiento

    def ingresar_vehiculo(self, placa):
        if len(self.vehiculos) >= self.capacidad_total:
            return False
        self.vehiculos.append(placa)
        return True

    def salir_vehiculo(self, placa):
        if placa in self.vehiculos:
            self.vehiculos.remove(placa)
            return True
        return False

    def espacios_disponibles(self):
        return self.capacidad_total - len(self.vehiculos)


est = Estacionamiento(2)
print(est.ingresar_vehiculo("ABC123"))  # True
print(est.ingresar_vehiculo("XYZ789"))  # True
print(est.ingresar_vehiculo("DEF456"))  # False, lleno
print(f"Disponibles: {est.espacios_disponibles()}")
est.salir_vehiculo("ABC123")
print(f"Disponibles tras salida: {est.espacios_disponibles()}")