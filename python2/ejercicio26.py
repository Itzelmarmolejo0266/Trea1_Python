class GestorSuscripciones:
    """Gestiona días restantes de suscripciones de usuarios."""

    def __init__(self):
        self.suscripciones = {}  # {usuario: dias_restantes}

    def agregar_suscripcion(self, usuario, dias):
        self.suscripciones[usuario] = dias

    def renovar(self, usuario, dias_extra):
        if usuario in self.suscripciones:
            self.suscripciones[usuario] += dias_extra

    def usuarios_vencidos(self):
        return [u for u, d in self.suscripciones.items() if d <= 0]

    def usuarios_activos(self):
        return [u for u, d in self.suscripciones.items() if d > 0]


gs = GestorSuscripciones()
gs.agregar_suscripcion("Ana", 5)
gs.agregar_suscripcion("Bob", 0)
gs.agregar_suscripcion("Carlos", -3)
print(f"Activos: {gs.usuarios_activos()}")
print(f"Vencidos: {gs.usuarios_vencidos()}")
gs.renovar("Bob", 10)
print(f"Activos tras renovar: {gs.usuarios_activos()}")