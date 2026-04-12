# Tabla de Requerimientos Final

![Banner del prototipo](assets/Banner_PAAD_01.jpg)

## Alcance de evaluacion

Los criterios se definen para una validacion controlada del prototipo. Por tanto, no dependen de despliegue en produccion, medicion de ahorros reales ni adopcion operativa en ambiente real.

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio o metrica de evaluacion |
|---|---|---|---|---|
| Negocio | N1 | El artefacto debe identificar franjas criticas de demanda a nivel zona para apoyar la habilitacion de filtros y la redistribucion de recursos. | Backtesting sobre historico, marcando como criticas las franjas de 15 minutos por percentil o umbral operativo definido. | Recall >= 0.80 en identificacion de franjas criticas. |
| Negocio | N2 | El artefacto debe mejorar la anticipacion frente a un baseline operativo simple. | Comparacion contra baseline naive o promedio historico por franja. | Mejora >= 10% en WMAPE o sMAPE respecto al baseline. |
| Negocio | N3 | El artefacto debe entregar una salida accionable por fecha, franja y zona. | Revision funcional del tablero y del dataset de salida. | 100% de las franjas del horizonte definido con prediccion, criticidad, capacidad de referencia y porcentaje estimado de ocupacion. |
| Negocio | N4 | El artefacto debe permitir revisar historicos por filtro, aunque la alerta principal sea por zona. | Revision funcional del tablero. | Historicos disponibles para los 13 filtros de la zona objetivo. |
| Desempeno | D1 | El modelo principal debe alcanzar desempeno aceptable en horizontes cortos de operacion. | Out-of-time testing o backtesting rolling. | WMAPE <= 15% o sMAPE <= 15% en horizontes 2h y 4h. |
| Desempeno | D2 | El modelo debe mantener un error absoluto razonable en unidades del problema. | Evaluacion temporal sobre validacion. | MAE reportado por zona y por franja, con umbral definido a partir de la distribucion historica. |
| Desempeno | D3 | El modelo debe controlar errores grandes en franjas de alta demanda. | Evaluacion temporal sobre validacion. | RMSE menor al baseline y reportado por zona. |
| Desempeno | D4 | La seleccion del modelo final debe estar tecnicamente justificada frente a alternativas. | Comparacion entre baseline, modelo interpretable y modelo supervisado. | Tabla comparativa con metricas y justificacion de modelo elegido. |
| Desempeno | D5 | El modelo debe identificar correctamente franjas criticas mas alla del error promedio. | Clasificacion binaria de franjas criticas vs no criticas sobre historico. | Recall >= 0.80 y F1 >= 0.70 para franjas criticas. |
| Funcionalidad | F1 | El prototipo debe permitir la consulta de resultados sin interaccion directa con codigo. | Prueba funcional con usuario de referencia o revisor del proyecto. | Consulta por fecha, zona y controles propios de la vista seleccionada sin abrir notebooks ni scripts. |
| Funcionalidad | F2 | El prototipo debe mostrar claramente prediccion, historico y criticidad. | Revision de la interfaz y de la salida visual. | Se visualizan serie estimada u observada, referencia comparable, tabla de franjas criticas y semaforo por zona. |
| Funcionalidad | F3 | El prototipo debe operar con datos anonimizados o muestras controladas en el repositorio. | Revision de repositorio y archivos de visualizacion. | Cero campos sensibles expuestos en repo o entregable compartido. |
| Funcionalidad | F4 | El prototipo debe permitir elegir distintos horizontes de anticipacion en la vista operativa. | Prueba funcional en la vista `Ahora`. | Al menos horizontes 2h, 4h, 6h y 24h disponibles en la logica de salida o el tablero. |
| Funcionalidad | F5 | El prototipo debe adaptar sus controles al contexto de consulta. | Prueba funcional en ambos modos del tablero. | La vista `Ahora` ofrece horizonte de consulta y la vista `Historico` ofrece rango de comparacion sin mezclar ambos controles. |
| Funcionalidad | F6 | El prototipo debe mostrar una referencia explicita de capacidad y el volumen estimado en personas en la lectura principal. | Revision funcional de la interfaz. | La grafica principal incluye linea o umbral de referencia y el valor proyectado se expresa en unidades del problema. |
| Funcionalidad | F7 | El prototipo debe expresar la ocupacion estimada tanto en numero de pasajeros como en porcentaje sobre la capacidad disponible. | Revision funcional de la interfaz. | La vista principal presenta simultaneamente volumen estimado y porcentaje de ocupacion de la zona. |
| Funcionalidad | F8 | El prototipo debe permitir definir manualmente la cantidad de filtros activos para recalcular capacidad y criticidad. | Prueba funcional en la vista `Ahora`. | El usuario puede ajustar el numero de filtros activos y la salida modifica capacidad, ocupacion y nivel de alerta. |
| Funcionalidad | F9 | El prototipo debe mostrar concentracion actual por filtro y destacar el recurso con mayor carga cuando la vista sea operativa. | Revision funcional de la interfaz en la vista `Ahora`. | Se identifican los 13 filtros de la zona objetivo y al menos un recurso se marca como mayor carga en el corte consultado. |
| Usabilidad | U1 | La interfaz debe ser entendible para un usuario no tecnico del area operativa. | Prueba con 2 a 3 usuarios de referencia del equipo o del entorno de validacion. | Al menos 80% de tareas basicas completadas sin ayuda relevante. |
| Usabilidad | U2 | La interfaz debe comunicar el resultado sin saturar al usuario con detalle tecnico. | Revision cualitativa del tablero y feedback de usuarios. | El usuario identifica criticidad, magnitud estimada, zona y nivel de confianza en menos de 3 minutos. |
| Usabilidad | U3 | La vista principal debe priorizar la alerta por zona y dejar el detalle por filtro como analitica complementaria. | Revision funcional del tablero. | La vista `Ahora` resalta la criticidad de zona y permite consultar distribucion actual o historicos por filtro sin perder contexto. |
| Datos | Q1 | Las fuentes integradas deben cumplir un umbral minimo de completitud y sincronizacion. | Perfilamiento y reporte de calidad sobre dataset maestro. | Completitud >= 98% en campos criticos y reglas de alineacion temporal documentadas. |
| Datos | Q2 | El prototipo debe construirse sobre la ventana comun validada entre las fuentes. | Revision de ETL y reporte de calidad. | Ventana de 3 meses historicos documentada y reproducible, con validacion temporal sobre las ultimas 2 semanas y backtesting rolling. |
| Datos | Q3 | La relacion temporal entre programacion, ingreso al muelle y paso por filtros debe quedar modelada o documentada. | Revision de feature engineering y reporte tecnico. | Existen lags o variables que representen la anticipacion entre las tres capas del proceso y la agregacion desde fuentes a minuto hacia la franja operativa de 15 minutos. |
| Datos | Q4 | Los recursos inestables o casi nulos no deben sesgar la evaluacion principal. | Analisis exploratorio y regla de exclusion o agrupacion. | Lista explicita de recursos excluidos o agrupados con justificacion tecnica. |

## Deseables

| Aspecto | ID | Requerimiento | Prueba prevista | Criterio o metrica |
|---|---|---|---|---|
| Deseable | X1 | Incluir intervalos de confianza o banda de incertidumbre. | Evaluacion sobre validacion. | Cobertura coherente y visualizacion interpretable. |
| Deseable | X2 | Incluir predicciones por filtro individual. | Evaluacion tecnica y prueba funcional. | Se muestran predicciones por filtro para recursos con estabilidad suficiente. |
| Deseable | X3 | Incorporar tiempos de proceso como senal de anomalia operativa. | Analisis exploratorio y prueba funcional. | El tablero resalta desviaciones inusuales de tiempo de proceso cuando aplique. |

## Base de formulacion

Los requerimientos se apoyan en evidencia previa:

- patrones horarios ya observados,
- limpieza y homologacion documentadas,
- ventana comun construida,
- levantamiento funcional documentado en anexo,
- necesidad diferenciada de seguimiento intradia y comparacion retrospectiva,
- existencia de tres capas del proceso: programacion, ingreso al muelle y paso por filtros.

## Validacion funcional prevista

La validacion con usuarios de referencia se plantea sobre dos perfiles: coordinacion operativa y analisis de control operativo. Las tareas base de prueba son:

1. identificar la siguiente franja critica y determinar si se requiere habilitar capacidad adicional;
2. interpretar la ocupacion esperada de la zona con base en pasajeros proyectados, capacidad disponible y porcentaje de ocupacion;
3. revisar una fecha anterior y concluir si el comportamiento observado fue atipico frente al historico comparable.

## Fuera de alcance

- validacion en produccion,
- medicion de ahorros reales,
- adopcion real en operacion,
- integracion corporativa completa,
- piloto real con usuarios finales,
- optimizacion completa de dotaciones.
