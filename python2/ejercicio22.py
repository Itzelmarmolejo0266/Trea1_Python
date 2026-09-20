class ContadorAsistencia:
    

    def __init__(self):
        self.eventos = {}  

    def registrar_asistente(self, evento, nombre):
        if evento not in self.eventos:
            self.eventos[evento] = []
        self.eventos[evento].append(nombre)

    def registrar_multiples(self, evento, *nombres):
        for nombre in nombres:
            self.registrar_asistente(evento, nombre)

    def asistentes_evento(self, evento):
        return self.eventos.get(evento, [])

    def evento_mas_concurrido(self):
        if not self.eventos:
            return None
        return max(self.eventos, key=lambda ev: len(self.eventos[ev]))

ca = ContadorAsistencia()
ca.registrar_multiples("Concierto", "Ana", "Bob", "Carlos")
ca.registrar_multiples("Teatro", "Ana", "ja", "hache", "Boby", "Carla")
print(f"Asistentes a Concierto: {ca.asistentes_evento('Concierto')}")
print(f"Evento más concurrido: {ca.evento_mas_concurrido()}")