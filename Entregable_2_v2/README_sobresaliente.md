# Entregable 2 — Versión Sobresaliente

Carpeta de trabajo independiente para construir el documento final y el notebook end-to-end con las evidencias adicionales requeridas para el nivel sobresaliente de la rúbrica del Módulo 2.

## Estructura

```
Entregable_2_Sobresaliente/
├── bases_limpias/
│   └── dataset_zona_15m.csv        ← único input del notebook (818KB, congelado)
├── notebooks/
│   └── 05_end_to_end_sobresaliente.ipynb   ← notebook principal
├── resultados_modelado/
│   ├── figuras/                    ← 6 figuras generadas
│   ├── tablas/                     ← 12 CSVs generados
│   ├── predicciones/
│   └── artifacts/
├── requirements.txt
└── README_sobresaliente.md
```

## Cómo ejecutar

```bash
# 1. Activar el entorno
source '../.venv_mod2/bin/activate'

# 2. Instalar dependencias (shap + statsmodels ya incluidos)
pip install -r requirements.txt

# 3. Abrir el notebook
jupyter notebook notebooks/05_end_to_end_sobresaliente.ipynb
# → Kernel → Restart & Run All
```

O en terminal sin interfaz gráfica:
```bash
../.venv_mod2/bin/jupyter nbconvert --to notebook --execute \
  --ExecutePreprocessor.timeout=600 \
  --output 05_ejecutado.ipynb \
  notebooks/05_end_to_end_sobresaliente.ipynb
```

## Qué produce el notebook (artefactos por criterio)

| Criterio rúbrica | Artefacto generado |
|---|---|
| 2.1 Trazabilidad | `tablas/req_modelo_metrica_evidencia_completo.csv` (24 reqs con estado) |
| 2.2 Alternativas | `tablas/comparison_extended.csv` (≥3 criterios + OLS + RF + HGB + baselines) |
| 2.3 Supuestos | `figuras/vif_analysis.png`, `figuras/diagnostico_residuales_ridge.png`, `tablas/ljungbox_ridge.csv`, `tablas/vif_analysis.csv` |
| 2.3 Features | `tablas/feature_justification.csv` (25 features con justificación de dominio) |
| 2.4 Sensibilidad | `figuras/sensitivity_n_estimators.png`, `tablas/sensitivity_n_estimators.csv` |
| 2.4 Train/val/test | `tablas/train_val_test_comparison.csv` (con discusión de overfitting) |
| 2.4 Métricas | `artifacts/operational_metrics_summary.json` (traducción a unidades operativas) |
| 2.5 SHAP global | `figuras/shap_summary_plot.png`, `tablas/shap_mean_importance.csv` |
| 2.5 SHAP local | `figuras/shap_waterfall_alta_demanda.png`, `figuras/shap_waterfall_baja_demanda.png` |
| 2.5 Iteraciones | `tablas/iteraciones_documentadas.csv` (5 iteraciones con fracasos documentados) |
| 2.5 Criticidad test | Análisis inline + propuesta de umbral adaptativo |
| 2.6 Plan | `tablas/plan_implementacion_completo.csv`, `tablas/escenarios_degradacion.csv` |
| 2.7 OLS coeficientes | `tablas/ols_coefficients.csv` (p-values + Durbin-Watson) |

## Qué falta incorporar al reporte escrito (`02_reporte_modelado_modulo2.md`)

1. Sección nueva: "Verificación de supuestos estadísticos" con VIF + Ljung-Box + QQ-plot
2. Ampliar Sección 4: tabla de justificación de features por dominio
3. Ampliar Sección 7: tabla comparativa con ≥3 criterios + OLS como paradigma estadístico
4. Ampliar Sección 8: narrar las 5 iteraciones documentadas (fracasos incluidos)
5. Ampliar Sección 9: SHAP summary + waterfall + conexión con dominio operativo
6. Ampliar Sección 10: criticidad en test + propuesta de umbral adaptativo
7. Ampliar Sección 11: plan con prioridades, responsables, dependencias + escenarios degradación
8. Sección nueva: "Traducción operativa de métricas" (WMAPE → pasajeros → implicación táctica)
9. Ampliar Sección 6: tabla de 24 requerimientos con estado (cubierto/parcial/pendiente)

## Datos que NO están en esta carpeta

Los archivos de datos crudos grandes permanecen en `Entregable 2/Datos/` y las bases intermedias en `Entregable 2/bases_limpias/`. Este notebook solo requiere `dataset_zona_15m.csv` (el dataset analítico final, 818KB).
