from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats
from scipy.stats import norm

PASTA_PROJETO = Path(__file__).resolve().parent.parent
print("Pasta do projeto:", PASTA_PROJETO)
print("CSV existe?", (PASTA_PROJETO / "dados" / "sp156.csv").exists())

df = pd.read_csv(PASTA_PROJETO / "dados" / "sp156.csv",
                 sep=",", encoding="utf-8", low_memory=False)

df["abertura"] = pd.to_datetime(df["Data de Abertura"], format="%m/%d/%Y")
df["finalizacao"] = pd.to_datetime(df["Data de Finalização"], format="%m/%d/%Y", errors="coerce")
df["tempo_dias"] = (df["finalizacao"] - df["abertura"]).dt.days

# --- Filtros (anote cada contagem para o relatório) ---
print("Linhas iniciais:", len(df))
df = df[df["Status"] == "Finalizada"]
print("Após Status = Finalizada:", len(df))
df = df.dropna(subset=["tempo_dias"])
print("Após exigir data de finalização:", len(df))

# --- Salvar a base tratada ---
colunas = ["abertura", "finalizacao", "tempo_dias", "Meio de Comunicação", "Tema",
           "Assunto", "Serviço", "Órgão", "Distrito", "Latitude", "Longitude"]
df[colunas].to_csv(PASTA_PROJETO / "dados" / "base_tratada.csv", index=False)

# --- Estatísticas descritivas ---
t = df["tempo_dias"]
print("\n", t.describe())
print("Assimetria:", round(stats.skew(t), 2), "| Curtose:", round(stats.kurtosis(t), 2))
print("% resolvidas no mesmo dia:", round((t == 0).mean() * 100, 1))

# --- Teste de normalidade (Shapiro em amostra de 5000, com seed fixa) ---
amostra = t.sample(5000, random_state=42)
print("\nShapiro-Wilk:", stats.shapiro(amostra))

pasta_fig = PASTA_PROJETO / "figuras"
pasta_fig.mkdir(exist_ok=True)
sm.qqplot(t, line="s")
plt.title("QQ-plot do tempo de atendimento")
plt.savefig(pasta_fig / "qqplot_tempo.png", dpi=150)
plt.show()

# --- Item 02 ---
media = t.mean()
mediana = t.median()
desvio = t.std(ddof=0)
p_a = norm.cdf(media, loc=media, scale=desvio)
p_b = 1 - norm.cdf(mediana, loc=media, scale=desvio)
print(f"\nMédia={media:.3f} | Mediana={mediana:.1f} | Desvio={desvio:.3f}")
print(f"(a) P(X < média)   = {p_a:.4f}")
print(f"(b) P(X > mediana) = {p_b:.4f}")

