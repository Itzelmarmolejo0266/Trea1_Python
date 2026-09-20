class ReservasMesas:
    """Gestiona reservas de mesas según capacidad del restaurante."""

    def __init__(self, total_mesas):
        self.total_mesas = total_mesas
        self.reservas = []  # (nombre, personas)

    def reservar_mesa(self, nombre, personas):
        if len(self.reservas) >= self.total_mesas:
            return False
        self.reservas.append((nombre, personas))
        return True

    def cancelar_reserva(self, nombre):
        self.reservas = [r for r in self.reservas if r[0] != nombre]

    def mesas_disponibles(self):
        return self.total_mesas - len(self.reservas)


rm = ReservasMesas(2)
print(rm.reservar_mesa("Ana", 4))      # True
print(rm.reservar_mesa("Bob", 2))      # True
print(rm.reservar_mesa("Carlos", 3))   # False
rm.cancelar_reserva("Ana")
print(f"Disponibles: {rm.mesas_disponibles()}")