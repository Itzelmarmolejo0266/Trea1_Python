class OrganizadorTareas:
    """Organiza tareas según sus días restantes."""

    def __init__(self):
        self.tareas = []  # (nombre, dias_restantes)

    def agregar_tarea(self, nombre, dias_restantes):
        self.tareas.append((nombre, dias_restantes))

    def tareas_urgentes(self, limite):
        return [t for t in self.tareas if t[1] <= limite]

    def tarea_mas_urgente(self):
        if not self.tareas:
            return None
        return min(self.tareas, key=lambda t: t[1])

    def eliminar_tarea(self, nombre):
        self.tareas = [t for t in self.tareas if t[0] != nombre]


ot = OrganizadorTareas()
ot.agregar_tarea("Informe", 2)
ot.agregar_tarea("Examen", 5)
ot.agregar_tarea("Pago", 1)
print(f"Urgentes (<=3 días): {ot.tareas_urgentes(3)}")
print(f"Más urgente: {ot.tarea_mas_urgente()}")
ot.eliminar_tarea("Pago")
print(f"Tras eliminar: {ot.tareas}")  