class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        if not letra.isalpha():
            return letra
        base = ord('A') if letra.isupper() else ord('a')
        posicion = (ord(letra) - base + desplazamiento) % 26
        return chr(base + posicion)

    def codificar_palabra(self, palabra, desplazamiento):
        codificada = ""
        for letra in palabra:
            codificada += self.codificar_letra(letra, desplazamiento)
        self.historial[palabra] = codificada
        return codificada

codificador = CodificadorCesar()
print("Palabra codificada:",
      codificador.codificar_palabra("HOLA", 2))
print("Otra palabra:",
      codificador.codificar_palabra("Python", 3))
print("Historial:", codificador.historial)

# La clase CodificadorCesar sirve para codificar letras y palabras
# desplazando cada letra una cantidad de posiciones en el abecedario.
#Entrada
#Una letra o palabra.
#Un número que indica el desplazamiento.

#Proceso
#Se revisa si el carácter es una letra.
#Se identifica si es mayúscula o minúscula.
#Se convierte la letra en un número usando ord().
#Se calcula la nueva posición.
#Se utiliza % 26 para volver al inicio del abecedario cuando
#se llega después de la letra Z.
#Se convierte nuevamente el número en letra usando chr().

#Salida
#Palabra codificada.
#Historial con la palabra original y la palabra codificada.

#BOSQUEJO
# Palabra:
# HOLA
# Desplazamiento:
# 2
# H + 2 = J
# O + 2 = Q
# L + 2 = N
# A + 2 = C
# Resultado:
# JQNC

#TABLA
# Palabra    Desplazamiento    Resultado
# HOLA       2                 JQNC
# Python     3                 Sbwkrq
# XYZ        2                 ZAB
# Resultado esperado:
# Palabra codificada: JQNC
# Otra palabra: Sbwkrq
