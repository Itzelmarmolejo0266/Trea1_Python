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

print("Lista invertida:", inversor.invertir_lista([1, 2, 3, 4]))
print("Varias listas invertidas:",
      inversor.invertir_multiples(
          [1, 2, 3],
          [10, 20, 30]
      ))

# Entrada:
# Recibe una lista individual o varias listas.

# Proceso:
# Recorre cada lista desde la última posición hasta
# la primera y guarda sus elementos en una nueva lista.
# Cuando recibe varias listas, guarda cada resultado
# en un diccionario.

# Salida:
# Devuelve una lista invertida o un diccionario
# con las listas originales y sus versiones invertidas.


#  BOSQUEJO
#
# Lista original:
# [1, 2, 3, 4]
#
# Posiciones:
# 0 = 1
# 1 = 2
# 2 = 3
# 3 = 4
#
# Recorrido inverso:
# 3, 2, 1, 0
#
# Resultado:
# [4, 3, 2, 1]
#
# Varias listas:
# [1, 2, 3] -> [3, 2, 1]
# [10, 20, 30] -> [30, 20, 10]


#TABLA PEQUEÑA
#
# Lista original    Resultado invertido
# [1, 2, 3]         [3, 2, 1]
# [10, 20, 30]      [30, 20, 10]
#
# Diccionario final:
# {
#     (1, 2, 3): [3, 2, 1],
#     (10, 20, 30): [30, 20, 10]
# }