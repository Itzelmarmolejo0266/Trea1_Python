class CombinadorListas:
    def intercalar(self, lista1, lista2):
        resultado = []
        largo_maximo = max(len(lista1), len(lista2))
        for i in range(largo_maximo):
            if i < len(lista1):
                resultado.append(lista1[i])
            if i < len(lista2):
                resultado.append(lista2[i])
        return resultado

    def intercalar_multiples(self, *listas):
        resultado = list(listas[0])
        for siguiente in listas[1:]:
            resultado = self.intercalar(resultado, siguiente)
        return resultado
combinador = CombinadorListas()
print(
    "Dos listas intercaladas:",
    combinador.intercalar(
        [1, 2, 3],
        ["a", "b", "c"]
    )
)
print(
    "Varias listas intercaladas:",
    combinador.intercalar_multiples(
        [1, 2],
        ["a", "b", "c"],
        [10, 20, 30, 40]
    )
)
# La clase CombinadorListas sirve para combinar dos o más listas
# alternando sus elementos por posición.

#Entrada
#Dos listas para el método intercalar().
#Dos o más listas para el método intercalar_multiples().

#Proceso
#Se revisa el tamaño de las listas.
#Se recorren sus posiciones mediante un for.
#Se agrega un elemento de la primera lista.
#Después se agrega un elemento de la segunda lista.
#Si una lista es más corta, se verifica que la posición exista.
#Para varias listas, se reutiliza el método intercalar().

#Salida
#Una lista con los elementos intercalados.

#BOSQUEJO
# Primera lista:
# [1, 2, 3]

# Segunda lista:
# ["a", "b", "c"]

# Resultado:
# [1, "a", 2, "b", 3, "c"]

# Para varias listas:
# Lista 1: [1, 2]
# Lista 2: ["a", "b", "c"]
# Lista 3: [10, 20, 30, 40]

# Resultado:
# [1, 10, "a", 20, 2, 30, "b", 40, "c"]


#self.intercalar():
#Reutiliza el método intercalar() para no repetir código.

#len():
#Cuenta cuántos elementos tiene una lista.
#max():
#Obtiene el tamaño de la lista más larga.
#range():
#Permite recorrer los índices de las listas.
#append():
#   Agrega elementos a la lista resultado.

#TABLA
# Lista 1: [1, 2, 3]
# Lista 2: ["a", "b", "c"]

# Índice 0 -> 1, "a"
# Índice 1 -> 2, "b"
# Índice 2 -> 3, "c"

# Resultado esperado:
# [1, "a", 2, "b", 3, "c"]
