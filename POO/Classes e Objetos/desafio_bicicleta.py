class Bicicleta:
    def __init__(self,cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinhar(self):
        print("Plim Plim")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicleta parada!")

    def correr(self):
        print("Vrummmm...")

    # def __str__(self):
    #     return f"Bicicleta: Cor: {self.cor}, Modelo: {self.modelo}, Ano: {self.ano}, Valor: {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"



    
b1 = Bicicleta("Vermelha", "Caloi", 2022, 60)
b1.buzinhar()
b1.parar()
b1.correr()
print(b1.cor, b1.modelo, b1.ano, b1.valor)
print(b1.__str__())