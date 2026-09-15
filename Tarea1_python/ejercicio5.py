class AnalizadorNumeros:
    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        resultado = {"pares": [], "impares": []}
        for n in numeros:
            if self.es_par(n):
                resultado["pares"].append(n)
            else:
                resultado["impares"].append(n)
        self.ultimo_resultado = resultado
        return resultado

    def cantidad_pares_impares(self):
        return (
            len(self.ultimo_resultado["pares"]),
            len(self.ultimo_resultado["impares"])
        )

analizador = AnalizadorNumeros()
print(analizador.separar(10, 5, 8, 3, 7, 2))
print(analizador.cantidad_pares_impares())

#Entrada
# La clase recibe varios números mediante *numeros.

# Proceso
# El método es_par() verifica si cada número es divisible entre 2.
# El método separar() recorre los números con un for.
# Si el número es par, se guarda en la lista "pares".
# Si no es par, se guarda en la lista "impares".
# Después, el resultado se guarda en self.ultimo_resultado.
# El método cantidad_pares_impares() cuenta los elementos de ambas listas.

# S: Salida
# separar() retorna un diccionario con dos listas:
# "pares" e "impares".
# cantidad_pares_impares() retorna una tupla con dos cantidades:
# (cantidad_de_pares, cantidad_de_impares).

# Bosquejo
# Entrada: 10, 5, 8, 3, 7, 2
# Pares: [10, 8, 2]
# Impares: [5, 3, 7]
# Cantidades: (3, 3)

# Tabla pequeña:
# Número | Resultado de % 2 | Clasificación
# 10     | 0               | Par
# 5      | 1               | Impar
# 8      | 0               | Par
# 3      | 1               | Impar