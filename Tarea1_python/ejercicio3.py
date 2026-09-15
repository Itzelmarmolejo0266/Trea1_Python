class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)

        return resultado


carrito = CarroCompras()

carrito.agregar_articulo("Laptop", 500)
carrito.agregar_articulo("Mouse", 20)
carrito.agregar_articulo("Teclado", 35)
carrito.agregar_articulo("Audifonos", 80)

print("Articulos:", carrito.articulos)
print("Total del carrito:", carrito.total_carrito())
print("Articulos entre $20 y $100:",
      carrito.articulos_por_rango(20, 100))


# Entrada:
# Recibe el nombre y el precio de cada artículo.
# También recibe un precio mínimo y un precio máximo
# para buscar artículos por rango.

# Proceso:
# Guarda los artículos y sus precios en un diccionario.
# Calcula el total sumando los precios.
# Recorre los artículos y selecciona los que estén
# dentro del rango indicado.

# Salida:
# Muestra los artículos guardados, el total del carrito
# y una lista con los artículos que cumplen el rango.


#  BOSQUEJO

# Artículos:
# Laptop = 500
# Mouse = 20
# Teclado = 35
# Audifonos = 80

# Total:
# 500 + 20 + 35 + 80 = 635
#
# Rango:
# Precio mínimo = 20
# Precio máximo = 100

# Artículos que cumplen:
# Mouse = 20
# Teclado = 35
# Audifonos = 80

# Resultado:
# ["Mouse", "Teclado", "Audifonos"]


#TABLA PEQUEÑA
#
# Artículo    Precio    ¿Entre 20 y 100?
# Laptop      500       No
# Mouse       20        Sí
# Teclado     35        Sí
# Audifonos   80        Sí
#
# Total:
# 500 + 20 + 35 + 80 = 635
#
# Lista final:
# ["Mouse", "Teclado", "Audifonos"]