class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto
        conteo = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }
        for caracter in texto:

            if caracter.isdigit():
                conteo["digitos"] += 1

            elif caracter.isalpha():

                if self.solo_vocales(caracter):
                    conteo["vocales"] += 1
                else:
                    conteo["consonantes"] += 1
        return conteo

analizador = AnalizadorString()

print(analizador.contar_por_tipo("Hola123"))
print("Texto más largo:", analizador.texto_mas_largo)
print(analizador.contar_por_tipo("Python2026"))
print("Texto más largo:", analizador.texto_mas_largo)

#Entrada
# La clase recibe un texto mediante el método contar_por_tipo().
# También recibe una letra en el método solo_vocales().

#Proceso
# El constructor crea el atributo texto_mas_largo con una cadena vacía.
# contar_por_tipo() compara la longitud del texto recibido con
# la longitud del texto más largo guardado.
# Si el texto nuevo es más largo, se actualiza el atributo.
# Después se crea un diccionario con tres contadores:
# vocales, consonantes y digitos.
# El texto se recorre carácter por carácter usando un for.
# Si el carácter es un dígito, aumenta el contador de digitos.
# Si el carácter es una letra, se utiliza solo_vocales()
# para comprobar si es una vocal.
# Si es vocal, aumenta el contador de vocales.
# Si no es vocal, aumenta el contador de consonantes.

#Salida
# contar_por_tipo() retorna un diccionario con:
# - Cantidad de vocales.
# - Cantidad de consonantes.
# - Cantidad de dígitos.
# Además, se guarda el texto más largo en self.texto_mas_largo.

# Bosquejo
# Texto: "Hola123"
# Vocales: o, a = 2
# Consonantes: H, l = 2
# Dígitos: 1, 2, 3 = 3
# Resultado:
# {"vocales": 2, "consonantes": 2, "digitos": 3}


# Métodos y funciones utilizados:
# - len(): cuenta caracteres.
# - lower(): convierte una letra a minúscula.
# - isdigit(): verifica si es un dígito.
# - isalpha(): verifica si es una letra.

# Tabla pequeña:
# Carácter | Clasificación
# H        | Consonante
# o        | Vocal
# l        | Consonante
# a        | Vocal
# 1        | Dígito
# 2        | Dígito
# 3        | Dígito
#
# Resultado final:
# {"vocales": 2, "consonantes": 2, "digitos": 3}