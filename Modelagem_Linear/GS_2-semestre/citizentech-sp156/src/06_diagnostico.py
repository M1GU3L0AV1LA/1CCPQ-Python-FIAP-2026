from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

PASTA = Path(__file__).resolve().parent.parent
serv = pd.read_csv(PASTA / "dados" / "base_servicos.csv")
trat = pd.read_csv(PASTA / "dados" / "base_tratada.csv")
bruta = pd.read_csv(PASTA / "dados" / "sp156.csv", low_memory=False)

# Órgão principal de cada serviço
orgao_serv = trat.groupby("Serviço")["Órgão"].agg(lambda s: s.mode().iloc[0])
serv["Órgão"] = serv["Serviço"].map(orgao_serv)

# Variáveis por órgão, calculadas na base bruta (todos os status)
org = bruta.groupby("Órgão").agg(
    carga_orgao=("Status", "size"),
    pct_nao_finalizada_orgao=("Status", lambda s: (s != "Finalizada").mean() * 100),
)
serv = serv.merge(org, left_on="Órgão", right_index=True, how="left")

# Transformações para reduzir a assimetria
serv["log_n"] = np.log10(serv["n_solicitacoes"])
serv["log_carga"] = np.log10(serv["carga_orgao"])
serv["tempo_log"] = np.log1p(serv["tempo_mediano"])

print("Serviços sem órgão associado:", serv["Órgão"].isna().sum())
print("Órgãos distintos:", serv["Órgão"].nunique())

candidatas = ["n_solicitacoes", "log_n", "carga_orgao", "log_carga",
              "pct_nao_finalizada_orgao", "pct_portal", "pct_crm",
              "pct_com_endereco", "pct_fim_semana"]

res = pd.DataFrame({
    "pearson_tempo_mediano": serv[candidatas].corrwith(serv["tempo_mediano"]),
    "pearson_tempo_log": serv[candidatas].corrwith(serv["tempo_log"]),
    "spearman_tempo_mediano": serv[candidatas].corrwith(serv["tempo_mediano"], method="spearman"),
}).round(3)
print("\n", res.sort_values("spearman_tempo_mediano"))

# Mapa de calor
pasta_fig = PASTA / "figuras"
cols = candidatas + ["tempo_mediano"]
plt.figure(figsize=(9, 7))
sns.heatmap(serv[cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Correlação de Pearson – variáveis por serviço")
plt.tight_layout()
plt.savefig(pasta_fig / "heatmap_candidatas.png", dpi=150)
plt.show()

serv.to_csv(PASTA / "dados" / "base_servicos_v2.csv", index=False)