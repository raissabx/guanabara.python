class CalculoBonus:
    
    def __init__(self, salario, fator):
        self.salario = salario
        self.fator = fator
        
    def calcular_bonus(self):
        return self.salario * self.fator
    
desenvolvedor = CalculoBonus(1, -1)
print(desenvolvedor.calcular_bonus())

diretor = CalculoBonus(1, 2)
print(diretor.calcular_bonus())