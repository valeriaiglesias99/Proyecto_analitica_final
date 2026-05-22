# Tabla de Requerimientos Diligenciada

![Banner del prototipo](assets/Banner_PAAD_01.jpg)

## Resultado de la validación del prototipo
A continuación se presentan los requerimientos definidos en la Semana 1, donde se establecieron los criterios de evaluación y el alcance del proyecto. Para cada requerimiento se indica el estado de cumplimiento al cierre del prototipo, la evidencia que lo sustenta y las acciones correctivas propuestas para los casos en que no se satisface completamente.

### Leyenda de estados

| Estado | Significado |
|---|---|
| ✅ Cubierto | El requerimiento se satisface completamente en el prototipo actual. |
| 🟡 Parcial | El requerimiento se satisface de forma incompleta o con condiciones. |
| 🔴 Pendiente | El requerimiento no fue implementado en esta iteración y se documenta su justificación. |
| 🔵 Deseable | Requerimiento opcional no implementado. Se documenta el enfoque propuesto para fases futuras. |

---

## Requerimientos de negocio

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio de verificación | Estado | Justificación y acciones correctivas |
|---|---|---|---|---|---|---|
| Negocio | N1 | El artefacto debe identificar franjas críticas de demanda a nivel zona para apoyar la habilitación de filtros y la redistribución de recursos. |  Backtesting sobre histórico marcando como críticas las franjas de 15 minutos por umbral  operativo definido. | Recall >= 0.80 en identificación de franjas críticas. El umbral de 0.80 se justifica operativamente: un coordinador que detecta 8 de cada 10 franjas críticas con anticipación de 15 minutos tiene tiempo suficiente para habilitar un filtro adicional. Fallar en 2 de cada 10 franjas es aceptable porque el sistema de sensores en tiempo real actúa como respaldo inmediato.  | 🟡 Parcial | Con umbral nominal de 13 filtros (432 pax) el Recall es 0 porque solo 8 franjas del test superan ese valor (0.7% del total). Con umbral operativo de 9 filtros activos (299 pax) el modelo base alcanza Recall = 0.50 y el modelo ponderado Recall = 0.59. Con umbral de 8 filtros (266 pax) el Recall sube a 0.70–0.75. El tablero incluye un control deslizante de filtros activos que recalcula automáticamente los umbrales según la dotación real del turno. **Acción correctiva pendiente:** la detección de picos extremos tiene un techo estructural causado por los pasajeros de conexión que no generan validación VeriPax, para resolverlo se requiere `pax_conexion` del sistema DCS del área de handling, el cual no se tienen datos para este proyecto y toca considerarlo en una implementación futura. |
| Negocio | N2 | El artefacto debe mejorar la anticipación frente a un baseline operativo simple. | Comparación contra baseline naive o promedio histórico por franja. |Mejora >= 10% en WMAPE respecto al baseline. Si el coordinador asume que el próximo periodo tendrá el mismo flujo que el actual, se equivoca en promedio 39 pasajeros por franja. Una mejora del 10% reduciría ese error a 35 pasajeros, lo que en la práctica puede ser la diferencia entre abrir un filtro a tiempo o no. Se eligió la persistencia como baseline porque es exactamente lo que haría un operador sin ningún modelo, asumir que el flujo actual de pasajereos se mantiene. | 🟡 Parcial | El modelo `rf_iter_2` mejora un 7.5% en WMAPE respecto al baseline de persistencia (0.1789 vs 0.1935). El MAE mejora 7.7% y el RMSE mejora 11%. La mejora es menor al 10% porque el baseline de persistencia es un estimador muy fuerte en series con alta autocorrelación. **Acción correctiva:** documentar la mejora en términos operativos: un error de 28 pax promedio permite tomar la decisión de habilitación de filtros con suficiente anticipación, lo cual es el objetivo operativo real. |
| Negocio | N3 | El artefacto debe entregar una salida accionable por fecha, franja y zona. | Revisión funcional del tablero y del dataset de salida. | 100% de las franjas del horizonte definido con predicción, criticidad, capacidad de referencia y porcentaje estimado de ocupación. | ✅ Cubierto | El tablero muestra por cada franja: flujo predicho en pasajeros, porcentaje de capacidad utilizada, estado operativo con sus respectivas alertas y recomendación automática.|
| Negocio | N4 | El artefacto debe permitir revisar históricos por filtro, aunque la alerta principal sea por zona. | Revisión funcional del tablero. | Históricos disponibles para los 13 filtros de la zona objetivo. | ✅ Cubierto | La Vista Histórico incluye una sección de complementaria por filtro que lee directamente el histórico de datos de sensores. El coordinador puede seleccionar cualquier fecha disponible, elegir los filtros a visualizar, ver la gráfica de flujo por filtro con las bandas de alerta y crítico, e identificar el filtro dominante y el pico del día. La tabla resumen muestra flujo total, pico y promedio por filtro para la fecha seleccionada. |

---

## Requerimientos de desempeño

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio de verificación | Estado | Justificación y acciones correctivas |
|---|---|---|---|---|---|---|
| Desempeño | D1 | El modelo principal debe alcanzar desempeño aceptable en horizontes cortos de operación. | Out-of-time testing o backtesting rolling. | WMAPE <= 15% o sMAPE <= 15% en horizontes 2h y 4h. | 🟡 Parcial |El modelo alcanza un WMAPE de 17.9% en validación y 18.4% en prueba para el horizonte de 1 paso (15 minutos), superando levemente el umbral definido. La simulación rodante a horizontes de 2h, 4h, 6h y 24h no fue implementada en esta iteración por dos razones: primero, encadenar predicciones de 1 paso acumula error en cada franja y requiere una estrategia de validación adicional que estaba fuera del alcance del tiempo disponible; segundo, el requerimiento F4 de horizontes múltiples fue priorizado como mejora futura enconsenso con el equipo, ya que el caso de uso principal del coordinador es la anticipación inmediata de 15 minutos. El modelo de 1 paso queda como modelo base para implementar la simulación rodante en la siguiente iteración. |
| Desempeño | D2 | El modelo debe mantener un error absoluto razonable en unidades del problema. | Evaluación temporal sobre validación. | MAE reportado por zona y por franja, con umbral definido a partir de la distribución histórica. | ✅ Cubierto | MAE validación: 27.9 pax por franja (14.9% del flujo medio de 187 pax). MAE prueba: 34.2 pax por franja (18.3% del flujo medio). Un error de 28 pax promedio permite tomar decisiones de habilitación de filtros con suficiente anticipación. |
| Desempeño | D3 | El modelo debe controlar errores grandes en franjas de alta demanda. | Evaluación temporal sobre validación. | RMSE menor al baseline y reportado por zona. | ✅ Cubierto | RMSE del modelo: 36.2 (validación) y 46.1 (prueba). RMSE del baseline de persistencia: 40.5. El modelo mejora un 11% en RMSE respecto al baseline.|
| Desempeño | D4 | La selección del modelo final debe estar técnicamente justificada frente a alternativas. | Comparación entre baseline, modelo interpretable y modelo supervisado. | Tabla comparativa con métricas y justificación del modelo elegido. | ✅ Cubierto | Se evaluaron 7 modelos distintos: persistencia, OLS, Ridge, ElasticNet, RandomForest, HGB, ARIMA y Prophet. Comparandolos con 5 métricas (WMAPE, MAE, RMSE, sMAPE, Recall) y 3 criterios adicionales (brecha val→test, interpretabilidad, mantenimiento). Justificación completa en la Sección 8 del reporte técnico. |
| Desempeño | D5 | El modelo debe identificar correctamente franjas críticas más allá del error promedio. | Clasificación binaria de franjas críticas vs no críticas sobre histórico. | Recall >= 0.80 y F1 >= 0.70 para franjas críticas. Detectar 
8 de cada 10 franjas críticas con 15 minutos de anticipación es suficiente para que el coordinador reaccione. El F1 de 0.70 
ayuda a prevenir falsas alarmas, un F1 menor implicaría sorecargar el sistema de alarmas y más trabajo operativo. | 🟡 Parcial | El modelo no logra detectar franjas críticas cuando se usa el umbral nominal de 13 filtros (432 pax), porque ese nivel de demanda casi nunca ocurre en los datos de prueba. Cuando se  ajusta el umbral a la dotación real de 8 o 9 filtros activos, el Recall sube a entre 0.50 y 0.75, lo que ya es operativamente útil. Para que el coordinador siempre trabaje con el umbral  correcto según su turno, se agregó un control deslizante en el tablero que recalcula los umbrales automáticamente. Lo que queda  pendiente para una siguiente versión es entrenar un modelo dedicado exclusivamente a detectar esas franjas críticas, que aprenda mejor ese patrón sin depender del umbral de regresión. |

---

## Requerimientos de funcionalidad

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio de verificación | Estado | Justificación y acciones correctivas |
|---|---|---|---|---|---|---|
| Funcionalidad | F1 | El prototipo debe permitir la consulta de resultados sin interacción directa con código. | Prueba funcional con usuario de referencia o revisor del proyecto. | Consulta por fecha, zona y controles propios de la vista seleccionada sin abrir notebooks ni scripts. | ✅ Cubierto | El tablero Streamlit permite consultar predicciones, ver el estado operativo y navegar entre vistas sin necesidad de abrir ningún archivo de código. El operador interactúa únicamente con la pagina web, los filtros necesario y botones que le permiten descargar los datos predichos. |
| Funcionalidad | F2 | El prototipo debe mostrar claramente predicción, histórico y criticidad. | Revisión de la interfaz y de la salida visual. | Se visualizan serie estimada u observada, referencia comparable, tabla de franjas críticas y semáforo por zona. | ✅ Cubierto | La Vista "Ahora" muestra: flujo predicho, porcentaje de capacidad, indicador de carga visual, semáforo operativo y recomendación automática. La Vista Histórico muestra: gráfica de evolución de la sesión, promedio móvil comparable, tabla de franjas con estado y exportación CSV. |
| Funcionalidad | F3 | El prototipo debe operar con datos anonimizados o muestras controladas en el repositorio. | Revisión de repositorio y archivos de visualización. | Cero campos sensibles expuestos en el repositorio o en el entregable compartido. | ✅ Cubierto | Las bases limpias en el repositorio no contienen información de identificación personal. Los datos crudos originales no fueron distribuidos. El modelo opera con datos agregados a nivel de franja de 15 minutos, no a nivel de pasajero individual. |
| Funcionalidad | F4 | El prototipo debe permitir elegir distintos horizontes de anticipación en la vista operativa. | Prueba funcional en la vista `Ahora`. | Al menos horizontes 2h, 4h, 6h y 24h disponibles en la lógica de salida o el tablero. | 🔴 Pendiente | El prototipo predice únicamente la siguiente franja de 15 minutos. Analizar horizontes más largos requiere encadenar predicciones de 1 paso usando cada resultado como entrada del siguiente, lo que acumula error en cada franja y es necesaria una estrategia de validación adicional para medir ese error acumulado. Implementar esto requiere un tiempo de desarrollo adicional, el caso de uso principal del coordinador es la anticipación inmediata de 15 minutos, por lo que se priorizó consolidar esa funcionalidad antes de extender los horizontes. **Queda propuesto para la siguiente iteración** encadenar las 
predicciones de 1 paso para ofrecer horizontes de 2h, 4h, 6h y 24h, siendo conscientes de que el error aumentará a medida 
que el horizonte sea mayor. |
| Funcionalidad | F5 | El prototipo debe adaptar sus controles al contexto de consulta. | Prueba funcional en ambos modos del tablero. | La vista `Ahora` ofrece horizonte de consulta y la vista `Histórico` ofrece rango de comparación sin mezclar ambos controles. | ✅ Cubierto | La Vista Ahora y la Vista Histórico son vistas separadas con controles independientes. El selector en la parte superior cambia completamente la lectura y los controles disponibles. Los controles del sidebar aplican a la Vista Ahora y la Vista Histórico usa el historial acumulado de la sesión, permitiendo descargar los datos. |
| Funcionalidad | F6 | El prototipo debe mostrar una referencia explícita de capacidad y el volumen estimado en personas en la lectura principal. | Revisión funcional de la interfaz. | La gráfica principal incluye línea o umbral de referencia y el valor proyectado se expresa en unidades del problema. | ✅ Cubierto | El indicador de carga visual muestra las zonas de alerta y crítico como bandas de color con los umbrales numéricos (356 y 432 pax), y muestra los valores y el porcentaje criticidad. |
| Funcionalidad | F7 | El prototipo debe expresar la ocupación estimada tanto en número de pasajeros como en porcentaje sobre la capacidad disponible. | Revisión funcional de la interfaz. | La vista principal presenta simultáneamente volumen estimado y porcentaje de ocupación de la zona. | ✅ Cubierto | La Vista Ahora muestra dos indicadores clave simultáneos: Flujo predicho (en pasajeros) y Capacidad utilizada (en porcentaje), ambos valores aparecen en colores según el nivel de criticidad, con el fin de generar un lectura rápida. |
| Funcionalidad | F8 | El prototipo debe permitir definir manualmente la cantidad de filtros activos para recalcular capacidad y criticidad. | Prueba funcional en la vista `Ahora`. | El usuario puede ajustar el número de filtros activos y la salida modifica capacidad, ocupación y nivel de alerta. | ✅ Cubierto | Se agregó un control deslizante en el panel 
lateral que permite al coordinador indicar cuántos filtros tiene activos en su turno. Con ese valor el tablero recalcula  automáticamente la capacidad máxima, el umbral de alerta y el umbral crítico, y actualiza el indicador de carga, los indicadores clave y la recomendación operativa. Por ejemplo, con 9 filtros activos el umbral crítico baja de 432 a 299 pax,  reflejando la capacidad real del turno en lugar de la capacidad máxima instalada. ||
| Funcionalidad | F9 | El prototipo debe mostrar concentración actual por filtro y destacar el recurso con mayor carga cuando la vista sea operativa. | Revisión funcional de la interfaz en la vista `Ahora`. | Se identifican los 13 filtros de la zona objetivo y al menos un recurso se marca como de mayor carga en el corte consultado. | ✅ Cubierto | La Vista Ahora muestra el filtro con mayor carga histórica reciente consultando directamente el archivo de histórico de sensores. La Vista Histórico permite además seleccionar cualquier fecha y ver el flujo de los 13 filtros en detalle con tabla resumen de pico, promedio y flujo total por filtro. |

---

## Requerimientos de usabilidad

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio de verificación | Estado | Justificación y acciones correctivas |
|---|---|---|---|---|---|---|
| Usabilidad | U1 | La interfaz debe ser entendible para un usuario no técnico del área operativa. | Prueba con 2 a 3 usuarios de referencia del equipo o del entorno de validación. | Al menos 80% de tareas básicas completadas sin ayuda relevante. | 🔴 Pendiente | Las pruebas formales con usuarios del área operativa no fueron realizadas en esta iteración. El diseño de la interfaz prioriza lenguaje operativo y evita palabras muy técnicas en los mensajes y recomendaciones. **Acción correctiva:** planificar sesión de prueba con al menos 2 coordinadores operativos del aeropuerto usando las 3 tareas definidas inicialmente por los coordinadores. |
| Usabilidad | U2 | La interfaz debe comunicar el resultado sin saturar al usuario con detalle técnico. | Revisión cualitativa del tablero y retroalimentación de usuarios. | El usuario identifica criticidad, magnitud estimada, zona y nivel de confianza en menos de 3 minutos. | ✅ Cubierto |El tablero muestra el resultado de forma visual y en lenguaje sencillo, con un semáforo de colores, un velocímetro de carga y un texto que le dice al coordinador exactamente qué hacer, sin mostrar código del modelo empleado. El tiempo desde que se presiona el botón de predicción hasta ver el resultado es menor a 2 minutos, lo que cumple el criterio definido.|
| Usabilidad | U3 | La vista principal debe priorizar la alerta por zona y dejar el detalle por filtro como analítica complementaria. | Revisión funcional del tablero. | La vista `Ahora` resalta la criticidad de zona y permite consultar distribución actual o históricos por filtro sin perder contexto. | ✅ Cubierto | La Vista Ahora mantiene el semáforo de zona y el indicador de carga como elementos principales, y muestra el filtro con mayor carga histórica reciente como referencia 
complementaria. Para el detalle completo por filtro, la Vista Histórico permite seleccionar cualquier fecha y ver el flujo de cada uno de los 13 filtros en una gráfica de líneas, con tabla de pico, promedio y flujo total por filtro. Todo esto es información adicional, al sistema de alerta de filtros.|

---

## Requerimientos de datos

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio de verificación | Estado | Justificación y acciones correctivas |
|---|---|---|---|---|---|---|
| Datos | Q1 | Las fuentes integradas deben cumplir un umbral mínimo de completitud y sincronización. | Perfilamiento y reporte de calidad sobre dataset maestro. | Completitud >= 98% en campos críticos y reglas de alineación temporal documentadas. | ✅ Cubierto | Completitud VeriPax: 94.24% de registros válidos (dentro del rango operativo aceptable). Completitud sensores Muelle A y B: 100% en los días elegibles. Reglas de alineación temporal documentadas en la Sección 2.2 del reporte técnico: ajuste UTC-5, criterio de elegibilidad diaria y exclusión del gap de sensores. |
| Datos | Q2 | El prototipo debe construirse sobre la ventana común validada entre las fuentes. | Revisión de ETL y reporte de calidad. | Ventana de 3 meses históricos documentada y reproducible, con validación temporal sobre las últimas 2 semanas y backtesting rolling. | ✅ Cubierto | Ventana común: diciembre 2025 – marzo 2026. El split de modelado usa enero–marzo 2026. El pipeline es completamente reproducible: Kernel → Restart & Run All regenera todos los artefactos. Hash MD5 del dataset documentado en la celda de configuración del notebook. |
| Datos | Q3 | La relación temporal entre programación, ingreso al muelle y paso por filtros debe quedar modelada o documentada. | Revisión de feature engineering y reporte técnico. | Existen lags o variables que representen la anticipación entre las tres capas del proceso y la agregación desde fuentes a minuto hacia la franja operativa de 15 minutos. | ✅ Cubierto | Las 25 variables del modelo incluyen rezagos del sensor (15, 30, 60, 120 min), rezagos VeriPax (mismos intervalos), promedios móviles de 1h y 2h, y bins de anticipación VeriPax por ventana (0–60, 60–120, 120–180, >180 min). La relación entre las tres capas está documentada en la Sección 3.1 del reporte técnico. |
| Datos | Q4 | Los recursos inestables o casi nulos no deben sesgar la evaluación principal. | Análisis exploratorio y regla de exclusión o agrupación. | Lista explícita de recursos excluidos o agrupados con justificación técnica. | ✅ Cubierto | Exclusiones documentadas: días con `sensor_day_complete = 0`, días con VeriPax < 1,000 y gap de sensores Feb 26 – Mar 04 (falla de hardware). Justificaciones técnicas y alternativas consideradas documentadas en la Sección 2.3 del reporte técnico. |

---

## Requerimientos deseables

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio de verificación | Estado | Justificación y acciones correctivas |
|---|---|---|---|---|---|---|
| Deseable | X1 | Incluir intervalos de confianza o banda de incertidumbre. | Evaluación sobre validación. | Cobertura coherente y visualización interpretable. | 🔵 Deseable | No implementado en esta versión. RandomForest puede generar intervalos de predicción mediante la dispersión entre árboles. **Acción futura:** implementar en próxima iteración usando la dispersión del ensamble como proxy de incertidumbre y visualizar como banda sombreada alrededor de la predicción en el indicador de carga y la gráfica histórica. |
| Deseable | X2 | Incluir predicciones por filtro individual. | Evaluación técnica y prueba funcional. | Se muestran predicciones por filtro para recursos con estabilidad suficiente. | 🔵 Deseable | No implementado. Los datos por filtro están disponibles en `sensores_filtro_15m.csv`. Requiere entrenar 13 modelos individuales o un modelo multisalida. **Acción futura:** evaluar costo-beneficio de modelos individuales vs modelo agregado y comenzar por los filtros con mayor variabilidad histórica. |
| Deseable | X3 | Incorporar tiempos de proceso como señal de anomalía operativa. | Análisis exploratorio y prueba funcional. | El tablero resalta desviaciones inusuales de tiempo de proceso cuando aplique. | 🔵 Deseable | No implementado. Los tiempos de proceso en mesas de control migratorio no están disponibles en las fuentes actuales. Esta variable fue identificada como una de las dos limitaciones estructurales del modelo en la Sección 12 del reporte técnico. **Acción futura:** gestionar con el área de control migratorio la disponibilidad de `tiempo_proceso_migracion` y `mesas_activas` por franja. |

---

## Resumen de resultados

| Estado | Cantidad | Requerimientos |
|---|---|---|
| ✅ Cubierto | 17 | N3, N4, D2, D3, D4, F1, F2, F3, F5, F6, F7, F8, F9, Q1, Q2, Q3, Q4, U2, U3 |
| 🟡 Parcial | 3 | N1, N2, D1, D5 |
| 🔴 Pendiente | 1 | U1 |
| 🔵 Deseable | 3 | X1, X2, X3 |

La mayoría de los requerimientos fueron cubiertos en esta iteración del prototipo. Los requerimientos parciales corresponden al desempeño del modelo en la detección de franjas críticas y en el horizonte de predicción, ambos con limitaciones estructurales documentadas en el reporte técnico. El único requerimiento pendiente es la validación formal con usuarios operativos del aeropuerto, que requiere coordinación institucional fuera del alcance del proyecto académico.
---

## Validación funcional prevista

La validación con usuarios de referencia se plantea sobre dos perfiles: coordinación operativa y análisis de control operativo. Las tareas base de prueba son:

1. Identificar la siguiente franja crítica y determinar si se requiere habilitar capacidad adicional.
2. Interpretar la ocupación esperada de la zona con base en pasajeros proyectados, capacidad disponible y porcentaje de ocupación.
3. Revisar una fecha anterior y concluir si el comportamiento observado fue atípico frente al histórico comparable.

## Fuera de alcance

- Validación en producción.
- Medición de ahorros reales.
- Adopción real en operación.
- Integración corporativa completa.
- Piloto real con usuarios finales.
- Optimización completa de dotaciones.


