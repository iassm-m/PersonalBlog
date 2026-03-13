class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Aluno(Pessoa):
    def __init__(self, nome, notas):
        super().__init__(nome)
        self.notas = notas
        self.media = self.calcular_media()


    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        return "Aprovado" if self.media >= 6 else "Reprovado"

try:
    alunos = [
        Aluno("Ana", [7, 8, 6, 9, 7]),
        Aluno("Carlos", [5, 4, 6, 4 ,8]),
        Aluno("Beatriz", [9, 8, 10, 9, 10])
    ]

    alunos.sort(key=lambda a: a.media, reverse=True)

    for aluno in alunos:
        print(f"{aluno.nome}: Média {aluno.media:.2f} - {aluno.situacao()}")

except Exception as e:
    print("Erro ao processar alunos:", e)
