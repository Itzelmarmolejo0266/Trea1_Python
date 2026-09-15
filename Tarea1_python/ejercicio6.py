class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for t in temps:
            self.registrar_temperatura(t)

gestor = GestorTemperatura()
gestor.registrar_temperatura(25)
gestor.registrar_multiples(30, 28, 32, 26)
print("Temperaturas:", gestor.temperaturas)
print("Temperatura mínima:", gestor.minima())
print("Temperatura máxima:", gestor.maxima())
print("Promedio:", gestor.promedio())

#Entrada
# La clase recibe temperaturas individuales o varias temperaturas
# mediante el parámetro *temps.

#Proceso
# El constructor crea una lista vacía llamada temperaturas.
# registrar_temperatura() agrega una temperatura a la lista.
# registrar_multiples() recorre varias temperaturas con un for
# y reutiliza registrar_temperatura().
# minima() busca el valor menor usando min().
# maxima() busca el valor mayor usando max().
# promedio() suma las temperaturas con sum() y divide
# para la cantidad de elementos obtenida con len().

#Salida
# La clase permite obtener:
# - La lista de temperaturas.
# - La temperatura mínima.
# - La temperatura máxima.
# - El promedio de las temperaturas.

# Bosquejo 
# Entrada: 25, 30, 28, 32, 26
# Lista final: [25, 30, 28, 32, 26]
# Mínima: 25
# Máxima: 32
# Promedio: 141 / 5 = 28.2

# Funciones utilizadas:
# - append(): agrega temperaturas a la lista.
# - min(): obtiene la temperatura menor.
# - max(): obtiene la temperatura mayor.
# - sum(): suma todas las temperaturas.
# - len(): cuenta cuántas temperaturas existen.

# Tabla pequeña:
# Temperatura | Acción
# 25          | Se agrega a la lista
# 30          | Se agrega a la lista
# 28          | Se agrega a la lista
# 32          | Se agrega a la lista
# 26          | Se agrega a la lista

# Resultado:
# Lista: [25, 30, 28, 32, 26]
# Mínima: 25
# Máxima: 32
# Promedio: 28.2