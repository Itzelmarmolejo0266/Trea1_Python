class ValidadorEmail:
    """Valida formato básico de correos electrónicos."""

    def __init__(self):
        self.historial = []

    def _cumple_formato(self, correo):
        """Regla de validación pura, sin efectos secundarios."""
        if " " in correo:
            return False
        if correo.count("@") != 1:
            return False
        usuario, dominio = correo.split("@")
        if len(usuario) == 0 or "." not in dominio:
            return False
        return True

    def es_valido(self, correo):
        self.historial.append(correo)
        return self._cumple_formato(correo)

    def validar_multiples(self, *correos):
        resultado = {'validos': [], 'invalidos': []}
        for correo in correos:
            if self.es_valido(correo):
                resultado['validos'].append(correo)
            else:
                resultado['invalidos'].append(correo)
        return resultado

    def cantidad_validos(self):
        return sum(1 for correo in self.historial if self._cumple_formato(correo))


ve = ValidadorEmail()
clasificados = ve.validar_multiples("ana@correo.com", "ana correo.com", "bob@@x.com")
print(clasificados)
print(f"Válidos en total: {ve.cantidad_validos()}")