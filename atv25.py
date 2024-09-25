# Enunciado: Crie um programa que receba a nota de 5 alunos e exiba quantos foram aprovados (nota maior ou igual a 7).
def contar_aprovados():
    aprovados = 0
    
    for i in range(5):
        try:
            nota = float(input(f"Digite a nota do aluno {i + 1}: "))
            if nota >= 7:
                aprovados += 1
        except ValueError:
            print("Por favor, digite uma nota válida.")
            # Pode-se considerar a nota como 0 ou ignorar a entrada, dependendo do critério
            continue

    print(f"Total de alunos aprovados: {aprovados}")

contar_aprovados()
