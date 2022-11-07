class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome=nome
        self.idade=idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022- ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_de_idade(idade):
        return idade>=18

# p = Pessoa("João", 19)
# print(p.nome, p.idade)

p2 = Pessoa.criar_de_data_nascimento(2003,3,20,"João")
print(p2.nome, p2.idade)
print(Pessoa.e_maior_de_idade(17))
print(Pessoa.e_maior_de_idade(18))