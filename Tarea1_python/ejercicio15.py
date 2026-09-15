class DivisorFinder:
    def encontrar_divisores(self, numero):
        divisores = []
        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores.append(i)
        return tuple(divisores)
    
    def es_perfecto(self, numero):
        divisores = self.encontrar_divisores(numero)
        suma_propios = sum(divisores) - numero
        return suma_propios == numero

    def encontrar_multiples_divisores(self, *numeros):
        resultado = {}
        for n in numeros:
            resultado[n] = self.encontrar_divisores(n)
        return resultado

divisor = DivisorFinder()

print("Divisores de 6:", divisor.encontrar_divisores(6))
print("¿6 es perfecto?:", divisor.es_perfecto(6))
print("¿8 es perfecto?:", divisor.es_perfecto(8))
print(
    "Divisores de varios números:",
    divisor.encontrar_multiples_divisores(6, 8, 10, 12)
)
# La clase DivisorFinder sirve para encontrar los divisores de un
# número, comprobar si es un número perfecto y buscar los divisores
# de varios números.

#Entrada
#Uno o varios números enteros.

#Proceso
#Se revisan los números desde 1 hasta el número recibido.
#Se utiliza el operador % para comprobar si la división es exacta.
#Los divisores encontrados se guardan en una lista.
#La lista se convierte en una tupla.
#Para comprobar si un número es perfecto, se suman sus divisores
#y se resta el número original.
#Para varios números, se guardan los resultados en un diccionario.

#Salida
#Tupla con los divisores de un número.
#True o False para saber si el número es perfecto.
#Diccionario con varios números y sus divisores.

#BOSQUEJO
# Número: 6
# Divisores:
# 1, 2, 3 y 6.
# Divisores propios:
# 1, 2 y 3.
# Suma de divisores propios:
# 1 + 2 + 3 = 6.
# Como la suma es igual al número, 6 es perfecto.
# Número: 8
# Divisores:
# 1, 2, 4 y 8.
# Divisores propios:
# 1, 2 y 4.
# Suma:
# 1 + 2 + 4 = 7.

# Como 7 no es igual a 8, el número no es perfecto.

#TABLA
# Número    Divisores             ¿Es perfecto?
# 6         1, 2, 3, 6            Sí
# 8         1, 2, 4, 8            No
# 10        1, 2, 5, 10           No

# Resultado esperado:
# Divisores de 6: (1, 2, 3, 6)
# ¿6 es perfecto?: True
# ¿8 es perfecto?: False

 