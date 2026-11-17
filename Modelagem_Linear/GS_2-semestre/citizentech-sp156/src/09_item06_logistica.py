from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.metrics import (confusion_matrix, accuracy_score, roc_auc_score,
                             roc_curve, ConfusionMatrixDisplay)

PASTA = Path(__file__).resolve().parent.parent
df = pd.read_csv(PASTA / "dados" / "base_servicos_v2.csv")
pasta_fig = PASTA / "figuras"

XS = ["pct_nao_finalizada_orgao", "pct_portal", "log_n"]
CORTE = df["tempo_mediano"].median()
df["lento"] = (df["tempo_mediano"] > CORTE).astype(int)

print(f"Corte (mediana dos serviços) = {CORTE:.1f} dias")
print("Distribuição da classe:\n", df["lento"].value_counts())
referencia = max(df["lento"].mean(), 1 - df["lento"].mean())
print(f"Acurácia de referência (classe majoritária): {referencia:.3f}")

X = sm.add_constant(df[XS])
y = df["lento"]

# (a) Equação da regressão logística
modelo = sm.Logit(y, X).fit(disp=False)
print(modelo.summary())
termos = " ".join(f"{b:+.3f}*{n}" for n, b in modelo.params.items() if n != "const")
print(f"\nlogit(p) = ln(p/(1-p)) = {modelo.params['const']:.3f} {termos}")
print("p = 1 / (1 + exp(-logit))")

odds = pd.DataFrame({"odds_ratio": np.exp(modelo.params),
                     "IC95_inf": np.exp(modelo.conf_int()[0]),
                     "IC95_sup": np.exp(modelo.conf_int()[1])}).round(3)
print("\nOdds ratios:\n", odds)
print(f"\nPseudo-R² (McFadden) = {modelo.prsquared:.4f} | "
      f"Teste da razão de verossimilhança p = {modelo.llr_pvalue:.4g}")

# (b) Matriz de confusão e acurácia – modelo completo (como pede o enunciado)
prob = modelo.predict(X)
pred = (prob >= 0.5).astype(int)
cm = confusion_matrix(y, pred)
vn, fp, fn, vp = cm.ravel()
print("\n=== Modelo completo (dados de ajuste) ===")
print(cm)
print(f"Acurácia = {accuracy_score(y, pred):.3f}")
print(f"Sensibilidade (acerta os lentos) = {vp/(vp+fn):.3f}")
print(f"Especificidade (acerta os não lentos) = {vn/(vn+fp):.3f}")
print(f"AUC = {roc_auc_score(y, prob):.3f}")

ConfusionMatrixDisplay(cm, display_labels=["Não lento", "Lento"]).plot(cmap="Blues")
plt.title("Matriz de confusão – regressão logística")
plt.savefig(pasta_fig / "item06_matriz_confusao.png", dpi=150)
plt.show()

# Validação: treino/teste (seed fixa)
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.30, random_state=42, stratify=y)
m_tr = sm.Logit(y_tr, X_tr).fit(disp=False)
p_te = m_tr.predict(X_te)
pred_te = (p_te >= 0.5).astype(int)
print("\n=== Validação (30% de teste) ===")
print(confusion_matrix(y_te, pred_te))
print(f"Acurácia no teste = {accuracy_score(y_te, pred_te):.3f} | AUC = {roc_auc_score(y_te, p_te):.3f}")

fpr, tpr, _ = roc_curve(y_te, p_te)
plt.figure(figsize=(5.5, 5))
plt.plot(fpr, tpr, label=f"AUC = {roc_auc_score(y_te, p_te):.2f}")
plt.plot([0, 1], [0, 1], "--", color="gray", label="Acaso")
plt.xlabel("Taxa de falsos positivos")
plt.ylabel("Taxa de verdadeiros positivos")
plt.title("Curva ROC (dados de teste)")
plt.legend()
plt.savefig(pasta_fig / "item06_roc.png", dpi=150)
plt.show()

# (c) Classificação de um serviço novo, com 3 variáveis explicativas
novo = pd.DataFrame({"const": [1.0],
                     "pct_nao_finalizada_orgao": [30.0],
                     "pct_portal": [60.0],
                     "log_n": [np.log10(500)]})
p_novo = float(modelo.predict(novo).iloc[0])
print(f"\nServiço novo (30% pendentes, 60% portal, 500 solicitações): "
      f"P(lento) = {p_novo:.3f} -> {'LENTO' if p_novo >= 0.5 else 'NÃO LENTO'}")