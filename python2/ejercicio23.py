class AgendaCitas:
    """Gestiona horarios disponibles y reservados para citas."""

    def __init__(self, horarios):
        self.disponibles = list(horarios)  # copia, no la lista original
        self.reservas = {}  # {hora: nombre}

    def reservar_hora(self, hora, nombre):
        if hora not in self.disponibles:
            return False
        self.disponibles.remove(hora)
        self.reservas[hora] = nombre
        return True

    def cancelar_cita(self, hora):
        if hora in self.reservas:
            del self.reservas[hora]
            self.disponibles.append(hora)

    def horarios_libres(self):
        return self.disponibles


ac = AgendaCitas(["9:00", "10:00", "11:00"])
print(ac.reservar_hora("9:00", "Ana"))       # True
print(ac.reservar_hora("9:00", "Bob"))       # False, ya está ocupada
print(f"Libres: {ac.horarios_libres()}")
ac.cancelar_cita("9:00")
print(f"Libres tras cancelar: {ac.horarios_libres()}")