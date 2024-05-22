# platform: beecrowd - https://judge.beecrowd.com/pt/problems/view/3412
# programming language: Python
# status: Accepted

# author: Gabriel Soares
# https://www.linkedin.com/in/gabrielsoarespebr/
# https://github.com/gabrielsoarespebr

qtdAluno = int(input())

alunoNomeLista = []
alunoNotaLista = []

for _ in range(qtdAluno):
    alunoNome = input()

    alunoNomeLista.append(alunoNome)

    alunoAvaliacaoLista = list(map(float, input().split()))

    alunoNota = 0

    if (len(alunoAvaliacaoLista) == 1):
        alunoNota = round(alunoAvaliacaoLista[0]/2, 1)

    if (len(alunoAvaliacaoLista) == 2):
        alunoNota = round(sum(alunoAvaliacaoLista)/2, 1)

    if (len(alunoAvaliacaoLista) == 3):
        alunoNota = round(sum(alunoAvaliacaoLista)/3, 1)

    if (len(alunoAvaliacaoLista) == 4):
        avaliacaoTrioInicialLista = alunoAvaliacaoLista[:3]

        avaliacaoUltima = alunoAvaliacaoLista[3]

        avaliacaoMenor = min(avaliacaoTrioInicialLista)

        if (avaliacaoUltima > avaliacaoMenor):
            indexSubstituir = avaliacaoTrioInicialLista.index(avaliacaoMenor)

            avaliacaoTrioInicialLista[indexSubstituir] = avaliacaoUltima

        alunoNota = round(sum(avaliacaoTrioInicialLista)/3, 1)

    alunoNotaLista.append(alunoNota)

for i in range(qtdAluno):
    print(alunoNomeLista[i]+":",alunoNotaLista[i])
