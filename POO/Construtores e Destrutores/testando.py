class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando instancia...")
        self.nome=nome
        self.cor=cor
        self.acordado=acordado

    def __del__(self):
        print("Removendo instancia!")

    def latir(self):
        print("auau")

def criar_cachorro():
    c = Cachorro("Zeus", "Preto")
    print(c.nome)

    
c = Cachorro("Luke", "cinza")
c.latir()

print("Ola mundo")

del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()