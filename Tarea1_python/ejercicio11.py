class ContadorFrecuencia:
    def __init__(self):
        self.frecuencias = {}

    def agregar_elemento(self, elemento):
        self.frecuencias[elemento] = self.frecuencias.get(elemento, 0) + 1

    def elemento_mas_frecuente(self):
        return max(self.frecuencias, key=self.frecuencias.get)

    def frecuencia_elemento(self, elemento):
        return self.frecuencias.get(elemento, 0)

contador = ContadorFrecuencia()
contador.agregar_elemento("rojo")
contador.agregar_elemento("azul")
contador.agregar_elemento("rojo")
contador.agregar_elemento("verde")
contador.agregar_elemento("azul")
contador.agregar_elemento("rojo")

print("Frecuencias:", contador.frecuencias)
print("Elemento más frecuente:", contador.elemento_mas_frecuente())
print("Frecuencia de rojo:", contador.frecuencia_elemento("rojo"))
print("Frecuencia de verde:", contador.frecuencia_elemento("verde"))
print("Frecuencia de amarillo:", contador.frecuencia_elemento("amarillo"))

# La clase ContadorFrecuencia sirve para contar cuántas veces
# aparece cada elemento.

#Entrada
#Elementos individuales, como "rojo" o "azul".

#Proceso
#Se guarda cada elemento en un diccionario.
#Si el elemento ya existe, se aumenta su contador.
#Si el elemento no existe, comienza con la cantidad 1.
#Se busca cuál elemento tiene la mayor cantidad.

#Salida
#Diccionario con las frecuencias.
#Elemento que aparece más veces.
#Cantidad de veces que aparece un elemento consultado.

# 2. BOSQUEJO 
# Elementos agregados:
# "rojo", "azul", "rojo", "verde", "azul", "rojo"

# Resultado:
# rojo  -> 3
# azul  -> 2
# verde -> 1

# El elemento más frecuente es "rojo".

#TABLA
# Elemento       Frecuencia
# rojo           3
# azul           2
# verde          1
# amarillo       0

# Resultado esperado:
# Elemento más frecuente: rojo
