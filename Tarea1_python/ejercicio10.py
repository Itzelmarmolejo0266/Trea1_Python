class Tareas:
    def __init__(self):
        self.tareas = []
    def agregar_tarea(self, descripcion, prioridad):
        self.tareas.append((descripcion, prioridad))
    def tareas_prioritarias(self):
        return [t for t in self.tareas if t[1] == "alta"]
    def eliminar_completada(self, descripcion):
        self.tareas = [t for t in self.tareas if t[0] != descripcion]

lista_tareas = Tareas()

lista_tareas.agregar_tarea("Hacer deberes", "alta")
lista_tareas.agregar_tarea("Ordenar el cuarto", "baja")
lista_tareas.agregar_tarea("Estudiar Python", "alta")
lista_tareas.agregar_tarea("Ver una película", "media")

print("Todas las tareas:", lista_tareas.tareas)
print("Tareas prioritarias:", lista_tareas.tareas_prioritarias())
lista_tareas.eliminar_completada("Hacer deberes")
print("Tareas después de eliminar:", lista_tareas.tareas)

#Entrada
# La clase recibe una descripción y una prioridad para cada tarea.
# También recibe una descripción cuando se desea eliminar una tarea.

#Proceso
# El constructor crea una lista vacía llamada tareas.
# agregar_tarea() crea una tupla con la descripción y la prioridad.
# Después agrega esa tupla a la lista usando append().
# tareas_prioritarias() recorre la lista y filtra las tareas
# cuya prioridad sea "alta".
# eliminar_completada() reconstruye la lista y conserva
# solamente las tareas cuya descripción sea diferente
# de la descripción recibida.

#Salida
# La clase permite mostrar:
# - Todas las tareas guardadas.
# - Las tareas que tienen prioridad alta.
# - La lista después de eliminar una tarea.

# Bosquejo
# Tareas iniciales:
# ("Hacer deberes", "alta")
# ("Ordenar el cuarto", "baja")
# ("Estudiar Python", "alta")
# ("Ver una película", "media")

# Tareas prioritarias:
# ("Hacer deberes", "alta")
# ("Estudiar Python", "alta")

# Si se elimina "Hacer deberes":
# ("Ordenar el cuarto", "baja")
# ("Estudiar Python", "alta")
# ("Ver una película", "media")


# Tabla pequeña:
# Descripción       | Prioridad | ¿Es prioritaria?
# Hacer deberes     | alta      | Sí
# Ordenar el cuarto | baja      | No
# Estudiar Python   | alta      | Sí
# Ver una película  | media     | No

# Resultado:
# Las tareas prioritarias son:
# ("Hacer deberes", "alta")
# ("Estudiar Python", "alta")