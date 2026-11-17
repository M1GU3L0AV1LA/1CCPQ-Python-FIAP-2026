from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import norm

PASTA_PROJETO = Path(__file__).resolve().parent.parent
df = pd.read_csv(PASTA_PROJETO / "dados" / "base_tratada.csv")
t = df["tempo_dias"]

# Parâmetros de referência (a base inteira é a "população")
mu0 = t.mean()
sigma = t.std(ddof=0)      # desvio padrão populacional
print(f"mu0 = {mu0:.3f} | sigma = {sigma:.3f} | N = {len(t)}")

SEED = 42  # documente no relatório; não troque a seed para "caçar" um resultado


def teste_z(n, alfa, cauda, seed):
    amostra = t.sample(n, random_state=seed)
    xbar = amostra.mean()
    erro_padrao = sigma / np.sqrt(n)
    z = (xbar - mu0) / erro_padrao

    if cauda == "esquerda":    # H1: mu < mu0
        z_crit = norm.ppf(alfa)
        p_valor = norm.cdf(z)
        rejeita = z < z_crit
    else:                      # direita, H1: mu > mu0
        z_crit = norm.ppf(1 - alfa)
        p_valor = 1 - norm.cdf(z)
        rejeita = z > z_crit

    print(f"\nn={n} | alfa={alfa:.0%} | cauda {cauda}")
    print(f"Média amostral = {xbar:.3f} | erro padrão = {erro_padrao:.3f}")
    print(f"z calculado = {z:.4f} | z crítico = {z_crit:.4f} | p-valor = {p_valor:.4f}")
    print("Decisão:", "REJEITA H0" if rejeita else "NÃO REJEITA H0")


# (a) H0: mu = mu0  vs  H1: mu < mu0 | alfa = 6% | n = 20
teste_z(n=20, alfa=0.06, cauda="esquerda", seed=SEED)

# (b) H0: mu = mu0  vs  H1: mu > mu0 | alfa = 9% | n = 25
teste_z(n=25, alfa=0.09, cauda="direita", seed=SEED)