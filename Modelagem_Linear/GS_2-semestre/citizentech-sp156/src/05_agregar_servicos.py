from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PASTA_PROJETO = Path(__file__).resolve().parent.parent
df = pd.read_csv(PASTA_PROJETO / "dados" / "base_tratada.csv", parse_dates=["abertura"])

# --- Métricas por serviço ---
g = df.groupby("Serviço").agg(
    n_solicitacoes=("tempo_dias", "size"),
    tempo_medio=("tempo_dias", "mean"),
    tempo_mediano=("tempo_dias", "median"),
    pct_fim_semana=("abertura", lambda s: (s.dt.dayofweek >= 5).mean() * 100),
    pct_com_endereco=("Latitude", lambda s: s.notna().mean() * 100),
)

# --- % por canal de comunicação ---
canais = pd.crosstab(df["Serviço"], df["Meio de Comunicação"], normalize="index") * 100
canais.columns = ["pct_" + c.lower() for c in canais.columns]
g = g.join(canais)

# --- Só serviços com volume suficiente (critério a justificar no relatório) ---
MIN_SOLICITACOES = 30
print("Serviços antes do filtro:", len(g))
g = g[g["n_solicitacoes"] >= MIN_SOLICITACOES]
print(f"Serviços com >= {MIN_SOLICITACOES} solicitações:", len(g))

g = g.round(2).reset_index()
g.to_csv(PASTA_PROJETO / "dados" / "base_servicos.csv", index=False)

print("\n", g.describe().T[["count", "mean", "50%", "std", "min", "max"]])
print("\nMais lentos:\n", g.nlargest(5, "tempo_mediano")[["Serviço", "n_solicitacoes", "tempo_mediano"]])
print("\nMais rápidos:\n", g.nsmallest(5, "tempo_mediano")[["Serviço", "n_solicitacoes", "tempo_mediano"]])
print("\nCorrelação com tempo_mediano:\n",
      g.drop(columns="Serviço").corr()["tempo_mediano"].sort_values())

pasta_fig = PASTA_PROJETO / "figuras"
g["tempo_mediano"].hist(bins=30)
plt.title("Tempo mediano de atendimento por serviço")
plt.xlabel("Dias")
plt.ylabel("Nº de serviços")
plt.savefig(pasta_fig / "hist_tempo_mediano_servicos.png", dpi=150)
plt.show()