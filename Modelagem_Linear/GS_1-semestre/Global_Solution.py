import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Carregar o dataset
df = pd.read_csv('database.csv')

# Extrair o ANO da coluna Launch Date
df['Ano'] = df['Launch Date'].str.extract(r'(\d{4})').astype(int)

# Remover nulos da massa (8 registros sem valor)
df_massa = df['Payload Mass (kg)'].dropna()

print(f"Total de registros: {len(df)}")
print(f"Registros com massa válida: {len(df_massa)}")

# TABELA A: Lançamentos por Ano (Variável Discreta)
# 1. Frequência absoluta — contar lançamentos por ano
fi = df['Ano'].value_counts().sort_index()

# 2. Frequência relativa (%)
fr = (fi / fi.sum() * 100).round(2)

# 3. Frequência acumulada absoluta
fac = fi.cumsum()

# 4. Frequência relativa acumulada (%)
frc = fr.cumsum().round(2)

# 5. Montar a tabela
tabela_discreta = pd.DataFrame({
    'Ano'                        : fi.index,
    'fi (Freq. Absoluta)'        : fi.values,
    'fr% (Freq. Relativa)'       : fr.values,
    'Fac (Freq. Acum. Abs.)'     : fac.values,
    'Frc% (Freq. Acum. Rel.)'    : frc.values,
})

# 6. Linha de TOTAL
total = pd.DataFrame([{
    'Ano'                        : 'TOTAL',
    'fi (Freq. Absoluta)'        : fi.sum(),
    'fr% (Freq. Relativa)'       : 100.00,
    'Fac (Freq. Acum. Abs.)'     : '-',
    'Frc% (Freq. Acum. Rel.)'    : '-',
}])

tabela_discreta = pd.concat([tabela_discreta, total], ignore_index=True)

print("\n📋 TABELA A — Lançamentos por Ano (Variável Discreta)")
print(tabela_discreta.to_string(index=False))

# TABELA B: Massa da Carga (Variável Contínua)

n = len(df_massa)

# Regra de Sturges para definir número de classes
k = int(round(1 + 3.322 * math.log10(n)))  # → 6 classes

# Criar os intervalos com pd.cut
intervalos = pd.cut(df_massa, bins=k)

# Frequência absoluta por intervalo
fi_cont = intervalos.value_counts().sort_index()

# Frequência relativa (%)
fr_cont = (fi_cont / fi_cont.sum() * 100).round(2)

# Frequências acumuladas
fac_cont = fi_cont.cumsum()
frc_cont = fr_cont.cumsum().round(2)

# Montar a tabela
tabela_continua = pd.DataFrame({
    'Classe (kg)'                : [str(i) for i in fi_cont.index],
    'fi (Freq. Absoluta)'        : fi_cont.values,
    'fr% (Freq. Relativa)'       : fr_cont.values,
    'Fac (Freq. Acum. Abs.)'     : fac_cont.values,
    'Frc% (Freq. Acum. Rel.)'    : frc_cont.values,
})

# Linha de TOTAL
total_cont = pd.DataFrame([{
    'Classe (kg)'                : 'TOTAL',
    'fi (Freq. Absoluta)'        : fi_cont.sum(),
    'fr% (Freq. Relativa)'       : 100.00,
    'Fac (Freq. Acum. Abs.)'     : '-',
    'Frc% (Freq. Acum. Rel.)'    : '-',
}])

tabela_continua = pd.concat([tabela_continua, total_cont], ignore_index=True)

print("\n📋 TABELA B — Massa da Carga em kg (Variável Contínua)")
print(tabela_continua.to_string(index=False))

#=========================================================
#GRÁFICO 1: Resultado das Missões (Gráfico de Barras)
# 1. Contar quantas missões tiveram cada resultado
resultados = df['Mission Outcome'].value_counts()

# 2. Definir cor para cada barra
#    Se o resultado for "Success" → verde, senão → vermelho
cores = ['#00e676' if r == 'Success' else '#ff1744'
         for r in resultados.index]

# 3. Criar a figura e o eixo
fig1, ax1 = plt.subplots(figsize=(8, 5))

# 4. Desenhar as barras
barras = ax1.bar(
    resultados.index,   # rótulos no eixo X
    resultados.values,  # alturas das barras
    color=cores,        # cores definidas acima
    edgecolor='#333',   # borda de cada barra
    width=0.5,          # largura das barras
)

# 5. Rótulo em cima de cada barra (valor)
for barra, valor in zip(barras, resultados.values):
    pct = valor / resultados.sum() * 100
    ax1.text(
        barra.get_x() + barra.get_width() / 2,  # posição X: centro da barra
        barra.get_height() + 0.3,                # posição Y: topo + espaço
        f'{valor} ({pct:.1f}%)',                  # texto exibido
        ha='center', fontsize=11, fontweight='bold'
    )

# 6. Elementos obrigatórios do gráfico
ax1.set_title('Resultado das Missões SpaceX — Sucesso vs Falha (2006–2017)',
              fontsize=13, fontweight='bold', pad=15)
ax1.set_xlabel('Resultado da Missão', fontsize=11)
ax1.set_ylabel('Número de Missões',   fontsize=11)
ax1.set_ylim(0, resultados.max() * 1.3)   # espaço acima das barras
ax1.grid(axis='y', linestyle='--', alpha=0.5)

# 7. Legenda manual com patches coloridos
legenda = [
    mpatches.Patch(color='#00e676', label=f"Sucesso — {resultados.get('Success', 0)} missões"),
    mpatches.Patch(color='#ff1744', label=f"Falha   — {resultados.get('Failure', 0)} missões"),
]
ax1.legend(handles=legenda, fontsize=10)

# 8. Fonte dos dados (rodapé)
fig1.text(0.99, 0.01, 'Fonte: SpaceX Missions Dataset — Kaggle (2006–2017)',
          ha='right', fontsize=8, color='gray')

# 9. Salvar e mostrar
plt.tight_layout()
plt.savefig('grafico1_resultado_missoes.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico 1 salvo!")

# GRÁFICO 2: Lançamentos por Ano
# 1. Preparar os dados por ano e resultado
anos_ord = sorted(df['Ano'].unique())

suc_ano = (df[df['Mission Outcome'] == 'Success']
           .groupby('Ano').size()
           .reindex(anos_ord, fill_value=0))

fal_ano = (df[df['Mission Outcome'] == 'Failure']
           .groupby('Ano').size()
           .reindex(anos_ord, fill_value=0))

total_ano = suc_ano + fal_ano

# 2. Criar figura
fig2, ax2 = plt.subplots(figsize=(12, 6))

# 3. Barras empilhadas — sucessos na base, falhas em cima
ax2.bar(anos_ord, suc_ano.values, color='#00e676',
        label='Sucesso', edgecolor='#333', linewidth=0.8)

ax2.bar(anos_ord, fal_ano.values,
        bottom=suc_ano.values,        # começa do topo da barra verde
        color='#ff1744',
        label='Falha', edgecolor='#333', linewidth=0.8)

# 4. Rótulo de total acima de cada barra
for ano, total_val in zip(anos_ord, total_ano.values):
    ax2.text(ano, total_val + 0.1, str(total_val),
             ha='center', fontsize=9, fontweight='bold')

# 5. Elementos obrigatórios
ax2.set_title('Lançamentos SpaceX por Ano — Evolução 2006–2017',
              fontsize=13, fontweight='bold', pad=15)
ax2.set_xlabel('Ano de Lançamento', fontsize=11)
ax2.set_ylabel('Número de Missões', fontsize=11)
ax2.set_xticks(anos_ord)
ax2.set_xticklabels(anos_ord, rotation=45, ha='right')
ax2.set_ylim(0, total_ano.max() * 1.6)
ax2.grid(axis='y', linestyle='--', alpha=0.4)

# 6. Legenda combinada dos dois eixos
ax2.legend(fontsize=9, loc='upper left')

# 7. Fonte
fig2.text(0.99, 0.01, 'Fonte: SpaceX Missions Dataset — Kaggle (2006–2017)',
          ha='right', fontsize=8, color='gray')

# 8. Salvar e mostrar
plt.tight_layout()
plt.savefig('grafico2_lancamentos_por_ano.png', dpi=150, bbox_inches='tight')
plt.show()
print("Gráfico 2 salvo!")

# ==================================================================
# ANÁLISE 1: Payload Mass — Massa da Carga Útil (kg)
massa = df['Payload Mass (kg)'].dropna()

print("═══ ANÁLISE 1 — Massa da Carga Útil (kg) ═══")

# Medidas de Tendência Central:
print("Média:",    massa.mean())
print("Mediana:",  massa.median())
print("Moda:",     massa.mode())

# Medidas de Dispersão:
print("Mínimo:",              massa.min())
print("Máximo:",              massa.max())
print("Amplitude:",           massa.max() - massa.min())
print("Variância:",           massa.var())
print("Desvio Padrão:",       massa.std())
print("Coef. de Variação:",   massa.std() / massa.mean() * 100)

# Medidas Separatrizes:
print("Quartis:", massa.quantile([0.25, 0.50, 0.75]))

# Análise Gráfica: Boxplot
plt.boxplot(massa,
            patch_artist=True,
            boxprops=dict(facecolor='skyblue'))
plt.title('Boxplot — Massa da Carga Útil (kg)')
plt.ylabel('Massa (kg)')
plt.savefig('boxplot_massa.png', dpi=150, bbox_inches='tight')
plt.show()

# ANÁLISE 2: Lançamentos por Ano

lancamentos = df.groupby('Ano').size().astype(float)

print("═══ ANÁLISE 2 — Lançamentos por Ano ═══")

# Medidas de Tendência Central:
print("Média:",    lancamentos.mean())
print("Mediana:",  lancamentos.median())
print("Moda:",     lancamentos.mode())

# Medidas de Dispersão:
print("Mínimo:",              lancamentos.min())
print("Máximo:",              lancamentos.max())
print("Amplitude:",           lancamentos.max() - lancamentos.min())
print("Variância:",           lancamentos.var())
print("Desvio Padrão:",       lancamentos.std())
print("Coef. de Variação:",   lancamentos.std() / lancamentos.mean() * 100)

# Medidas Separatrizes:
print("Quartis:", lancamentos.quantile([0.25, 0.50, 0.75]))

# Análise Gráfica: Boxplot
plt.boxplot(lancamentos,
            patch_artist=True,
            boxprops=dict(facecolor='salmon'))
plt.title('Boxplot — Lançamentos por Ano')
plt.ylabel('Nº de Lançamentos')
plt.savefig('boxplot_lancamentos.png', dpi=150, bbox_inches='tight')
plt.show()































































































































































































































































































