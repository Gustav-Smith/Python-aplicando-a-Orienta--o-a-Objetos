class Carro:
    carros = []
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)
    
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

    def listar_carro():
        for carro in Carro.carros:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')
            
carro_fusca = Carro('Fusca', 'Azul', 1970)

Carro.listar_carro()
