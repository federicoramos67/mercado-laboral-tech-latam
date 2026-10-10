# 💼 Mercado Laboral Tech en LATAM

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0-150458?logo=pandas&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-0.12-4C9BE8?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7-11557C?logo=plotly&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completado-brightgreen)
![License](https://img.shields.io/badge/License-MIT-yellow)

> Proyecto demostrativo de análisis del mercado laboral tecnológico en seis países de América Latina, mediante un dataset sintético reproducible.

> **Importante:** el script genera 1.200 registros sintéticos con supuestos definidos en el código. Las cifras y gráficos sirven para demostrar un flujo analítico; no son estimaciones representativas ni conclusiones basadas en microdatos reales de encuestas.

---

## 🎯 Objetivo

Demostrar cómo estructurar y comunicar un análisis de preguntas de negocio, por ejemplo:

- ¿En qué país se paga más a los profesionales tech?
- ¿Qué tecnologías dominan el mercado laboral?
- ¿Cuánto crece el sueldo con la experiencia?
- ¿Qué roles tienen mayor diferencial salarial entre Junior y Senior?
- ¿Cómo está distribuida la modalidad remoto/híbrido/presencial?

---

## 📈 Visualizaciones Generadas

| # | Título | Tipo |
|---|---|---|
| 1 | Distribución de sueldos tech por país (USD/mes) | Boxplot |
| 2 | Sueldo promedio por rol y nivel de experiencia | Bar chart agrupado |
| 3 | Top 10 tecnologías más demandadas en LATAM | Bar chart horizontal |
| 4 | Modalidad de trabajo por país (%) | Bar chart apilado |
| 5 | Crecimiento salarial según años de experiencia | Line chart |

Todas las visualizaciones se exportan automáticamente a la carpeta `graficos/`.

---

## 📊 Resultados ilustrativos del escenario simulado

El script resume, a partir de la simulación y sus parámetros, el país con mayor sueldo mediano, el rol con mayor sueldo promedio, la tecnología más frecuente, la modalidad predominante y la brecha salarial Junior/Senior. Estos resultados cambian si se modifican los supuestos o la semilla aleatoria; **no deben citarse como estadísticas observadas del mercado laboral**.

---

## 📂 Estructura del Proyecto

```
mercado-laboral-tech-latam/
├── analisis.py       # Script principal: generación de datos + 5 visualizaciones
├── graficos/         # Carpeta de salida con los PNG generados
├── requirements.txt  # Dependencias del proyecto
└── README.md
```

---

## 🚀 Cómo Ejecutar

```bash
# 1. Clonar el repositorio
git clone https://github.com/federicoramos67/mercado-laboral-tech-latam.git
cd mercado-laboral-tech-latam

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Ejecutar el análisis
python analisis.py
```

Al finalizar, encontrarás los 5 gráficos en la carpeta `graficos/` y un resumen ejecutivo en la consola.

---

## 🛠️ Tecnologías Utilizadas

| Herramienta | Uso |
|---|---|
| **Python 3.10+** | Lenguaje principal |
| **Pandas** | Generación y manipulación del dataset |
| **NumPy** | Cálculos numéricos y datos sintéticos |
| **Matplotlib** | Motor de visualización base |
| **Seaborn** | Visualizaciones estadísticas |

---

## 📊 Sobre los Datos

Este proyecto utiliza **datos sintéticos** generados con `numpy.random`, calibrados en base a:
- Stack Overflow Developer Survey 2023
- Encuesta de Sueldos IT Argentina (OpenQube)
- Informes salariales de la industria tech LATAM 2023–2024

Los parámetros se inspiraron en referencias públicas, pero los registros se generan artificialmente y no son una reproducción ni una validación de esas fuentes. Para convertir el proyecto en un estudio empírico, habría que sustituir el generador por microdatos con licencia y metodología documentadas, limpiar y validar la muestra, y reportar limitaciones y fecha de extracción.

---

## 👤 Autor

**Federico Ramos** — Analista de Datos Jr. | Uruguay

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/federico-ramos-904024281)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/federicoramos67)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:federicoramos6767@gmail.com)

---

> 💡 **Contexto personal**: Como profesional tech uruguayo buscando mi primera oportunidad en datos, este análisis surgió de una pregunta real: *¿en qué país y con qué skills tengo más oportunidades?* Los datos hablan por sí solos.
