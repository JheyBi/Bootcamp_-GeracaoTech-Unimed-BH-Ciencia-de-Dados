class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome=nome
        self.matricula=matricula

    def __str__(self):
        return f"Nome: {self.nome}\nMatricula: {self.matricula}\nEscola: {self.escola}\n"

aluno_1 = Estudante("João", 1)
aluno_2 = Estudante("Sophia", 2)
print(aluno_1, aluno_2)
aluno_1.matricula=3
Estudante.escola = "UENP"
print(aluno_1, aluno_2)