# Tabla de Requerimientos Final

![Banner del prototipo](assets/Banner_PAAD_01.jpg)

## Alcance de evaluación

Los criterios se definen para una validación controlada del prototipo. Por tanto, no dependen de despliegue en producción, medición de ahorros reales ni adopción operativa en ambiente real.

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio o métrica de evaluación |
|---|---|---|---|---|
| Negocio | N1 | El artefacto debe identificar franjas críticas de demanda a nivel zona para apoyar la habilitación de filtros y la redistribución de recursos. | Backtesting sobre histórico, marcando como críticas las franjas de 15 minutos por percentil o umbral operativo definido. | Recall >= 0.80 en identificación de franjas críticas. |
| Negocio | N2 | El artefacto debe mejorar la anticipación frente a un baseline operativo simple. | Comparación contra baseline naive o promedio histórico por franja. | Mejora >= 10% en WMAPE o sMAPE respecto al baseline. |
| Negocio | N3 | El artefacto debe entregar una salida accionable por fecha, franja y zona. | Revisión funcional del tablero y del dataset de salida. | 100% de las franjas del horizonte definido con predicción, criticidad, capacidad de referencia y porcentaje estimado de ocupación. |
| Negocio | N4 | El artefacto debe permitir revisar históricos por filtro, aunque la alerta principal sea por zona. | Revisión funcional del tablero. | Históricos disponibles para los 13 filtros de la zona objetivo. |
| Desempeño | D1 | El modelo principal debe alcanzar desempeño aceptable en horizontes cortos de operación. | Out-of-time testing o backtesting rolling. | WMAPE <= 15% o sMAPE <= 15% en horizontes 2h y 4h. |
| Desempeño | D2 | El modelo debe mantener un error absoluto razonable en unidades del problema. | Evaluación temporal sobre validación. | MAE reportado por zona y por franja, con umbral definido a partir de la distribución histórica. |
| Desempeño | D3 | El modelo debe controlar errores grandes en franjas de alta demanda. | Evaluación temporal sobre validación. | RMSE menor al baseline y reportado por zona. |
| Desempeño | D4 | La seleccion del modelo final debe estar técnicamente justificada frente a alternativas. | Comparación entre baseline, modelo interpretable y modelo supervisado. | Tabla comparativa con métricas y justificación de modelo elegido. |
| Desempeño | D5 | El modelo debe identificar correctamente franjas críticas mas alla del error promedio. | Clasificación binaria de franjas críticas vs no críticas sobre histórico. | Recall >= 0.80 y F1 >= 0.70 para franjas críticas. |
| Funcionalidad | F1 | El prototipo debe permitir la consulta de resultados sin interacción directa con código. | Prueba funcional con usuario de referencia o revisor del proyecto. | Consulta por fecha, zona y controles propios de la vista seleccionada sin abrir notebooks ni scripts. |
| Funcionalidad | F2 | El prototipo debe mostrar claramente predicción, histórico y criticidad. | Revisión de la interfaz y de la salida visual. | Se visualizan serie estimada u observada, referencia comparable, tabla de franjas criticas y semaforo por zona. |
| Funcionalidad | F3 | El prototipo debe operar con datos anonimizados o muestras controladas en el repositorio. | Revision de repositorio y archivos de visualización. | Cero campos sensibles expuestos en repo o entregable compartido. |
| Funcionalidad | F4 | El prototipo debe permitir elegir distintos horizontes de anticipación en la vista operativa. | Prueba funcional en la vista `Ahora`. | Al menos horizontes 2h, 4h, 6h y 24h disponibles en la lógica de salida o el tablero. |
| Funcionalidad | F5 | El prototipo debe adaptar sus controles al contexto de consulta. | Prueba funcional en ambos modos del tablero. | La vista `Ahora` ofrece horizonte de consulta y la vista `Histórico` ofrece rango de comparación sin mezclar ambos controles. |
| Funcionalidad | F6 | El prototipo debe mostrar una referencia explicita de capacidad y el volúmen estimado en personas en la lectura principal. | Revisión funcional de la interfaz. | La gráfica principal incluye línea o umbral de referencia y el valor proyectado se expresa en unidades del problema. |
| Funcionalidad | F7 | El prototipo debe expresar la ocupación estimada tanto en número de pasajeros como en porcentaje sobre la capacidad disponible. | Revision funcional de la interfaz. | La vista principal presenta simultáneamente volumen estimado y porcentaje de ocupación de la zona. |
| Funcionalidad | F8 | El prototipo debe permitir definir manualmente la cantidad de filtros activos para recalcular capacidad y criticidad. | Prueba funcional en la vista `Ahora`. | El usuario puede ajustar el numero de filtros activos y la salida modifica capacidad, ocupacion y nivel de alerta. |
| Funcionalidad | F9 | El prototipo debe mostrar concentración actual por filtro y destacar el recurso con mayor carga cuando la vista sea operativa. | Revision funcional de la interfaz en la vista `Ahora`. | Se identifican los 13 filtros de la zona objetivo y al menos un recurso se marca como mayor carga en el corte consultado. |
| Usabilidad | U1 | La interfaz debe ser entendible para un usuario no técnico del área operativa. | Prueba con 2 a 3 usuarios de referencia del equipo o del entorno de validación. | Al menos 80% de tareas basicas completadas sin ayuda relevante. |
| Usabilidad | U2 | La interfaz debe comunicar el resultado sin saturar al usuario con detalle tecnico. | Revisión cualitativa del tablero y feedback de usuarios. | El usuario identifica criticidad, magnitud estimada, zona y nivel de confianza en menos de 3 minutos. |
| Usabilidad | U3 | La vista principal debe priorizar la alerta por zona y dejar el detalle por filtro como analítica complementaria. | Revisión funcional del tablero. | La vista `Ahora` resalta la criticidad de zona y permite consultar distribución actual o historicos por filtro sin perder contexto. |
| Datos | Q1 | Las fuentes integradas deben cumplir un umbral mínimo de completitud y sincronización. | Perfilamiento y reporte de calidad sobre dataset maestro. | Completitud >= 98% en campos críticos y reglas de alineación temporal documentadas. |
| Datos | Q2 | El prototipo debe construirse sobre la ventana comun validada entre las fuentes. | Revisión de ETL y reporte de calidad. | Ventana de 3 meses históricos documentada y reproducible, con validacion temporal sobre las ultimas 2 semanas y backtesting rolling. |
| Datos | Q3 | La relación temporal entre programación, ingreso al muelle y paso por filtros debe quedar modelada o documentada. | Revisión de feature engineering y reporte técnico. | Existen lags o variables que representen la anticipación entre las tres capas del proceso y la agregación desde fuentes a minuto hacia la franja operativa de 15 minutos. |
| Datos | Q4 | Los recursos inestables o casi nulos no deben sesgar la evaluación principal. | Análisis exploratorio y regla de exclusión o agrupación. | Lista explícita de recursos excluidos o agrupados con justificación técnica. |

## Deseables

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio o métrica |
|---|---|---|---|---|
| Deseable | X1 | Incluir intervalos de confianza o banda de incertidumbre. | Evaluación sobre validación. | Cobertura coherente y visualización interpretable. |
| Deseable | X2 | Incluir predicciones por filtro individual. | Evaluación tecnica y prueba funcional. | Se muestran predicciones por filtro para recursos con estabilidad suficiente. |
| Deseable | X3 | Incorporar tiempos de proceso como señal de anomalía operativa. | Análisis exploratorio y prueba funcional. | El tablero resalta desviaciones inusuales de tiempo de proceso cuando aplique. |

## Base de formulación

Los requerimientos se apoyan en evidencia previa:

- patrones horarios ya observados,
- limpieza y homologación documentadas,
- ventana comun construida,
- levantamiento funcional documentado en anexo,
- necesidad diferenciada de seguimiento intradía y comparación retrospectiva,
- existencia de tres capas del proceso: programación, ingreso al muelle y paso por filtros.

## Validación funcional prevista

La validación con usuarios de referencia se plantea sobre dos perfiles: coordinación operativa y análisis de control operativo. Las tareas base de prueba son:

1. identificar la siguiente franja crítica y determinar si se requiere habilitar capacidad adicional;
2. interpretar la ocupación esperada de la zona con base en pasajeros proyectados, capacidad disponible y porcentaje de ocupación;
3. revisar una fecha anterior y concluir si el comportamiento observado fue atipico frente al histórico comparable.

## Fuera de alcance

- validación en producción,
- medición de ahorros reales,
- adopción real en operacion,
- integración corporativa completa,
- piloto real con usuarios finales,
- optimización completa de dotaciones.
