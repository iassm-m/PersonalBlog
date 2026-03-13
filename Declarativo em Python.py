from functools import reduce

alunos = {
    "Ana": [7, 8, 6, 8, 10],
    "Carlos": [5, 4, 6, 9, 3],
    "Beatriz": [5, 4, 2, 7, 5],
    "Gustavo": [6, 7, 5, 6, 8]
}

# Calculando as médias com map
medias = list(map(lambda x: (x[0], sum(x[1])/len(x[1])), alunos.items()))

# Situação com map
resultados = list(map(lambda x: (x[0], x[1], "Aprovado" if x[1] >= 6 else "Reprovado"), medias))

# Estatísticas com reduce
media_turma = reduce(lambda acc, x: acc + x[1], resultados, 0) / len(resultados)
maior = max(resultados, key=lambda x: x[1])
menor = min(resultados, key=lambda x: x[1])

print("\n--- Resultados ---")
for nome, media, sit in resultados:
    print(f"{nome}: Média {media:.2f} - {sit}")

print(f"Média da turma: {media_turma:.2f}")
print(f"Maior média: {maior}")
print(f"Menor média: {menor}")
