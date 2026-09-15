class Calificador:
    def __init__(self):               # Entrada:
                                      # Recibe varias notas mediante el método cargar_notas(*args).
        self.notas = []

    def validar_nota(self, nota):     # Proceso:
                                      # Valida cada nota y guarda únicamente las que están
                                      # entre 0 y 100. Después calcula el promedio.
        return 0 <= nota <= 100

    def cargar_notas(self, *args):
        for nota in args:      
            if self.validar_nota(nota):
                self.notas.append(nota)

        return self.notas

    def promedio(self):
        if len(self.notas) == 0:                # Salida:
                                                # Devuelve True o False al validar una nota, una lista
                                                # con las notas válidas y el promedio de esas notas.
            return 0

        return sum(self.notas) / len(self.notas)

c = Calificador()
print(c.cargar_notas(85, 92, 110, 78, 88,-5))     #BOSQUEJO

                                               # Notas:
                                               # 85, 92, 110, 78, -5, 88

                                               # Notas válidas:
                                               # 85, 92, 78, 88

                                               # Suma:
                                               # 85 + 92 + 78 + 88 = 343

                                               # Cantidad de notas:
                                               # 4

                                               # Promedio:
                                               # 343 / 4 = 85.75
print(c.promedio())