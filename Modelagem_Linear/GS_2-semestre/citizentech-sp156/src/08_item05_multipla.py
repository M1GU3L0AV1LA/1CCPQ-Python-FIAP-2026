from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

PASTA = Path(__file__).resolve().parent.parent
df = pd.read_csv(PASTA / "dados" / "base_servicos_v2.csv")
pasta_fig = PASTA / "figuras"

Y = "tempo_mediano"
XS = ["pct_nao_finalizada_orgao", "pct_portal", "log_n"]
dados = df[[Y] + XS]
print("n =", len(dados))

# (a) Gráficos de dispersão (matriz)
sns.pairplot(dados, diag_kind="hist", plot_kws={"alpha": 0.5})
plt.savefig(pasta_fig / "item05_dispersao_matriz.png", dpi=150)
plt.show()

# (b) Matrizes de covariância e correlação
print("\nMatriz de covariância:\n", dados.cov().round(2))
print("\nMatriz de correlação de Pearson:\n", dados.corr().round(3))

# (c) Gráfico de correlação
plt.figure(figsize=(7, 5.5))
sns.heatmap(dados.corr(), annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)
plt.title("Correlação de Pearson – análise multivariada")
plt.tight_layout()
plt.savefig(pasta_fig / "item05_correlacao.png", dpi=150)
plt.show()

# (d) Regressão linear múltipla
X = sm.add_constant(dados[XS])
modelo = sm.OLS(dados[Y], X).fit()
termos = " ".join(f"{b:+.3f}*{n}" for n, b in modelo.params.items() if n != "const")
print(f"\nEquação: {Y} = {modelo.params['const']:.3f} {termos}")

# (e) Adequação: R², R² ajustado, Teste F e coeficientes
print(f"\nR² = {modelo.rsquared:.4f} | R² ajustado = {modelo.rsquared_adj:.4f}")
print(f"F = {modelo.fvalue:.3f} | p-valor (F) = {modelo.f_pvalue:.4g}")
print(modelo.summary())

# Multicolinearidade (VIF) – regra prática: VIF > 5 pede atenção
vif = pd.DataFrame({"variavel": X.columns,
                    "VIF": [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]})
print("\n", vif[vif["variavel"] != "const"].round(2))

# Sensibilidade: erros-padrão agrupados por órgão
robusto = sm.OLS(dados[Y], X).fit(
    cov_type="cluster", cov_kwds={"groups": pd.factorize(df["Órgão"])[0]})
print("\nCoeficientes com erro-padrão por cluster (órgão):")
print(robusto.summary().tables[1])

# Resíduos
plt.figure(figsize=(7, 5))
plt.scatter(modelo.fittedvalues, modelo.resid, alpha=0.6)
plt.axhline(0, color="red")
plt.title("Resíduos x valores ajustados (modelo múltiplo)")
plt.xlabel("Tempo mediano previsto (dias)")
plt.ylabel("Resíduo")
plt.savefig(pasta_fig / "item05_residuos.png", dpi=150)
plt.show()

# (f) Previsão com 3 variáveis explicativas (valores dentro da faixa observada)
print("\nFaixas observadas:\n", dados[XS].describe().loc[["min", "50%", "max"]].round(2))
novo = pd.DataFrame({"const": [1.0],
                     "pct_nao_finalizada_orgao": [30.0],
                     "pct_portal": [60.0],
                     "log_n": [np.log10(500)]})
pred = modelo.get_prediction(novo).summary_frame(alpha=0.05)
print("\nPrevisão (30% pendentes, 60% portal, 500 solicitações):")
print(pred[["mean", "obs_ci_lower", "obs_ci_upper"]].round(2))