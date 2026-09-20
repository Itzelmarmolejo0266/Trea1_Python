class CalculadoraPropina:
    def __init__(self):
        self.historial=[]
    def calcular_propina(self, cuenta, porcentaje):
        return cuenta * (porcentaje / 100)
    def registrar_cuenta(self, cuenta, porcentaje):
        propina = self.calcular_propina(cuenta, porcentaje)
        total = cuenta + propina
        self.historial.append((cuenta, porcentaje, propina, total))
        return total
    
    def dividir_entre_personas(self,total,personas):
        return total / personas
    
    def total_recaudado(self):
        return sum(total for _, _, _, total in self.historial)
    
cp=CalculadoraPropina()
total1=cp.registrar_cuenta(100,15)
print(f"Total con propina: {total1}")
print(f"Dividido entre 4 personas: {cp.dividir_entre_personas(total1, 4)}") 
print(f"Total recaudado: {cp.total_recaudado()}")