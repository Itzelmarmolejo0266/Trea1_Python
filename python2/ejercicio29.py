class SistemaVotacion:
    """Gestiona votos para una lista fija de candidatos."""

    def __init__(self, candidatos):
        self.votos = {c: 0 for c in candidatos}

    def votar(self, candidato):
        if candidato not in self.votos:
            return False
        self.votos[candidato] += 1
        return True

    def votar_multiples(self, *candidatos):
        for candidato in candidatos:
            self.votar(candidato)

    def ganador(self):
        return max(self.votos, key=self.votos.get)

    def total_votos(self):
        return sum(self.votos.values())


sv = SistemaVotacion(["A", "B", "C"])
sv.votar_multiples("A", "B", "A", "A")
print(f"Votos: {sv.votos}")
print(f"Ganador: {sv.ganador()}")
print(f"Total votos: {sv.total_votos()}")