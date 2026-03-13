def calcular_media(notas):
    
    if len(notas) == 0:
        return 0
    soma = 0
    for x in notas:
        soma += x
    return soma / len(notas)


def situacao(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"


def ler_alunos(qtd):
    lista = []
    for i in range(qtd):
        print(f"\nAluno {i+1}")
        nome = input("Nome: ")

        # lendo notas
        raw = input("Notas separadas por espaço: ").strip()
        pedacos = raw.split(" ")
        notas = []

        for ped in pedacos:
            if ped == "":
                continue
            try:
                notas.append(float(ped))
            except:
                notas.append(0)  

        lista.append([nome, notas])
    return lista


def estatisticas(alunos):
    medias = []
    for a in alunos:
        m = calcular_media(a[1])
        medias.append(m)

    if len(medias) == 0:
        return 0, 0, 0

    media_geral = sum(medias) / len(medias)
    maior = max(medias)
    menor = min(medias)

    return media_geral, maior, menor


#principal 
try:
    n = int(input("Quantidade de alunos: "))
except:
    print("Número inválido. Usando 0.")
    n = 0

alunos = ler_alunos(n)

print("\n--- Resultados Parciais ---")
for aluno in alunos:
    nome = aluno[0]
    notas = aluno[1]
    media = calcular_media(notas)
    print(f"{nome} -> Média: {media:.2f} ({situacao(media)})")

m_geral, maior_m, menor_m = estatisticas(alunos)


print("\n--- Estatísticas ---")
print("Média da turma:", round(m_geral, 2))
print("Maior média:", maior_m)
print("Menor média:", menor_m)

