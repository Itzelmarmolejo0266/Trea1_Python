class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mejor_equipo = None
        mayor_cantidad = -1
        for nombre, jugadores in self.equipos.items():
            if len(jugadores) > mayor_cantidad:
                mayor_cantidad = len(jugadores)
                mejor_equipo = nombre
        return mejor_equipo
gestor = Equipos()

gestor.crear_equipo("Barcelona")
gestor.crear_equipo("Emelec")
gestor.crear_equipo("Liga")
gestor.agregar_jugador("Barcelona", "Juan")
gestor.agregar_jugador("Barcelona", "Pedro")
gestor.agregar_jugador("Emelec", "Luis")
gestor.agregar_jugador("Emelec", "Ana")
gestor.agregar_jugador("Emelec", "Mateo")
gestor.agregar_jugador("Liga", "María")
gestor.agregar_jugador("Liga", "Sofía")
gestor.agregar_jugador("Liga", "Diego")
gestor.agregar_jugador("Liga", "Pablo")

print("Equipos:", gestor.equipos)
print("Equipo con más integrantes:",
      gestor.equipo_mayor_integrantes())
# 1
# La clase Equipos permite crear equipos deportivos,
# agregar jugadores y saber qué equipo tiene más integrantes.

#Entrada
#Nombre del equipo.
#Nombre del jugador.

#Proceso
#Se crea cada equipo.
#Se agregan los jugadores a su equipo correspondiente.
#Se cuentan los jugadores de cada equipo.
#Se compara la cantidad de integrantes.

#Salida
#Se muestran los equipos con sus jugadores.
#Se muestra el equipo que tiene más integrantes.

#BOSQUEJO 

# Barcelona tiene 2 jugadores:
# Juan y Pedro.

# Emelec tiene 3 jugadores:
# Luis, Ana y Mateo.

# Liga tiene 4 jugadores:
# María, Sofía, Diego y Pablo.
# El equipo con más jugadores es Liga, porque tiene 4 integrantes.

#TABLA
# Equipo       Cantidad de jugadores
# Barcelona    2
# Emelec       3
# Liga         4

# Resultado esperado:
# Equipo con más integrantes: Liga