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

carrito.agregar_articulo("Cuaderno", 3.50)
carrito.agregar_articulo("Esfero", 1.25)
carrito.agregar_articulo("Mochila", 25.00)
carrito.agregar_articulo("Colores", 4.50)

print("Artículos:", carrito.articulos)
print("Total del carrito:", carrito.total_carrito())
print("Artículos entre $3 y $10:",
      carrito.articulos_por_rango(3, 10))
