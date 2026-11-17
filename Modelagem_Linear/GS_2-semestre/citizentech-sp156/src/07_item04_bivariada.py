from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy.stats import pearsonr

PASTA = Path(__file__).resolve().parent.parent
df = pd.read_csv(PASTA / "dados" / "base_servicos_v2.csv")
pasta_fig = PASTA / "figuras"

X_NOME = "pct_nao_finalizada_orgao"
Y_NOME = "tempo_mediano"
x, y = df[X_NOME], df[Y_NOME]
print("n =", len(df))

# (a) Gráfico de dispersão
plt.figure(figsize=(7, 5))
plt.scatter(x, y, alpha=0.6)
plt.title("Fila do órgão x tempo mediano de atendimento")
plt.xlabel("% de solicitações não finalizadas no órgão")
plt.ylabel("Tempo mediano de atendimento (dias)")
plt.savefig(pasta_fig / "item04_dispersao.png", dpi=150)
plt.show()

# (b) Covariância e correlação de Pearson
cov = np.cov(x, y, ddof=1)[0, 1]
r, p_r = pearsonr(x, y)
print(f"\nCovariância = {cov:.3f}")
print(f"Pearson r = {r:.4f} | p-valor = {p_r:.4g}")

# (c) Gráfico de correlação de Pearson (matriz 2x2)
plt.figure(figsize=(4.5, 3.5))
sns.heatmap(df[[X_NOME, Y_NOME]].corr(), annot=True, fmt=".3f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlação de Pearson")
plt.tight_layout()
plt.savefig(pasta_fig / "item04_correlacao.png", dpi=150)
plt.show()

# (d) Regressão linear simples + reta no gráfico
modelo = sm.OLS(y, sm.add_constant(x)).fit()
b0, b1 = modelo.params
print(f"\nEquação: tempo_mediano = {b0:.3f} + {b1:.3f} * {X_NOME}")

plt.figure(figsize=(7, 5))
plt.scatter(x, y, alpha=0.6, label="Serviços")
xs = np.linspace(x.min(), x.max(), 100)
plt.plot(xs, b0 + b1 * xs, color="red", label="Reta de regressão")
plt.title("Regressão linear simples")
plt.xlabel("% de solicitações não finalizadas no órgão")
plt.ylabel("Tempo mediano de atendimento (dias)")
plt.legend()
plt.savefig(pasta_fig / "item04_regressao.png", dpi=150)
plt.show()

# (e) Adequação do modelo: R², Teste F
print(f"\nR² = {modelo.rsquared:.4f} | R² ajustado = {modelo.rsquared_adj:.4f}")
print(f"Estatística F = {modelo.fvalue:.3f} | p-valor (F) = {modelo.f_pvalue:.4g}")
print(modelo.summary())

# Sensibilidade: erros-padrão robustos por órgão (observações não independentes)
robusto = sm.OLS(y, sm.add_constant(x)).fit(
    cov_type="cluster", cov_kwds={"groups": pd.factorize(df["Órgão"])[0]})
print("\nCoeficiente de X com erro-padrão por cluster (órgão):")
print(robusto.summary().tables[1])

# (f) Previsão
novo = 30  # % não finalizadas: troque por um valor realista da base
previsto = b0 + b1 * novo
print(f"\nPrevisão: órgão com {novo}% não finalizadas -> {previsto:.1f} dias (mediano)")
print("Intervalo observado de X:", round(x.min(), 1), "a", round(x.max(), 1))


# Resíduos x valores ajustados (checa variância constante e outliers)
plt.figure(figsize=(7, 5))
plt.scatter(modelo.fittedvalues, modelo.resid, alpha=0.6)
plt.axhline(0, color="red")
plt.title("Resíduos x valores ajustados")
plt.xlabel("Tempo mediano previsto (dias)")
plt.ylabel("Resíduo")
plt.savefig(pasta_fig / "item04_residuos.png", dpi=150)
plt.show()

# Sensibilidade: Y em escala logarítmica
m_log = sm.OLS(df["tempo_log"], sm.add_constant(x)).fit()
print(f"\n[log] R² = {m_log.rsquared:.4f} | F = {m_log.fvalue:.2f} | "
      f"coef = {m_log.params.iloc[1]:.4f}")

# Intervalo de confiança (média) e de previsão (um serviço individual), 95%
pred = modelo.get_prediction(np.array([[1.0, novo]])).summary_frame(alpha=0.05)
print("\n", pred[["mean", "mean_ci_lower", "mean_ci_upper", "obs_ci_lower", "obs_ci_upper"]])