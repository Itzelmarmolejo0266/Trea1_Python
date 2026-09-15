class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        mayores = []
        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                mayores.append(nombre)
        return mayores

    def edad_promedio(self):
        if not self.personas:
            return 0
        return sum(self.personas.values()) / len(self.personas)

gestor = GestorPersonas()

gestor.agregar_persona("Ana", 20)
gestor.agregar_persona("Luis", 15)
gestor.agregar_persona("María", 25)
gestor.agregar_persona("Pedro", 17)

print("Personas registradas:", gestor.personas)
print("Personas mayores o iguales a 18:",
      gestor.personas_mayores(18))
print("Edad promedio:", gestor.edad_promedio())

#Entrada
# La clase recibe nombres y edades mediante agregar_persona().
# También recibe una edad mínima para buscar personas mayores.

#Proceso
# El constructor crea un diccionario vacío llamado personas.
# El nombre se utiliza como clave y la edad como valor.
# agregar_persona() guarda cada nombre con su edad.
# personas_mayores() recorre el diccionario con .items().
# Si la edad es mayor o igual a edad_minima, agrega el nombre
# a la lista mayores.
# edad_promedio() obtiene las edades con .values(),
# las suma con sum() y divide para la cantidad de personas
# usando len().
# Si no existen personas, retorna 0 para evitar dividir entre cero.

#Salida
# La clase permite obtener:
# - El diccionario de personas registradas.
# - Una lista con los nombres que cumplen la edad mínima.
# - El promedio de las edades.

# Bosquejo 
# Personas:
# Ana: 20
# Luis: 15
# María: 25
# Pedro: 17

# Edad mínima: 18
# Personas mayores o iguales a 18:
# ["Ana", "María"]

# Promedio:
# (20 + 15 + 25 + 17) / 4 = 19.25

# Funciones y métodos utilizados:
# - items(): obtiene claves y valores del diccionario.
# - values(): obtiene solamente las edades.
# - append(): agrega nombres a la lista.
# - sum(): suma las edades.
# - len(): cuenta las personas.

# Tabla pequeña:
# Nombre | Edad | ¿Mayor o igual a 18?
# Ana    | 20   | Sí
# Luis   | 15   | No
# María  | 25   | Sí
# Pedro  | 17   | No

# Resultado:
# Personas mayores o iguales a 18: ["Ana", "María"]
# Edad promedio: 19.25