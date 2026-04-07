"""
Mercado Laboral Tech en LATAM - Analisis Exploratorio
======================================================
Fuente: Datos sinteticos basados en Stack Overflow Developer Survey 2023
y encuestas de sueldos de comunidades tech de LATAM (OpenQube, Encuesta IT).

Autor: Federico Ramos
Repo  : https://github.com/federicoramos67/mercado-laboral-tech-latam
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
from pathlib import Path

# ── Configuracion global ─────────────────────────────────────────────────────
sns.set_theme(style="darkgrid", palette="muted")
plt.rcParams.update({"figure.dpi": 130, "font.size": 11})
OUTPUT_DIR = Path("graficos")
OUTPUT_DIR.mkdir(exist_ok=True)

NP_SEED = 42
rng = np.random.default_rng(NP_SEED)

# ── Generacion de datos sinteticos ────────────────────────────────────────────
PAISES     = ["Argentina", "Uruguay", "Brasil", "Colombia", "Chile", "Mexico"]
ROLES      = ["Data Analyst", "Data Engineer", "Data Scientist",
               "Backend Dev", "Frontend Dev", "DevOps", "Full Stack"]
EXP_NIVELES = ["Junior", "Semi-Senior", "Senior"]
TECNOLOGIAS = ["Python", "SQL", "JavaScript", "Java", "TypeScript",
                "R", "Scala", "Go", "Rust", "Kotlin"]

# Sueldo base mensual en USD por pais (mediana aproximada 2023-2024)
SUELDO_BASE = {
    "Argentina": 1_200, "Uruguay": 2_800, "Brasil": 2_200,
    "Colombia": 1_600,  "Chile":   2_500,  "Mexico": 1_900,
}
# Multiplicador por nivel de experiencia
MULT_EXP = {"Junior": 0.55, "Semi-Senior": 1.0, "Senior": 1.75}
# Multiplicador por rol
MULT_ROL = {
    "Data Scientist": 1.30, "Data Engineer": 1.20, "DevOps": 1.25,
    "Data Analyst":   1.05, "Backend Dev":   1.10,
    "Full Stack":      1.08, "Frontend Dev":  0.95,
}

n = 1_200
paises_col  = rng.choice(PAISES,      n, p=[.22,.08,.28,.15,.14,.13])
roles_col   = rng.choice(ROLES,       n, p=[.18,.12,.14,.20,.15,.10,.11])
exp_col     = rng.choice(EXP_NIVELES, n, p=[.35,.40,.25])

sueldos = np.array([
    SUELDO_BASE[p] * MULT_EXP[e] * MULT_ROL[r] * rng.uniform(0.80, 1.20)
    for p, r, e in zip(paises_col, roles_col, exp_col)
]).round(0)

# Tecnologias (cada dev conoce entre 2 y 5)
tecnologias_col = ["||".join(rng.choice(TECNOLOGIAS, rng.integers(2, 6), replace=False))
                   for _ in range(n)]

anios_exp_num = {"Junior": 1, "Semi-Senior": 3, "Senior": 7}
anios_exp_col = np.array([
    anios_exp_num[e] + rng.integers(0, 3) for e in exp_col
])

remoto_col = rng.choice(["Remoto", "Hibrido", "Presencial"], n,
                         p=[0.55, 0.32, 0.13])

df = pd.DataFrame({
    "pais":        paises_col,
    "rol":         roles_col,
    "experiencia": exp_col,
    "anios_exp":   anios_exp_col,
    "sueldo_usd":  sueldos,
    "tecnologias": tecnologias_col,
    "modalidad":   remoto_col,
})

print(f"Dataset generado: {df.shape[0]} registros, {df.shape[1]} columnas")
print(df.describe()[["sueldo_usd", "anios_exp"]].round(1))

# ── Figura 1: Distribucion de sueldos por pais ────────────────────────────────
fig, ax = plt.subplots(figsize=(11, 5))
orden_paises = (df.groupby("pais")["sueldo_usd"]
                  .median().sort_values(ascending=False).index)
sns.boxplot(data=df, x="pais", y="sueldo_usd", order=orden_paises,
            palette="Blues_r", ax=ax)
ax.set_title("Distribucion de Sueldos Tech por Pais (USD/mes)", fontsize=14, fontweight="bold")
ax.set_xlabel("Pais")
ax.set_ylabel("Sueldo mensual (USD)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "01_sueldos_por_pais.png")
plt.close()
print("[OK] Figura 1 guardada")

# ── Figura 2: Sueldo promedio por rol y nivel de experiencia ──────────────────
pivot = (df.groupby(["rol", "experiencia"])["sueldo_usd"]
           .mean().unstack()
           .reindex(columns=["Junior", "Semi-Senior", "Senior"]))

fig, ax = plt.subplots(figsize=(12, 5))
pivot.plot(kind="bar", ax=ax, colormap="viridis", edgecolor="white", width=0.75)
ax.set_title("Sueldo Promedio por Rol y Nivel de Experiencia", fontsize=14, fontweight="bold")
ax.set_xlabel("Rol")
ax.set_ylabel("Sueldo promedio (USD)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.tick_params(axis="x", rotation=30)
ax.legend(title="Experiencia")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "02_sueldo_rol_experiencia.png")
plt.close()
print("[OK] Figura 2 guardada")

# ── Figura 3: Top 10 tecnologias mas demandadas ────────────────────────────────
tech_series = (df["tecnologias"].str.split("||")
                                .explode()
                                .value_counts()
                                .head(10))

fig, ax = plt.subplots(figsize=(9, 5))
colors = sns.color_palette("rocket", len(tech_series))
bars = ax.barh(tech_series.index[::-1], tech_series.values[::-1], color=colors[::-1])
for bar, val in zip(bars, tech_series.values[::-1]):
    ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height() / 2,
            str(val), va="center", fontsize=10)
ax.set_title("Top 10 Tecnologias Mas Demandadas en LATAM", fontsize=14, fontweight="bold")
ax.set_xlabel("Cantidad de profesionales que la usan")
ax.set_xlim(0, tech_series.values.max() * 1.15)
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "03_tecnologias_demandadas.png")
plt.close()
print("[OK] Figura 3 guardada")

# ── Figura 4: Modalidad de trabajo por pais ────────────────────────────────────
modalidad_pct = (df.groupby(["pais", "modalidad"])
                   .size().unstack(fill_value=0)
                   .div(df.groupby("pais").size(), axis=0) * 100)
modalidad_pct = modalidad_pct.loc[orden_paises]

fig, ax = plt.subplots(figsize=(10, 5))
modalidad_pct.plot(kind="bar", stacked=True, ax=ax,
                   color=["#2ecc71", "#f39c12", "#e74c3c"],
                   edgecolor="white", width=0.7)
ax.set_title("Modalidad de Trabajo por Pais (%)", fontsize=14, fontweight="bold")
ax.set_xlabel("Pais")
ax.set_ylabel("Porcentaje (%)")
ax.tick_params(axis="x", rotation=25)
ax.legend(title="Modalidad", loc="upper right")
ax.yaxis.set_major_formatter(mticker.PercentFormatter())
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "04_modalidad_por_pais.png")
plt.close()
print("[OK] Figura 4 guardada")

# ── Figura 5: Correlacion sueldo vs anios de experiencia ──────────────────────
fig, ax = plt.subplots(figsize=(8, 5))
for pais, color in zip(["Uruguay", "Argentina", "Brasil"],
                        ["#1abc9c", "#3498db", "#e67e22"]):
    sub = df[df["pais"] == pais]
    medias = sub.groupby("anios_exp")["sueldo_usd"].median()
    ax.plot(medias.index, medias.values, marker="o", label=pais, color=color, linewidth=2)
ax.set_title("Crecimiento Salarial segun Experiencia (paises seleccionados)",
             fontsize=13, fontweight="bold")
ax.set_xlabel("Anios de experiencia")
ax.set_ylabel("Sueldo mediano (USD)")
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"${x:,.0f}"))
ax.legend()
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "05_crecimiento_salarial.png")
plt.close()
print("[OK] Figura 5 guardada")

# ── Resumen estadistico final ─────────────────────────────────────────────────
print("\n===== RESUMEN EJECUTIVO =====")
print(f"Pais con mayor sueldo mediano : {df.groupby('pais')['sueldo_usd'].median().idxmax()}")
print(f"Rol mejor pagado (promedio)   : {df.groupby('rol')['sueldo_usd'].mean().idxmax()}")
print(f"Tecnologia mas usada          : {df['tecnologias'].str.split('||').explode().value_counts().idxmax()}")
print(f"Modalidad predominante        : {df['modalidad'].value_counts().idxmax()}")
print(f"Brecha Junior vs Senior (x)   : {(df[df.experiencia=='Senior']['sueldo_usd'].mean() / df[df.experiencia=='Junior']['sueldo_usd'].mean()):.1f}x")
print(f"\nGraficos exportados en: ./{OUTPUT_DIR}/")
print("Analisis completado exitosamente.")
