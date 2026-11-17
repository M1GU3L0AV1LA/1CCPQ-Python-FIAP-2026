from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import confusion_matrix

PASTA = Path(__file__).resolve().parent.parent
serv = pd.read_csv(PASTA / "dados" / "base_servicos_v2.csv")
trat = pd.read_csv(PASTA / "dados" / "base_tratada.csv")
bruta = pd.read_csv(PASTA / "dados" / "sp156.csv", low_memory=False)
pasta_fig = PASTA / "figuras"
pasta_tab = PASTA / "tabelas"
pasta_tab.mkdir(exist_ok=True)

# ---------- A) Logística com erro-padrão agrupado por órgão ----------
XS = ["pct_nao_finalizada_orgao", "pct_portal", "log_n"]
serv["lento"] = (serv["tempo_mediano"] > serv["tempo_mediano"].median()).astype(int)
X = sm.add_constant(serv[XS])
y = serv["lento"]
grupos = pd.factorize(serv["Órgão"])[0]

modelo = sm.Logit(y, X).fit(disp=False)
robusto = sm.Logit(y, X).fit(disp=False, cov_type="cluster", cov_kwds={"groups": grupos})
print("=== Logística com erro-padrão por órgão ===")
print(robusto.summary().tables[1])

# ---------- B) Corte de probabilidade x sensibilidade ----------
prob = modelo.predict(X)
linhas = []
for corte in [0.3, 0.4, 0.5, 0.6]:
    pred = (prob >= corte).astype(int)
    vn, fp, fn, vp = confusion_matrix(y, pred).ravel()
    linhas.append({"corte": corte,
                   "acuracia": (vn + vp) / len(y),
                   "sensibilidade": vp / (vp + fn),
                   "especificidade": vn / (vn + fp)})
tab_corte = pd.DataFrame(linhas).round(3)
print("\n=== Efeito do corte de probabilidade ===\n", tab_corte)
tab_corte.to_csv(pasta_tab / "corte_probabilidade.csv", index=False)

# ---------- C) Segundo exemplo de classificação ----------
novo = pd.DataFrame({"const": [1.0], "pct_nao_finalizada_orgao": [2.0],
                     "pct_portal": [60.0], "log_n": [np.log10(500)]})
print("\nExemplo 2 (2% pendentes, 60% portal, 500 solic.): P(lento) =",
      round(float(modelo.predict(novo).iloc[0]), 3))

# ---------- D) Insights para o assistente digital ----------
def resumo(grupo):
    return grupo["tempo_dias"].agg(
        n="size", mediana="median", media="mean",
        p90=lambda s: s.quantile(0.9),
        pct_mesmo_dia=lambda s: (s == 0).mean() * 100).round(1)

por_tema = trat.groupby("Tema").apply(resumo, include_groups=False)
por_tema = por_tema.sort_values("n", ascending=False).head(10)
por_canal = trat.groupby("Meio de Comunicação").apply(resumo, include_groups=False)
top_serv = (trat.groupby("Serviço").apply(resumo, include_groups=False)
            .sort_values("n", ascending=False).head(10))

print("\n=== Por tema (top 10 em volume) ===\n", por_tema)
print("\n=== Por canal ===\n", por_canal)
print("\n=== Top 10 serviços em volume ===\n", top_serv)
por_tema.to_csv(pasta_tab / "por_tema.csv")
por_canal.to_csv(pasta_tab / "por_canal.csv")
top_serv.to_csv(pasta_tab / "top_servicos.csv")

# Cobertura: quantos serviços cobrem a maior parte dos pedidos (base bruta, todos os status)
vol = bruta["Serviço"].value_counts()
cum = vol.cumsum() / vol.sum() * 100
print("\n=== Cobertura acumulada de solicitações ===")
for k in [5, 10, 20, 50]:
    print(f"Top {k} serviços: {cum.iloc[k-1]:.1f}%")
for alvo in [50, 80, 90]:
    print(f"{alvo}% das solicitações: {(cum < alvo).sum() + 1} serviços (de {len(vol)})")

plt.figure(figsize=(7, 5))
plt.plot(range(1, len(cum) + 1), cum.values)
plt.title("Cobertura acumulada de solicitações por serviço")
plt.xlabel("Nº de serviços (ordenados por volume)")
plt.ylabel("% acumulado das solicitações")
plt.grid(alpha=0.3)
plt.savefig(pasta_fig / "cobertura_servicos.png", dpi=150)
plt.show()
