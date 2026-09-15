class AgrupadorEdades:
    def __init__(self):
        self.grupos = {}
    def clasificar_edad(self, edad):
        if edad < 13:
            return "niño"
        elif edad < 18:
            return "adolescente"
        elif edad < 60:
            return "adulto"
        else:
            return "mayor"
    def agrupar_por_categoria(self, *edades):
        resultado = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }
        for edad in edades:
            categoria = self.clasificar_edad(edad)
            resultado[categoria].append(edad)
        self.grupos = resultado
        return resultado
    def edad_promedio_categoria(self, categoria):
        edades = self.grupos.get(categoria, [])
        if not edades:
            return 0
        return sum(edades) / len(edades)

agrupador = AgrupadorEdades()
resultado = agrupador.agrupar_por_categoria(
    8, 12, 15, 17, 20, 25, 34, 45, 61, 70)

print("Grupos:", resultado)
print("Promedio de niños:", agrupador.edad_promedio_categoria("niño"))
print("Promedio de adolescentes:", agrupador.edad_promedio_categoria("adolescente"))
print("Promedio de adultos:", agrupador.edad_promedio_categoria("adulto"))
print("Promedio de mayores:", agrupador.edad_promedio_categoria("mayor"))
#ENTRADA
# Recibimos varias edades:
# 8, 12, 15, 17, 20, 25, 34, 45, 61, 70
#PROCESO
# 1. clasificar_edad() determina si cada edad es:
#    niño, adolescente, adulto o mayor.
# 2. agrupar_por_categoria() coloca cada edad
#    dentro de la lista correspondiente.
# 3. edad_promedio_categoria() suma las edades
#    y las divide para saber el promedio.
#SALIDA
# Se muestra el diccionario con las edades agrupadas
# y el promedio de cada categoría.

# BOSQUEJO:
# 8, 12       -> niño
# 15, 17      -> adolescente
# 20,25,34,45 -> adulto
# 61,70       -> mayor

# VERIFICACIÓN:
# Categoría       Edades              Promedio
# niño            [8, 12]            10.0
# adolescente     [15, 17]           16.0
# adulto          [20,25,34,45]      31.0
# mayor           [61,70]            65.5