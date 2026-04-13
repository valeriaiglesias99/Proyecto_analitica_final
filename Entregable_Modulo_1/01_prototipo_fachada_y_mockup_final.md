# Prototipo Fachada y Mockup Final

![Banner del prototipo](assets/Banner_PAAD_01.jpg)

## 1. Nombre del artefacto

Tablero predictivo para planificación táctica de demanda en filtros de una zona internacional de control.

## 2. Usuario final y necesidad

### Perfiles de usuario identificados

| Perfil | Rol dentro del caso | Necesidad principal | Salida esperada | Prioridad |
|---|---|---|---|---|
| Coordinador de operaciones | Monitorea flujos intradía y decide la habilitación de filtros y la redistribución de recursos. | Anticipar picos de demanda con suficiente tiempo para actuar. | Semáforo por zona, línea temporal, franjas críticas y nivel de confianza visible. | Alta |
| Analista de control operativo | Revisa históricos, valida comportamientos atípicos y analiza patrones por recurso. | Entender comportamiento pasado, contrastar días comparables y revisar detalle por filtro. | Históricos comparables, trazabilidad temporal y analítica complementaria por filtro. | Media |
| Responsable táctico o de supervisión | Revisa desempeño general, necesidades de capacidad y comportamiento agregado de la operación. | Contar con una vista sintética del comportamiento esperado y observado para seguimiento operativo. | Resumen agregado por zona, franjas críticas del día y comparación general contra histórico. | Media-baja |

### Usuario priorizado

El usuario principal priorizado es el coordinador de operaciones encargado de monitorear flujos, emitir alertas y decidir la habilitación de recursos en filtros durante el día.

### Sustento de la priorización

La priorización se soporta en el Anexo 1. Entrevista funcional y validación de datos, que hará parte del entregable en formato PDF, y en la naturaleza operativa del caso:

- en la entrevista, el usuario consultado se identifica como coordinador de operaciones y declara que sus decisiones centrales son habilitar filtros, alertar congestión y redistribuir recursos;
- el horizonte de mayor valor declarado es de 2h a 4h, lo cual corresponde a decisiones intradía y no a seguimiento directivo de largo plazo;
- la granularidad requerida de 15 minutos y la necesidad de una alerta por zona evidencian un uso operativo de alta frecuencia;
- el requerimiento de acceso visual simple y sin código confirma que la primera capa del artefacto debe responder a un usuario de acción rápida;
- la necesidad de revisar históricos por filtro sugiere un segundo perfil analítico, orientado a validación y seguimiento;
- la lectura agregada por zona también puede ser consumida por un perfil de supervisión, pero no es el usuario crítico para definir el MVP, dado que el valor diferencial del artefacto se concentra en la anticipación operativa.

### Necesidad a resolver

La operación hoy reacciona tarde a cambios de demanda. El usuario necesita anticipar el flujo de pasajeros con granularidad de 15 minutos para tomar decisiones tácticas sobre habilitación de filtros y distribución de recursos, con especial foco en horizontes cortos del mismo día. Aunque algunas fuentes operativas se registran a nivel de minuto, el artefacto consolida la lectura y la predicción en franjas de 15 minutos para reducir ruido y facilitar decisiones operativas.

## 3. Problema de negocio

Cómo anticipar, con granularidad de 15 minutos y horizontes operativos de 2, 4, 6 y hasta 24 horas, las franjas con mayor flujo esperado en filtros de la zona internacional objetivo para apoyar decisiones de habilitación y distribución de recursos.

## 4. Modelo lógico de impacto

### Input

- programación de vuelos,
- registros de validación de ingreso al muelle,
- sensores de paso por filtros,
- variables calendario y catálogos auxiliares.

### Output

- pronóstico por franja de 15 minutos,
- semáforo de criticidad por zona,
- vista operativa `Ahora` para seguimiento intradía,
- vista `Histórico` para comparación retrospectiva,
- histórico comparable,
- detalle histórico por filtro,
- distribución actual del flujo por filtro y recurso con mayor carga,
- capacidad de referencia visible en la lectura principal, en unidades absolutas y relativas,
- porcentaje de ocupación estimada respecto a la capacidad disponible,
- nivel visible de confianza o calidad de la predicción.

### Outcome esperado

- mejor anticipación de franjas críticas,
- menor reacción tardía ante congestión,
- mejor habilitación táctica de filtros.

## 5. Indicadores y métricas de impacto esperadas

En esta fase se priorizan indicadores proxy evaluables offline:

- capacidad de identificar franjas críticas,
- mejora frente a baseline histórico simple,
- cobertura de las franjas y horizontes útiles para planeación,
- confiabilidad visible de la alerta para el usuario.

## 6. Alcance del MVP

### Must

- integración de tres fuentes prioritarias,
- predicción cada 15 minutos,
- alerta principal por zona,
- doble vista global `Ahora / Histórico`,
- parámetro manual para definir cantidad de filtros activos,
- históricos por filtro,
- comparación contra baseline,
- horizontes de 2h, 4h, 6h y 24h,
- muestra anonimizada o controlada para visualización.

### Should

- indicador visible de confianza,
- predicción por filtro cuando el recurso tenga estabilidad suficiente.

### Could

- recomendación simple basada en reglas,
- tiempos de proceso como señal de anomalía operacional.

### Fuera de alcance

- optimización completa de dotaciones,
- despliegue productivo,
- medición real de ahorros,
- adopción real en operación,
- integración corporativa completa.

## 7. Forma de uso esperada

El usuario accede a un tablero de consulta sin código y puede:

- elegir la vista general del informe entre `Ahora` y `Histórico`,
- seleccionar fecha, zona y granularidad de lectura,
- definir manualmente la cantidad de filtros activos para el corte o escenario consultado,
- escoger horizonte de consulta cuando se encuentre en la vista `Ahora`,
- escoger rango de comparación cuando se encuentre en la vista `Histórico`,
- revisar el estado de criticidad de la zona y su contraste contra capacidad de referencia,
- revisar la ocupación estimada frente a la capacidad disponible en número de pasajeros y porcentaje,
- comparar pronóstico contra histórico comparable,
- consultar distribución actual del flujo por filtro o analítica histórica por filtro según la vista elegida,
- revisar el nivel de confianza visible.

## 8. Flujo de interacción del usuario

1. El coordinador ingresa a la interfaz al inicio de la jornada o durante la operación intradía.
2. Define la vista general del informe según la necesidad del momento: `Ahora` para seguimiento operativo o `Histórico` para análisis retrospectivo.
3. Si se encuentra en `Ahora`, selecciona fecha, horizonte operativo y cantidad de filtros activos; si se encuentra en `Histórico`, selecciona la fecha analizada y el rango de comparación.
4. Revisa la vista principal de zona para identificar rápidamente el nivel de criticidad esperado, su relación con la capacidad de referencia y el porcentaje de ocupación estimado.
5. Contrasta la demanda estimada u observada con el histórico comparable para determinar si el comportamiento es normal, de alerta o atípico.
6. Consulta la tabla de franjas priorizadas para ubicar los periodos en los que podría requerirse habilitación adicional de filtros.
7. Navega al detalle por filtro: en `Ahora` revisa distribución actual del flujo y recurso con mayor carga; en `Histórico` revisa comportamiento pasado por fecha y comparativo.
8. Con base en la lectura agregada y el detalle complementario, decide habilitar filtros, redistribuir recursos o mantener la configuración actual.
9. En cortes posteriores del día, repite la consulta para actualizar la lectura operativa y verificar si la criticidad prevista se mantiene, aumenta o disminuye.

### Salidas que consume cada perfil

- coordinador de operaciones:
  semáforo por zona, franjas críticas, línea temporal y nivel visible de confianza;
- analista de control operativo:
  históricos comparables, detalle por filtro y trazabilidad del comportamiento observado;
- responsable táctico o de supervisión:
  resumen agregado, comparación general contra histórico y lectura sintética del estado esperado de la operación.

## 9. Decisiones de diseño justificadas

### El tablero es la forma de uso principal del artefacto

- el caso requiere lectura rápida de múltiples elementos al mismo tiempo: criticidad, línea temporal, comparación histórica y detalle por filtro;
- la consulta principal se realiza en un contexto de monitoreo operativo donde una vista consolidada tiene mayor valor que una interacción móvil reducida;
- un tablero facilita comparación visual, jerarquía de alertas y navegación entre zona y filtro sin aumentar complejidad de desarrollo;
- una aplicación móvil puede ser una extensión futura, pero no es la forma prioritaria para el MVP dado el tipo de decisión y el entorno de uso esperado.

### La interfaz de consulta tiene prioridad sobre una API como producto visible

- la necesidad del usuario no es consumir un servicio técnico aislado, sino interpretar rápidamente una situación operativa;
- la salida requiere semáforos, históricos comparables y una lectura visual de franjas críticas, elementos que una API por sí sola no resuelve para el usuario final;
- una API podría existir como componente técnico interno, pero la forma de uso principal del artefacto debe ser una interfaz de consulta.

### La actualización por cortes es suficiente para el valor operativo buscado

- el valor principal de la solución está en anticipar ventanas de 2h a 4h para apoyar decisiones tácticas, no en reaccionar a eventos de segundos;
- la granularidad operativa definida es de 15 minutos, lo cual hace viable una lógica de actualización por cortes temporales sin perder utilidad funcional;
- una arquitectura de streaming completo incrementaría complejidad de integración, monitoreo y validación sin ser indispensable para demostrar utilidad del artefacto en esta fase;
- por tanto, la solución se plantea con procesamiento reproducible por ventanas de tiempo y posibilidad de evolucionar hacia una mayor frecuencia de actualización.

### La alerta principal se concentra a nivel zona

- la decisión primaria del usuario se toma a nivel zona, donde se evalúa la necesidad de habilitar recursos adicionales;
- el comportamiento por filtro es valioso como analítica complementaria, pero no siempre todos los filtros están habilitados ni tienen estabilidad suficiente para soportar una alerta principal independiente;
- priorizar la zona mejora robustez del MVP y deja el detalle por filtro como segunda capa de análisis.

### La capacidad operativa se controla con un parámetro manual de filtros activos

- la operación requiere evaluar escenarios con diferente cantidad de filtros habilitados durante el día;
- permitir al usuario ajustar manualmente el número de filtros activos mantiene el artefacto conectado con la decisión operativa real sin exigir una capa prescriptiva completa;
- este parámetro modifica la capacidad disponible y, por tanto, la lectura de ocupación y criticidad;
- la definición manual del número de filtros activos es suficientemente simple para el MVP y evita comprometer una programación operativa completa de recursos.

### La separación entre `Ahora` e `Histórico` mejora la lectura del artefacto

- el usuario operativo necesita una lectura rápida de corto plazo, mientras que el perfil analítico necesita explorar comparativos retrospectivos sin contaminar la vista principal de monitoreo;
- mantener ambos usos en una sola pantalla sin separación contextual aumenta carga cognitiva y dificulta la interpretación inmediata;
- la vista `Ahora` prioriza horizonte, criticidad, capacidad de referencia y concentración actual por filtro;
- la vista `Histórico` prioriza fecha analizada, rango de comparación, comportamiento observado y patrones repetitivos;
- esta separación conserva coherencia funcional entre perfiles y evita duplicar productos distintos para una misma necesidad.

### Los controles cambian según la vista seleccionada para reducir ambigüedad

- en `Ahora` el usuario necesita elegir horizonte de anticipación, porque la pregunta es qué pasará en las próximas horas;
- en `Histórico` el usuario necesita elegir rango de comparación, porque la pregunta es cómo se comportó una fecha frente a períodos comparables;
- cambiar los controles junto con la vista reduce ambigüedad y hace que cada modo del tablero responda a una tarea concreta.

## 10. Funcionalidades esperadas

- consulta sin código,
- selector global de vista `Ahora / Histórico`,
- visualización de pronóstico cada 15 minutos,
- visualización del volumen proyectado en personas,
- línea de capacidad de referencia en la gráfica principal,
- visualización de ocupación estimada en porcentaje respecto a capacidad,
- tabla de franjas priorizadas,
- semáforo por zona,
- ajuste manual del número de filtros activos,
- distribución actual por filtro en la vista `Ahora`,
- analítica histórica por filtro en la vista `Histórico`,
- identificación del filtro con mayor carga en la lectura actual,
- trazabilidad mínima del dato y de la fecha de actualización disponible.

## 11. Tipos de análisis y modelos

### Baselines

- naive por última observación,
- promedio histórico por franja.

### Pregunta analítica 1. ¿Cómo anticipar el flujo agregado por zona en intervalos de 15 minutos?

**Alternativa 1: modelos de series de tiempo con variables exógenas**

- ejemplos: regresión dinámica, SARIMAX, Prophet o modelos equivalentes con componentes temporales;
- se consideran porque la variable objetivo tiene estructura temporal clara, estacionalidad intradía y dependencia secuencial;
- permiten incorporar señales externas como programación de vuelos y conteos de ingreso al muelle sin perder interpretabilidad;
- son especialmente pertinentes para horizontes cortos, donde la dinámica reciente del flujo tiene alto valor predictivo.

**Alternativa 2: modelos de regresión supervisada basados en árboles**

- ejemplos: Random Forest, XGBoost, LightGBM o equivalentes;
- se consideran porque el problema combina lags temporales, variables calendario, vuelos programados y señales operativas recientes;
- pueden capturar interacciones no lineales entre la demanda observada en filtros, el ingreso al muelle y la programación;
- resultan adecuados cuando se espera que la relación entre entradas y salida no sea estrictamente lineal ni puramente estacional.

**Justificación comparativa**

- los modelos de series de tiempo priorizan trazabilidad e interpretación del comportamiento intradía;
- los modelos de árboles priorizan flexibilidad predictiva y capacidad para capturar relaciones complejas entre fuentes heterogéneas;
- ambos deben compararse contra baselines simples para verificar que exista ganancia real de desempeño.

### Pregunta analítica 2. ¿Cómo identificar franjas críticas para la emisión de alertas operativas?

**Alternativa 1: clasificación derivada del pronóstico**

- consiste en transformar el pronóstico continuo en niveles de criticidad mediante umbrales, percentiles históricos o capacidad operativa de referencia;
- se considera porque conserva coherencia con la necesidad funcional principal: convertir una predicción de flujo en una alerta interpretable;
- facilita justificar cada alerta a partir de una variable continua y de reglas de negocio transparentes.

**Alternativa 2: modelo de clasificación directa**

- ejemplos: clasificación binaria o multiclase para estimar si una franja será normal, de alerta o crítica;
- se considera porque la salida operativa final es una decisión categórica y no solo un valor numérico;
- permite optimizar métricas orientadas a detección de eventos críticos, como recall y F1, aun cuando el error promedio de regresión no capture del todo el costo operativo de perder un pico.

**Justificación comparativa**

- el enfoque derivado del pronóstico es más trazable y mantiene una sola cadena analítica principal;
- la clasificación directa puede ser más útil si el objetivo operacional privilegia no omitir franjas críticas por encima de la precisión puntual;
- ambos enfoques son válidos y deben contrastarse según la estabilidad de las etiquetas de criticidad y la facilidad de adopción por parte del usuario.

### Pregunta analítica 3. ¿Cómo representar el comportamiento por filtro individual sin perder viabilidad?

**Alternativa 1: desagregación desde el pronóstico de zona**

- consiste en proyectar el total por zona y distribuirlo por filtro a partir de participaciones históricas, reglas operativas o perfiles de uso;
- se considera porque reduce complejidad, requiere menos datos por unidad y mantiene estable el MVP;
- es apropiada cuando no todos los filtros están siempre habilitados o cuando existe alta variabilidad en la activación individual.

**Alternativa 2: modelos independientes por filtro**

- consiste en entrenar modelos separados para filtros con suficiente actividad y estabilidad;
- se considera porque puede capturar diferencias reales de comportamiento entre recursos y mejorar el detalle analítico;
- es pertinente solo si existe volumen suficiente por filtro y una trazabilidad consistente de aperturas, cierres y uso.

**Justificación comparativa**

- la desagregación top-down es más simple y robusta para una primera implementación;
- los modelos por filtro ofrecen mayor granularidad, pero exigen mejor calidad de datos y una definición clara de recursos activos e inactivos;
- por esta razón, el detalle predictivo por filtro se mantiene como capacidad deseable y no como requisito central del MVP.

### Criterio general de selección

- el baseline sirve como referencia operacional mínima;
- las series de tiempo con exógenas aportan interpretabilidad y buen ajuste a la naturaleza secuencial del problema;
- la regresión supervisada aporta capacidad para capturar no linealidades e interacciones entre múltiples fuentes;
- la clasificación de criticidad permite alinear la salida con la decisión operativa final;
- la desagregación o modelado por filtro se evalúa según la estabilidad y la cobertura real de los recursos.

La optimización se deja fuera del MVP porque incrementa complejidad y no es necesaria para demostrar viabilidad analítica del prototipo.

## 12. Fuentes de datos y mini diccionario

| Fuente | Granularidad | Variable clave | Mecanismo de acceso previsto | Uso principal |
|---|---|---|---|---|
| Programación de vuelos | vuelo / tiempo programado | hora programada, destino, aerolínea, pasajeros programados | extracción desde tablas SQL Server integradas al entorno corporativo o desde exportaciones controladas derivadas de una capa refinada de esa arquitectura | señal planificada |
| Validación de ingreso al muelle | evento individual / registro base a minuto, agregable a 15 min | timestamp de paso, vuelo, aerolínea | consulta a registros operativos anonimizados, provenientes de tablas SQL Server o vistas consolidadas del entorno analítico | señal operativa intermedia |
| Sensores de filtros | conteo por recurso / registro base a minuto, agregable a 15 min | timestamp, filtro, conteo | extracción desde históricos de sensores consolidados en el entorno analítico o desde repositorios derivados de SQL Server | variable objetivo y validación de flujo real |
| Catálogos auxiliares | dimensión | aerolínea, operador, recurso | tablas maestras o dimensiones corporativas | homologación y enriquecimiento |

## 13. Acceso, ETL y data lineage

### Flujo general

1. Disponibilidad de fuentes históricas en una arquitectura medallion o en una capa analítica equivalente del entorno corporativo.
2. Extracción de la muestra controlada desde una capa refinada del entorno fuente.
3. Homologación temporal y limpieza.
4. Filtrado a la zona objetivo.
5. Agregación desde resolución base a minuto hacia franjas de 15 minutos.
6. Construcción de lags y variables calendario.
7. Consolidación del dataset maestro.
8. Entrenamiento, evaluación y scoring.
9. Publicación de salida para tablero de consulta.

### Contexto de arquitectura de datos

Las fuentes operativas del caso residen en bases de datos SQL Server y, en el entorno corporativo, su integración analítica se soporta sobre una arquitectura medallion o una capa equivalente de refinamiento progresivo del dato. Para este prototipo no se plantea una conexión productiva directa a esa arquitectura completa; por consideraciones de confidencialidad y alcance, la solución se construye sobre una muestra controlada y anonimizada, derivada de una capa refinada de dichas fuentes y suficiente para reproducir el flujo analítico del MVP.

### Regla de capacidad operativa

La capacidad de referencia de la zona se calcula a partir del número de filtros activos definido manualmente por el usuario y del tiempo promedio de proceso por pasajero. En esta versión del prototipo se toma como referencia un tiempo promedio de 23 segundos por persona. El cálculo base se formula a nivel de minuto y luego se agrega a la franja operativa de 15 minutos, de modo consistente con la resolución del tablero. La capacidad estimada se expresa tanto en número de pasajeros como en porcentaje de ocupación sobre dicha capacidad, de modo que el tablero pueda clasificar las franjas en condiciones normales, de alerta y críticas.

De manera inicial, la lectura de criticidad se plantea con estos umbrales:

- alerta desde 70% de ocupación estimada;
- criticidad desde 85% de ocupación estimada.

### Desarrollos requeridos para acceso y procesamiento

- identificación de la capa fuente y de la capa refinada desde la cual se extraerá la muestra de trabajo;
- homologación de llaves temporales entre las tres fuentes principales;
- definición de reglas de filtrado para la zona objetivo;
- agregación y consolidación de eventos desde resolución base a minuto hacia una granularidad de 15 minutos;
- construcción de variables derivadas y lags para representar anticipación operativa;
- incorporación del parámetro de filtros activos en la capa de salida para recalcular capacidad y ocupación;
- preparación de salidas consumibles por la interfaz de consulta.

### Riesgos de calidad y mitigación

- desalineación temporal entre fuentes:
  mitigación: homologación horaria y reglas de ventana común;
- recursos con comportamiento inestable:
  mitigación: exclusión o agrupación justificada;
- datos sensibles:
  mitigación: uso de muestra anonimizada en repositorio y entorno de visualización.

## 14. Diagrama esquemático del artefacto

La Figura 1 presenta el prototipo fachada del artefacto, integrando usuario, requerimientos, forma de uso, modelos, datos y procesos de ETL.

![Figura 1. Prototipo fachada del artefacto](<Diagrama 1.png>)

### Nota de alcance del diagrama

El diagrama representa la lógica funcional del MVP. No implica despliegue productivo ni integración completa con la arquitectura corporativa.

## 15. Arquitectura prevista

Adicionalmente al diagrama esquemático del artefacto, se plantea una arquitectura simplificada de la POC para representar la implementación mínima de la solución:

La Figura 2 muestra la arquitectura prevista de la solución, desde las fuentes históricas hasta la capa de consumo del resultado.

![Figura 2. Arquitectura prevista de la solución](<Diagrama 2.png>)

Esta arquitectura complementa el prototipo fachada y permite visualizar la ruta mínima desde las fuentes hasta el consumo del resultado, sin representar la arquitectura corporativa completa.

## 16. Representación visual de la interfaz

La representación visual de la interfaz se incluye en:

- [mockup_prototipo.html](assets/mockup_prototipo.html)

Esta representación incluye:

- vista global `Ahora` para seguimiento operativo,
- vista global `Histórico` para comparación retrospectiva,
- semáforo por zona,
- línea temporal de demanda,
- capacidad de referencia,
- porcentaje de ocupación respecto a capacidad,
- volumen proyectado en personas,
- parámetro manual de filtros activos,
- distribución actual por filtro,
- reporte histórico por filtro,
- cambio de controles según la vista seleccionada.

## 17. Coherencia back-end / front-end

- la alerta por zona depende del motor de scoring y la clasificación de criticidad;
- la vista `Ahora` depende del motor de pronóstico, de la clasificación de criticidad y de la disponibilidad de los últimos cortes de datos;
- la vista `Histórico` depende del histórico consolidado y de la lógica de comparación por fecha o ventana equivalente;
- la distribución actual por filtro depende del detalle de sensores y de la identificación de recursos activos;
- el histórico por filtro depende del detalle de sensores;
- la confiabilidad visible depende de la evaluación del modelo;
- la fecha de actualización visible depende del flujo ETL reproducido.

## 18. Supuestos

- existe acceso a las tres fuentes históricas necesarias;
- las llaves de unión entre fuentes pueden homologarse;
- la muestra de trabajo corresponde a 3 meses históricos anonimizados;
- el horizonte con mayor valor operativo es 2h a 4h;
- 6h y 24h forman parte del artefacto, con menor confiabilidad esperada frente a los horizontes cortos;
- el prototipo se valida offline y en entorno controlado.

## 19. Limitaciones

- no se medirá impacto real en operación,
- no se incluye optimización completa,
- no se garantiza despliegue productivo,
- la actualización frecuente del dato se emulará mediante replay o recortes históricos y no mediante una integración en tiempo real.
