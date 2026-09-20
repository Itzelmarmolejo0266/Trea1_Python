class ColaImpresion:
    """Cola de impresión FIFO: el primer documento en entrar es el primero en salir."""

    def __init__(self):
        self.cola = []
        self.historial_impresos = []

    def agregar_documento(self, nombre):
        self.cola.append(nombre)

    def imprimir_siguiente(self):
        if not self.cola:
            return None
        documento = self.cola.pop(0)  # saca el PRIMERO, no el último
        self.historial_impresos.append(documento)
        return documento

    def documentos_pendientes(self):
        return self.cola

    def cantidad_pendiente(self):
        return len(self.cola)


ci = ColaImpresion()
ci.agregar_documento("A")
ci.agregar_documento("B")
ci.agregar_documento("C")
print(ci.imprimir_siguiente())   # "A"
print(f"Pendientes: {ci.documentos_pendientes()}")
print(f"Cantidad: {ci.cantidad_pendiente()}")