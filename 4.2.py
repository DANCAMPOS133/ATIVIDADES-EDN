# Calculando a media da turma

print("=== DESCUBRA A MÉDIA DA TURMA ===")

quantidade_alunos = int(input("Digite a quantidade de alunos: "))

notas = []

for i in range(quantidade_alunos):
    nota = float(input(f"Digite a nota do aluno {i + 1}: "))
    notas.append(nota)

media = sum(notas) / quantidade_alunos

print("\nNotas registradas:", notas)
print(f"Média da turma: {media:.2f}")
