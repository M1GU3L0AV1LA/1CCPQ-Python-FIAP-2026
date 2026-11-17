# CitizenTech - Tempo de atendimento da Central SP156 (Prefeitura de São Paulo)
# Fonte: Dados Abertos SP156, julho/2026
# Estrutura esperada: dados/sp156.csv (a pasta figuras/ e tabelas/ são criadas)

from pathlib import Path
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from scipy import stats
from scipy.stats import norm
from sklearn.metrics import confusion_matrix, accuracy_score, roc_auc_score, roc_curve
from sklearn.model_selection import train_test_split
from statsmodels.stats.outliers_influence import variance_inflation_factor

SEED = 42                  # seed fixa: resultados reproduzíveis
MOSTRAR_GRAFICOS = True    # False = só salva os PNGs, sem abrir janelas
PASTA = Path(__file__).resolve().parent.parent
for p in ("figuras", "tabelas"):
    (PASTA / p).mkdir(exist_ok=True)
pd.set_option("display.width", None)
pd.set_option("display.max_columns", None)


def fim(nome, titulo=None, x=None, y=None):
    """Aplica título/eixos, adiciona a fonte, salva o PNG e mostra o gráfico."""
    if titulo: plt.title(titulo)
    if x: plt.xlabel(x)
    if y: plt.ylabel(y)
    plt.gcf().text(0.99, 0.005, "Fonte: Dados Abertos SP156 - Prefeitura de São Paulo (julho/2026)",
                   ha="right", fontsize=7, color="gray")
    plt.savefig(PASTA / "figuras" / f"{nome}.png", dpi=150, bbox_inches="tight")
    plt.show() if MOSTRAR_GRAFICOS else plt.close()


def equacao(modelo):
    return " ".join(f"{v:.3f}" if k == "const" else f"{v:+.3f}*{k}" for k, v in modelo.params.items())


# 1) LEITURA E PREPARAÇÃO (datas => mês/dia/ano)
bruta = pd.read_csv(PASTA / "dados" / "sp156.csv", low_memory=False)
df = bruta.copy()
df["abertura"] = pd.to_datetime(df["Data de Abertura"], format="%m/%d/%Y")
df["finalizacao"] = pd.to_datetime(df["Data de Finalização"], format="%m/%d/%Y", errors="coerce")
df["tempo_dias"] = (df["finalizacao"] - df["abertura"]).dt.days   # tempo de atendimento

print("Base bruta:", len(bruta))
df = df[df["Status"] == "Finalizada"]
print("Status = Finalizada:", len(df))
df = df.dropna(subset=["tempo_dias"])
print("Com data de finalização:", len(df), "| tempos negativos:", int((df["tempo_dias"] < 0).sum()))
t = df["tempo_dias"]

# 2) ESTATÍSTICA DESCRITIVA E NORMALIDADE
print("\n", t.describe(percentiles=[.25, .5, .75, .9, .95, .99]).round(2))
print(f"Moda: {t.mode()[0]} | Variância: {t.var():.2f} | CV: {t.std()/t.mean()*100:.1f}% "
      f"| Mesmo dia: {(t == 0).mean()*100:.1f}%")
print(f"Assimetria: {stats.skew(t):.2f} | Curtose: {stats.kurtosis(t):.2f}")
print("Shapiro-Wilk (amostra de 5000):", stats.shapiro(t.sample(5000, random_state=SEED)))

# Tabela de frequências (regra de Sturges)
k = round(1 + 3.322 * math.log10(len(t)))
fi = pd.cut(t, bins=k).value_counts().sort_index()
tabela = pd.DataFrame({"fi": fi, "fr%": (fi / fi.sum() * 100).round(2),
                       "Fac": fi.cumsum(), "Frc%": (fi.cumsum() / fi.sum() * 100).round(2)})
print(f"\nTabela de frequências (Sturges, k = {k}):\n", tabela)
tabela.to_csv(PASTA / "tabelas" / "frequencias_tempo.csv")

plt.hist(t.clip(upper=t.quantile(0.99)), bins=40, color="steelblue", edgecolor="white")
fim("hist_tempo_dias", "Distribuição do tempo de atendimento (SP156)",
    "Dias até a finalização (truncado no percentil 99)", "Nº de solicitações")
plt.boxplot(t, patch_artist=True, boxprops=dict(facecolor="skyblue"))
fim("boxplot_tempo_dias", "Boxplot - tempo de atendimento", None, "Dias")
sm.qqplot(t, line="s")
fim("qqplot_tempo", "QQ-plot do tempo de atendimento", "Quantis teóricos (Normal)", "Quantis da amostra (dias)")

# 3) ITEM 02 - PROBABILIDADE (Normal)
media, mediana, desvio = t.mean(), t.median(), t.std(ddof=0)
print(f"\nMédia = {media:.3f} | Mediana = {mediana} | Desvio padrão = {desvio:.3f}")

def classificar_evento(p):
    if np.isclose(p, 0): return "Impossível"
    if np.isclose(p, 1): return "Certo"
    if np.isclose(p, 0.5): return "Equiprovável"
    return "Improvável" if p < 0.5 else "Provável"

p_a = norm.cdf(media, media, desvio)    # a) P(X < média)
p_b = norm.sf(mediana, media, desvio)   # b) P(X > mediana)
print(f"a) P(X < média)   = {p_a:.4f} -> {classificar_evento(p_a)}")
print(f"b) P(X > mediana) = {p_b:.4f} -> {classificar_evento(p_b)}")
print(f"P(X < 0) sob a Normal = {norm.cdf(0, media, desvio):.4f} (tempo negativo é impossível)")

# 4) ITEM 03 - TESTE DE HIPÓTESE PARA A MÉDIA (teste Z, sigma conhecido)
def teste_z(n, alfa, cauda, rotulo):
    xbar = t.sample(n, random_state=SEED).mean()
    ep = desvio / np.sqrt(n)                  # erro padrão
    z = (xbar - media) / ep
    if cauda == "esquerda":                   # H1: mu < mu0
        zc, p_valor, rejeita = norm.ppf(alfa), norm.cdf(z), z < norm.ppf(alfa)
    else:                                     # H1: mu > mu0
        zc, p_valor, rejeita = norm.ppf(1 - alfa), norm.sf(z), z > norm.ppf(1 - alfa)
    print(f"\n{rotulo}) H0: mu = {media:.3f} | H1: mu {'<' if cauda == 'esquerda' else '>'} mu0 "
          f"| alfa = {alfa:.0%} | n = {n}")
    print(f"   Média amostral = {xbar:.3f} | Z = {z:.4f} | Z crítico = {zc:.4f} | p-valor = {p_valor:.4f}"
          f" -> {'REJEITA H0' if rejeita else 'NÃO REJEITA H0'}")


teste_z(20, 0.06, "esquerda", "a")
teste_z(25, 0.09, "direita", "b")

# 5) BASE POR SERVIÇO (unidade de análise dos itens 04, 05 e 06)
serv = df.groupby("Serviço").agg(
    n_solicitacoes=("tempo_dias", "size"),
    tempo_medio=("tempo_dias", "mean"),
    tempo_mediano=("tempo_dias", "median"),
    pct_fim_semana=("abertura", lambda s: (s.dt.dayofweek >= 5).mean() * 100),
    pct_com_endereco=("Latitude", lambda s: s.notna().mean() * 100),
)
canais = pd.crosstab(df["Serviço"], df["Meio de Comunicação"], normalize="index") * 100
canais.columns = ["pct_" + c.lower() for c in canais.columns]
serv = serv.join(canais)
print("\nServiços antes do filtro:", len(serv))
serv = serv[serv["n_solicitacoes"] >= 30].reset_index()   # evita medianas instáveis
print("Serviços com >= 30 solicitações:", len(serv))

serv["Órgão"] = serv["Serviço"].map(df.groupby("Serviço")["Órgão"].agg(lambda s: s.mode().iloc[0]))
org = bruta.groupby("Órgão").agg(carga_orgao=("Status", "size"),
                                 pct_nao_finalizada_orgao=("Status", lambda s: (s != "Finalizada").mean() * 100))
serv = serv.merge(org, left_on="Órgão", right_index=True, how="left")
serv["log_n"] = np.log10(serv["n_solicitacoes"])
serv.round(2).to_csv(PASTA / "dados" / "base_servicos_v2.csv", index=False)
print("Órgãos distintos:", serv["Órgão"].nunique())

# 6) ITEM 04 - ANÁLISE BIVARIADA (Y = tempo mediano | X = % não finalizada no órgão)
X_NOME, Y_NOME = "pct_nao_finalizada_orgao", "tempo_mediano"
d4 = serv[[X_NOME, Y_NOME]]
EIXO_X = "% de solicitações não finalizadas no órgão"
EIXO_Y = "Tempo mediano de atendimento (dias)"

sns.scatterplot(x=X_NOME, y=Y_NOME, data=d4)                                   # a) dispersão
fim("item04_dispersao", "Dispersão: fila do órgão x tempo mediano", EIXO_X, EIXO_Y)

print("\nCovariância:", round(np.cov(d4[X_NOME], d4[Y_NOME])[0, 1], 3))        # b)
print("Correlação de Pearson:", round(np.corrcoef(d4[X_NOME], d4[Y_NOME])[0, 1], 4))

sns.heatmap(d4.corr(), annot=True, fmt=".3f", cmap="coolwarm", vmin=-1, vmax=1)  # c)
fim("item04_correlacao", "Mapa de Correlação")

m4 = sm.OLS(d4[Y_NOME], sm.add_constant(d4[X_NOME])).fit()                    # d)
b0, b1 = m4.params
sns.regplot(x=X_NOME, y=Y_NOME, data=d4, ci=None, line_kws={"color": "red"})
fim("item04_regressao", "Gráfico de Dispersão com Reta de Regressão", EIXO_X, EIXO_Y)
print(f"\nEquação: tempo_mediano = {equacao(m4)}")

print(m4.summary())                                                            # e)
print(f"R² = {m4.rsquared:.4f} | R² ajustado = {m4.rsquared_adj:.4f} | "
      f"F = {m4.fvalue:.3f} | p-valor (F) = {m4.f_pvalue:.4g}")

nova_obs = 30                                                                  # f)
print(f"Intervalo observado de X: {d4[X_NOME].min():.1f} a {d4[X_NOME].max():.1f}")
print(f"Previsão ({nova_obs}% não finalizadas): {b0 + b1 * nova_obs:.1f} dias")

# 7) ITEM 05 - REGRESSÃO LINEAR MÚLTIPLA
XS = ["pct_nao_finalizada_orgao", "pct_portal", "log_n"]
d5 = serv[["tempo_mediano"] + XS]

sns.pairplot(d5, kind="reg", diag_kind=None)                                   # a)
plt.suptitle("Dispersão entre as variáveis", y=1.02)
fim("item05_dispersao_matriz")

print("\nMatriz de covariância:\n", d5.cov().round(2))                          # b)
print("\nMatriz de correlação de Pearson:\n", d5.corr().round(3))

sns.heatmap(d5.corr(), annot=True, fmt=".2f", cmap="coolwarm", vmin=-1, vmax=1)  # c)
fim("item05_correlacao", "Mapa de Correlação entre Variáveis")

X5 = sm.add_constant(d5[XS])                                                   # d)
m5 = sm.OLS(d5["tempo_mediano"], X5).fit()
print(f"\nEquação: tempo_mediano = {equacao(m5)}")

print(m5.summary())                                                            # e)
print(f"R² = {m5.rsquared:.4f} | R² ajustado = {m5.rsquared_adj:.4f} | p-valor (F) = {m5.f_pvalue:.4g}")

print("\nFaixas observadas:\n", d5[XS].describe().loc[["min", "50%", "max"]].round(2))   # f)
novo5 = pd.DataFrame({"const": [1.0], "pct_nao_finalizada_orgao": [30.0],
                      "pct_portal": [60.0], "log_n": [np.log10(500)]})
print("Previsão (30% pendentes, 60% portal, 500 solicitações):",
      round(float(m5.predict(novo5).iloc[0]), 2), "dias")

# 8) ITEM 06 - REGRESSÃO LOGÍSTICA (Y = 1 se tempo mediano > mediana dos serviços)
CORTE = serv["tempo_mediano"].median()
d6 = serv[XS].copy()
d6["lento"] = (serv["tempo_mediano"] > CORTE).astype(int)
ref = max(d6["lento"].mean(), 1 - d6["lento"].mean())
print(f"\nCorte = {CORTE:.1f} dias | classes:\n{d6['lento'].value_counts()}\nAcurácia de referência: {ref:.3f}")

X6 = sm.add_constant(d6[XS])
m6 = sm.Logit(d6["lento"], X6).fit(disp=False)                                 # a) modelo

fig, eixos = plt.subplots(1, 3, figsize=(15, 4.5))                             # b) sigmoides
for ax, var in zip(eixos, XS):
    grade = np.linspace(d6[var].min(), d6[var].max(), 100)
    X_c = pd.DataFrame({"const": 1.0, **{v: d6[v].mean() for v in XS}}, index=range(100))
    X_c[var] = grade                                    # só a variável em foco varia
    ax.plot(grade, m6.predict(X_c))
    ax.scatter(d6[var], d6["lento"], alpha=0.4)
    ax.set(title=f"Sigmoide - {var}", xlabel=var, ylabel="Probabilidade de serviço lento")
plt.tight_layout()
fim("item06_sigmoides")

print(m6.summary())                                                            # c) equação
print(f"\nlogit(p) = {equacao(m6)}   |   p = 1 / (1 + exp(-logit))")
odds = pd.DataFrame({"odds_ratio": np.exp(m6.params), "IC95_inf": np.exp(m6.conf_int()[0]),
                     "IC95_sup": np.exp(m6.conf_int()[1])}).round(3)
print("\nOdds ratios:\n", odds)
print(f"Pseudo-R² = {m6.prsquared:.4f} | p (razão de verossimilhança) = {m6.llr_pvalue:.4g}")

prob = m6.predict(X6)                                                          # d) classes
d6["classificacao"] = (prob > 0.5).astype(int)

cm = confusion_matrix(d6["lento"], d6["classificacao"])                        # e) confusão
vn, fp, fn, vp = cm.ravel()
print("\nMatriz de confusão (linhas = real, colunas = previsto):\n", cm)
print(f"Acurácia = {accuracy_score(d6['lento'], d6['classificacao']):.3f} | "
      f"Sensibilidade = {vp/(vp+fn):.3f} | Especificidade = {vn/(vn+fp):.3f}")
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Não lento", "Lento"],
            yticklabels=["Não lento", "Lento"])
fim("item06_matriz_confusao", "Matriz de confusão - regressão logística", "Classe prevista", "Classe real")

for pend, portal, volume in [(30, 60, 500), (2, 60, 500)]:                     # f) novos serviços
    novo = pd.DataFrame({"const": [1.0], "pct_nao_finalizada_orgao": [pend],
                         "pct_portal": [portal], "log_n": [np.log10(volume)]})
    p_novo = float(m6.predict(novo).iloc[0])
    print(f"Serviço novo ({pend}% pendentes, {portal}% portal, {volume} solic.): "
          f"P(lento) = {p_novo:.3f} -> {'lento' if p_novo > 0.5 else 'não lento'}")

# 9) EXTRAS
grupos = pd.factorize(serv["Órgão"])[0]   # serviços do mesmo órgão não são independentes
print("\nVIF:\n", pd.Series([variance_inflation_factor(X5.values, i) for i in range(1, X5.shape[1])],
                            index=XS).round(2))
print("\nRegressão múltipla (erro-padrão por órgão):\n",
      sm.OLS(d5["tempo_mediano"], X5).fit(cov_type="cluster", cov_kwds={"groups": grupos}).summary().tables[1])
print("\nLogística (erro-padrão por órgão):\n",
      sm.Logit(d6["lento"], X6).fit(disp=False, cov_type="cluster", cov_kwds={"groups": grupos}).summary().tables[1])

plt.scatter(m5.fittedvalues, m5.resid, alpha=0.6)
plt.axhline(0, color="red")
fim("item05_residuos", "Resíduos x valores ajustados", "Tempo mediano previsto (dias)", "Resíduo")

# Validação treino/teste (70/30) e curva ROC
X_tr, X_te, y_tr, y_te = train_test_split(X6, d6["lento"], test_size=0.30, random_state=SEED, stratify=d6["lento"])
p_te = sm.Logit(y_tr, X_tr).fit(disp=False).predict(X_te)
c_te = (p_te > 0.5).astype(int)
print("\nValidação (30% teste):\n", confusion_matrix(y_te, c_te))
print(f"Acurácia no teste = {accuracy_score(y_te, c_te):.3f} | AUC teste = {roc_auc_score(y_te, p_te):.3f} "
      f"| AUC modelo completo = {roc_auc_score(d6['lento'], prob):.3f}")
fpr, tpr, _ = roc_curve(y_te, p_te)
plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_te, p_te):.2f}")
plt.plot([0, 1], [0, 1], "--", color="gray", label="Acaso")
plt.legend()
fim("item06_roc", "Curva ROC (dados de teste)", "Taxa de falsos positivos", "Taxa de verdadeiros positivos")


def metricas(c):
    vn_, fp_, fn_, vp_ = confusion_matrix(d6["lento"], (prob >= c).astype(int)).ravel()
    return {"corte": c, "acuracia": (vn_ + vp_) / len(prob),
            "sensibilidade": vp_ / (vp_ + fn_), "especificidade": vn_ / (vn_ + fp_)}


tab_corte = pd.DataFrame([metricas(c) for c in (0.3, 0.4, 0.5, 0.6)]).round(3)
print("\nEfeito do corte de probabilidade:\n", tab_corte)
tab_corte.to_csv(PASTA / "tabelas" / "corte_probabilidade.csv", index=False)

# Tabelas para o assistente digital
resumo = lambda col: (df.groupby(col)["tempo_dias"].agg(
    n="size", mediana="median", media="mean", p90=lambda s: s.quantile(0.9),
    pct_mesmo_dia=lambda s: (s == 0).mean() * 100).round(1))
for nome, tab in [("por_canal", resumo("Meio de Comunicação")),
                  ("por_tema", resumo("Tema").nlargest(10, "n")),
                  ("top_servicos", resumo("Serviço").nlargest(10, "n"))]:
    print(f"\n{nome}:\n", tab)
    tab.to_csv(PASTA / "tabelas" / f"{nome}.csv")

vol = bruta["Serviço"].value_counts()
cum = vol.cumsum() / vol.sum() * 100
print("\nCobertura acumulada de solicitações (base bruta):")
for alvo in (50, 80, 90):
    print(f"  {alvo}% das solicitações: {(cum < alvo).sum() + 1} serviços (de {len(vol)})")
plt.plot(range(1, len(cum) + 1), cum.values)
plt.grid(alpha=0.3)
fim("cobertura_servicos", "Cobertura acumulada de solicitações por serviço",
    "Nº de serviços (ordenados por volume)", "% acumulado das solicitações")