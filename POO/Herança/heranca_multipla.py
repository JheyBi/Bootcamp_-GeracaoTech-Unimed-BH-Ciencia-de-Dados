class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {' , '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        super().__init__(**kw)
        self.cor_pelo=cor_pelo

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        super().__init__(**kw)
        self.cor_bico=cor_bico

class Gato(Mamifero):
    pass


class Ornitorrinco(Mamifero, Ave):
    pass


gato = Gato(numero_patas=4, cor_pelo="cinza")
print(gato)

ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo="vermelho", cor_bico="marrom")
print(ornitorrinco)