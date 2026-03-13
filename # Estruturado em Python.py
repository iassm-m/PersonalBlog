# Estruturado em Python
def calcular_media(notas):
    return sum(notas) / len(notas)

def situacao(media):
    return "Aprovado" if media >= 5 else "Reprovado"

def main():
    n = int(input("Quantidade de alunos: "))
    alunos = []

    for i in range(n):
        nome = input("Nome do aluno: ")
        notas = list(map(float, input("Digite as notas separadas por espaço: ").split()))
        media = calcular_media(notas)
        alunos.append((nome, media, situacao(media)))

    # Ordenar por média
    alunos.sort(key=lambda x: x[1], reverse=True)

    # Estatísticas
    medias = [a[1] for a in alunos]
    print("\n--- Resultados ---")
    for nome, media, sit in alunos:
        print(f"{nome}: Média {media:.2f} - {sit}")

    print(f"Média da turma: {sum(medias)/len(medias):.2f}")
    print(f"Maior média: {max(medias):.2f}")
    print(f"Menor média: {min(medias):.2f}")

if __name__ == "__main__":
    main()
