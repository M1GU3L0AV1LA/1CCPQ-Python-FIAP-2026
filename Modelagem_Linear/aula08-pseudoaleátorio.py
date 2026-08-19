# Gerar números inteiros pseudoaleátorios:
import random

print(random.sample(range(1, 11), 5))

print( [random.randint(1, 100) for _ in range(6)])

# Gerar Números decimais Pseudoaleatórios:
print( [random.uniform(1, 10) for _ in range(6)])

print( [round(random.uniform(1, 10), 2) for _ in range(6)])

# Gerar números Pseudoaleatórios viciados:
import random

random.seed(1)
print( [random.randint(1, 100) for _ in range(6)])

# Gerar sorteio de palavras
import random

nomes = ["Paulo", "Gabriel", "Iara", "Isis", "Lucas", "Zé"]
print(random.sample(nomes, 3))

# Gerar sorteio de palavras viciadas:
import numpy as np

nomes = ["Paulo", "Gabriel", "Iara", "Isis", "Lucas", "Zé"]
vies = [0.10, 0.20, 0.05, 0.15, 0.10, 0.40]

print(np.random.choice(nomes, 5, replace=False, p=vies))

