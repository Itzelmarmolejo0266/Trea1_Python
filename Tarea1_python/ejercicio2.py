class AnalizadorTexto:
    def __init__(self):
        self.palabras_unicas=set()
        self.orden_palabras=[]
    
    def agregar_palabra(self,palabra):             # Entrada:
                                                   # Recibe palabras individuales mediante agregar_palabra()
                                                   # o varias palabras mediante agregar_multiples(*args).
      if palabra not in self.palabras_unicas:
            self.palabras_unicas.add(palabra)
            self.orden_palabras.append(palabra)
                                                   # Proceso:
                                                   # Guarda las palabras en un conjunto para evitar duplicados
                                                   # y en una lista para mantener el orden de llegada.
                                                   # Después cuenta cuántas palabras únicas existen.
                                                                                              
    def contar_palabras(self):
        return len(self.palabras_unicas) 
    
    def agregar_multiples(self, *args):
        for palabra in args:
             self.agregar_palabra(palabra)
             
at = AnalizadorTexto()
at.agregar_multiples("hola", "mundo", "hola")

print(at.palabras_unicas)
print(at.orden_palabras)
print(at.contar_palabras())  # Salida:
                             # Devuelve la cantidad de palabras únicas mediante
                             # el método contar_palabras().
                             
# TABLA PEQUEÑA
#
# Palabra    ¿Es nueva?    ¿Se guarda?
# hola       Sí            Sí
# mundo      Sí            Sí
# hola       No            No
#
# Lista final:
# ["hola", "mundo"]
#
# Conjunto final:
# {"hola", "mundo"}
#
# Cantidad de palabras únicas:
# 2