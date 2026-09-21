class InversorSecuencia:

    def invertir_lista(self, lista):
        invertida = []

        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])

        return invertida

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            clave = tuple(lista)
            resultado[clave] = self.invertir_lista(lista)

        return resultado


inversor = InversorSecuencia()

print("Lista invertida:", inversor.invertir_lista([5, 10, 15, 20]))

print("Varias listas invertidas:",
      inversor.invertir_multiples(
          [2, 4, 6, 8],
          [100, 200, 300],
          [7, 14, 21, 28]
      ))


# Entrada:
# Recibe una lista individual o varias listas.
#
# Ejemplo:
# [5, 10, 15, 20]
#
# También puede recibir:
# [2, 4, 6, 8]
# [100, 200, 300]
# [7, 14, 21, 28]


# Proceso:
# Recorre cada lista desde la última posición
# hasta la primera y guarda los elementos
# en una nueva lista.
#
# Cuando recibe varias listas, guarda cada
# resultado invertido dentro de un diccionario.


# Salida:
# Devuelve una lista invertida o un diccionario
# con las listas originales y sus versiones invertidas.


# BOSQUEJO
#
# Lista original:
# [5, 10, 15, 20]
#
# Posiciones:
#  0 = 5
#  1 = 10
#  2 = 15
#  3 = 20
#
# Recorrido inverso:
# 3, 2, 1, 0
#
# Resultado:
# [20, 15, 10, 5]
#
#
# Varias listas:
#
# [2, 4, 6, 8] -> [8, 6, 4, 2]
#
# [100, 200, 300] -> [300, 200, 100]
#
# [7, 14, 21, 28] -> [28, 21, 14, 7]


# TABLA PEQUEÑA
#
# Lista original       Resultado invertido
# [5, 10, 15, 20]      [20, 15, 10, 5]
# [2, 4, 6, 8]          [8, 6, 4, 2]
# [100, 200, 300]       [300, 200, 100]
# [7, 14, 21, 28]       [28, 21, 14, 7]
#
#
# Diccionario final:
#
# {
#     (2, 4, 6, 8): [8, 6, 4, 2],
#     (100, 200, 300): [300, 200, 100],
#     (7, 14, 21, 28): [28, 21, 14, 7]
# }
