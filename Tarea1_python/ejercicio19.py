class Inventario:
    def __init__(self):
        self.stock = {}
    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = self.stock.get(producto, 0) + cantidad
    def restar_stock(self, producto, cantidad):
        disponible = self.stock.get(producto, 0)
        if disponible >= cantidad:
            self.stock[producto] -= cantidad
            return True
        return False
    def productos_bajo_stock(self, minimo):
        return [
            producto
            for producto, cantidad in self.stock.items()
            if cantidad < minimo
        ]

inventario = Inventario()
inventario.agregar_stock("Arroz", 20)
inventario.agregar_stock("Leche", 8)
inventario.agregar_stock("Pan", 15)
inventario.agregar_stock("Arroz", 5)
print("¿Se pudo vender leche?", inventario.restar_stock("Leche", 3))
print("¿Se pudo vender pan?", inventario.restar_stock("Pan", 20))
print("Productos con bajo stock:",
      inventario.productos_bajo_stock(10))
print("Inventario:", inventario.stock)
#ENTRADA
#nombre del producto
#cantidad de productos
#cantidad que queremos retirar
#cantidad mínima para detectar bajo stock
# Ejemplo:
# "Arroz", 20
# "Leche", 8
# "Pan", 15

#PROCESO
# 1. agregar_stock() agrega productos al diccionario.
# 2. Si el producto ya existe, suma la nueva cantidad.
# 3. restar_stock() verifica si hay suficiente stock.
# 4. Si hay suficiente, resta la cantidad y retorna True.
# 5. Si no hay suficiente, retorna False.
# 6. productos_bajo_stock() busca productos cuya
#cantidad sea menor al mínimo indicado.

#SALIDA
#Se obtiene:
#True o False al restar stock.
#Una lista con productos de bajo stock.
#El diccionario completo del inventario.

# BOSQUEJO:
# Arroz = 20 + 5 = 25
# Leche = 8 - 3 = 5
# Pan = 15
# Venta de leche:
# 8 >= 3 → True
# Venta de pan:
# 15 >= 20 → False
# Bajo stock con mínimo 10:
# Leche = 5 → sí está bajo

# VERIFICACIÓN:
# Operación              Resultado
# Agregar 20 arroz       Arroz = 20
# Agregar 5 arroz        Arroz = 25
# Vender 3 leche         True
# Vender 20 pan          False
# Bajo stock < 10        ['Leche']