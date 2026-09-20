class FiltroSpam:
    """Filtra correos según palabras prohibidas."""

    def __init__(self, palabras_prohibidas):
        self.palabras_prohibidas = palabras_prohibidas
        self.historial = []  # (correo, es_spam)

    def es_spam(self, texto):
        texto_min = texto.lower()
        resultado = any(palabra in texto_min for palabra in self.palabras_prohibidas)
        self.historial.append((texto, resultado))
        return resultado

    def filtrar_multiples(self, *correos):
        resultado = {'spam': [], 'legitimos': []}
        for correo in correos:
            if self.es_spam(correo):
                resultado['spam'].append(correo)
            else:
                resultado['legitimos'].append(correo)
        return resultado

    def cantidad_spam(self):
        return sum(1 for _, es in self.historial if es)


fs = FiltroSpam(["gratis", "premio", "urgente"])
clasificados = fs.filtrar_multiples(
    "Ganaste un premio", "Reunión mañana a las 10", "Oferta GRATIS solo hoy"
)
print(clasificados)
print(f"Cantidad spam: {fs.cantidad_spam()}")