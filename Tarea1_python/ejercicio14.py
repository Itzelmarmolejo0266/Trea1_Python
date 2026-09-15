class RegistroNotas:
    def __init__(self):
        self.notas = {}
    def registrar(self, estudiante, nota):
        self.notas[estudiante] = nota
    def estudiantes_aprobados(self, nota_minima):
        return [
            nombre
            for nombre, nota in self.notas.items()
            if nota >= nota_minima
        ]
    def mejor_estudiante(self):
        mejor_nombre = max(self.notas, key=self.notas.get)
        return (mejor_nombre, self.notas[mejor_nombre])

registro = RegistroNotas()
registro.registrar("Ana", 85)
registro.registrar("Luis", 60)
registro.registrar("María", 95)
registro.registrar("Pedro", 70)
registro.registrar("Sofía", 45)

print("Registro de notas:", registro.notas)
print(
    "Estudiantes aprobados:",
    registro.estudiantes_aprobados(70)
)
print(
    "Mejor estudiante:",
    registro.mejor_estudiante()
)
# La clase RegistroNotas sirve para guardar las notas de estudiantes,
# encontrar cuáles aprobaron y saber quién obtuvo la mejor nota.

#Entrada
#Nombre del estudiante.
#Nota del estudiante.
#Nota mínima para aprobar.

#Proceso
#Se guardan los estudiantes y sus notas en un diccionario.
#Se recorren los registros para buscar estudiantes aprobados.
#Se comparan las notas para encontrar la más alta.

#Salida
#Diccionario con los estudiantes y sus notas.
#Lista de estudiantes aprobados.
#Tupla con el mejor estudiante y su nota.

#BOSQUEJO
# Ana tiene 85.
# Luis tiene 60.
# María tiene 95.
# Pedro tiene 70.
# Sofía tiene 45.
# Nota mínima para aprobar: 70.
# Estudiantes aprobados:
# Ana, María y Pedro.
# Mejor estudiante:
# María, con 95 puntos.

#TABLA 
# Estudiante    Nota    ¿Aprueba con 70?
# Ana           85      Sí
# Luis          60      No
# María         95      Sí
# Pedro         70      Sí
# Sofía         45      No

# Resultado esperado:
# Estudiantes aprobados: ['Ana', 'María', 'Pedro']
# Mejor estudiante: ('María', 95)
