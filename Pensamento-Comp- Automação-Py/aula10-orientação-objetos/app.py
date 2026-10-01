from aluno import Aluno
from disciplina import Disciplina

# Criar / instanciar 1 aluno
aluno1 = Aluno("Miguel", "54321", "Ciência da computação")

# Criar 2 disciplinas
cs = Disciplina("Computer Science", "Lucas")
model_mat = Disciplina("Modelagem Matemática", "Christian")

# Matricular o aluno nas disciplinas
aluno1.matricular(cs)
aluno1.matricular(model_mat)
print(aluno1.disciplinas[0].professor)

# Adicionar notas do aluno referente a determinada disciplina
aluno1.adicionar_nota(cs, 10)
aluno1.adicionar_nota(cs, 8)
aluno1.adicionar_nota(model_mat, 5)
aluno1.adicionar_nota(model_mat, 4)

print(aluno1.notas_por_disciplina)
print(aluno1.calcular_media_d(model_mat))
print(aluno1.calcular_media_geral())