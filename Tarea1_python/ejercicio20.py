class AnalizadorPatrones:
    def __init__(self):
        self.ultimo_texto = ""
    def encontrar_palabras(self, texto, patron):
        self.ultimo_texto = texto
        palabras = texto.split()
        return [p for p in palabras if p.startswith(patron)]
    def agrupar_por_longitud(self, texto):
        self.ultimo_texto = texto
        resultado = {}
        for palabra in texto.split():
            longitud = len(palabra)
            if longitud not in resultado:
                resultado[longitud] = []
            resultado[longitud].append(palabra)
        return resultado
    def palabras_unicas(self):
        return set(self.ultimo_texto.split())

analizador = AnalizadorPatrones()
texto = "casa carro perro casa mesa pelota"
print("Palabras con 'ca':",
      analizador.encontrar_palabras(texto, "ca"))
print("Palabras agrupadas por longitud:",
      analizador.agrupar_por_longitud(texto))
print("Palabras únicas:",
      analizador.palabras_unicas())
#ENTRADA
# Recibimos un texto y, en algunos métodos,
# también recibimos un patrón.

# Ejemplo:
# texto = "casa carro perro casa mesa pelota"
# patrón = "ca"


#PROCESO
# 1. split() separa el texto en palabras.
# 2. encontrar_palabras() busca las palabras
#    que comienzan con el patrón.
# 3. agrupar_por_longitud() cuenta las letras
#    de cada palabra y las guarda en un diccionario.
# 4. palabras_unicas() utiliza set() para eliminar
#    las palabras repetidas.

#SALIDA
#una lista de palabras que coinciden con el patrón,
#un diccionario agrupado por longitud,
#un conjunto de palabras únicas.

# BOSQUEJO:
# Texto:
# "casa carro perro casa mesa pelota"
# Patrón "ca":
# casa  -> sí
# carro -> sí
# perro -> no
# casa  -> sí
# Resultado:
# ["casa", "carro", "casa"]

# AGRUPACIÓN:
# 4 letras -> ["casa", "casa", "mesa"]
# 5 letras -> ["carro", "perro"]
# 6 letras -> ["pelota"]
# PALABRAS ÚNICAS:
# {"casa", "carro", "perro", "mesa", "pelota"}

# VERIFICACIÓN:
# Operación              Resultado
# Buscar "ca"            ["casa", "carro", "casa"]
# 4 letras               ["casa", "casa", "mesa"]
# 5 letras               ["carro", "perro"]
# 6 letras               ["pelota"]
# Palabras únicas        5 palabras