class SelectorRango:
    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin + 1))

    def elementos_en_multiples_rangos(self, *rangos):
        combinados = set()
        for inicio, fin in rangos:
            for numero in self.crear_rango(inicio, fin):
                combinados.add(numero)
        return sorted(combinados)

selector = SelectorRango()
print("Primer rango:", selector.crear_rango(1, 5))
print(
    "Números combinados:",
    selector.elementos_en_multiples_rangos(
        (1, 5),
        (4, 8),
        (10, 12)
    )
)
# La clase SelectorRango permite crear rangos de números y combinar
# varios rangos evitando que los números se repitan.

#Entrada
#Un número inicial.
#Un número final.
#Varios pares de números que representan rangos.

#Proceso
#Se crea cada rango utilizando range().
#Se convierte el rango en una tupla.
#Se recorren los rangos recibidos.
#Se agregan los números a un conjunto set.
#El set elimina automáticamente los números duplicados.
#Se ordenan los números de menor a mayor.

#Salida
#Un rango representado como tupla.
#Una lista ordenada con todos los números sin duplicados.

#BOSQUEJO
# Rango 1: (1, 5)
# Números: 1, 2, 3, 4, 5
# Rango 2: (4, 8)
# Números: 4, 5, 6, 7, 8
# Rango 3: (10, 12)
# Números: 10, 11, 12
# Los números 4 y 5 se repiten, pero el set los guarda una sola vez.
# Resultado final:
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]

#TABLA
# Rango       Números
# (1, 5)      1, 2, 3, 4, 5
# (4, 8)      4, 5, 6, 7, 8
# (10, 12)    10, 11, 12

# Resultado esperado:
# [1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12]
