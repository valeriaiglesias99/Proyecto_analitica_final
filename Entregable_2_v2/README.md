# Entregable 2 — Módulo 2: Selección y Parametrización de Modelos

**Proyecto Aplicado en Analítica de Datos — Universidad de los Andes**  
Grupo 23: Danilo Suárez Vargas · Valeria Iglesias Miranda · Sergio Andrés Perdomo Murcia

---

## Descripción

Entrega del módulo de modelado para el pronóstico de flujo de pasajeros en los filtros de seguridad de la zona internacional del aeropuerto. Se construyó un modelo Random Forest que integra tres fuentes de datos operativas (sensores de filtros, VeriPax y programación de vuelos) para pronosticar el flujo en franjas de 15 minutos con un WMAPE de 17.9% en validación.

---

## Estructura de la carpeta

```
Entregable_2_v2/
├── Reporte_de_seleccion_y_parametrizacion_de_modelos.md   ← documento principal de la entrega
├── environment.yml                         ← entorno conda reproducible
├── requirements.txt                        ← alternativa pip
├── datos_originales/
│   └── programacionvuelos.csv             ← datos crudos de vuelos programados
├── bases_limpias/
│   ├── dataset_zona_15m.csv               ← dataset analítico final (input del notebook)
│   ├── sensores_filtro_15m.csv            ← flujo de sensores agregado a 15 min
│   └── vuelos_internacionales_programados.csv
├── notebooks/
│   └── Notebook_Modelado_Modulo2_PAAD2026.ipynb
├── resultados_modelado/
│   ├── artifacts/
│   │   ├── best_model_sobresaliente.joblib ← modelo final serializado
│   │   └── operational_metrics_summary.json
│   ├── figuras/                            ← 9 figuras generadas
│   └── tablas/                             ← 11 CSVs de métricas e iteraciones
└── assets/
```

> **Datos no incluidos por tamaño (>100 MB):** `dataveripax.csv` (303 MB) y `datasensores.csv` (203 MB) están disponibles en la carpeta `Entregable 2/Datos/` del repositorio local. El notebook solo requiere `dataset_zona_15m.csv` para ejecutarse.

---

## Cómo reproducir los resultados

### Opción 1 — Conda (recomendado)

```bash
conda env create -f environment.yml
conda activate paad_mod2
jupyter lab notebooks/Notebook_Modelado_Modulo2_PAAD2026.ipynb
```

### Opción 2 — pip + venv

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter lab notebooks/Notebook_Modelado_Modulo2_PAAD2026.ipynb
```

Una vez abierto el notebook: **Kernel → Restart & Run All**

El notebook regenera todas las figuras, tablas, métricas y el modelo `.joblib` desde cero. Tiempo estimado de ejecución: ~10 minutos.

---

## Modelos evaluados

| Modelo | WMAPE val | WMAPE test | Paradigma |
|---|---|---|---|
| **RF rf_iter_2** | **0.179** | **0.184** | ML no lineal |
| HGB | 0.181 | 0.180 | ML no lineal |
| Ridge | 0.184 | 0.194 | ML lineal |
| OLS statsmodels | 0.185 | 0.195 | Estadístico clásico |
| Persistencia | 0.194 | 0.178 | Heurístico |
| Prophet | 0.222 | 0.216 | Series de tiempo |
| ARIMA(2,0,1) | 0.463 | 0.418 | Series de tiempo |

---

## Artefactos por criterio de rúbrica

| Criterio | Artefacto |
|---|---|
| Trazabilidad (2.1) | `tablas/req_modelo_metrica_evidencia_completo.csv` |
| Comparación modelos (2.2) | `tablas/comparison_extended.csv` |
| Supuestos estadísticos (2.3) | `figuras/vif_analysis.png`, `figuras/diagnostico_residuales_ridge.png`, `tablas/ljungbox_ridge.csv` |
| Sensibilidad hiperparámetros (2.4) | `figuras/sensitivity_n_estimators.png`, `tablas/sensitivity_n_estimators.csv` |
| Interpretabilidad SHAP (2.5) | `figuras/shap_summary_plot.png`, `figuras/shap_waterfall_*.png` |
| Iteraciones documentadas (2.5) | `tablas/iteraciones_documentadas.csv` |
| Plan de implementación (2.6) | `tablas/plan_implementacion_completo.csv`, `tablas/escenarios_degradacion.csv` |
| Métricas operativas (2.7) | `artifacts/operational_metrics_summary.json` |
