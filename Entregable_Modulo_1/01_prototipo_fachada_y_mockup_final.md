# Prototipo Fachada y Mockup Final

![Banner del prototipo](assets/Banner_PAAD_01.jpg)

## 1. Nombre del artefacto

Tablero predictivo para planeacion tactica de demanda en filtros de una zona internacional de control.

## 2. Usuario final y necesidad

### Perfiles de usuario identificados

| Perfil | Rol dentro del caso | Necesidad principal | Salida esperada | Prioridad |
|---|---|---|---|---|
| Coordinador de operaciones | Monitorea flujos intradia y decide habilitacion de filtros y redistribucion de recursos | Anticipar picos de demanda con suficiente tiempo para actuar | Semaforo por zona, linea temporal, franjas criticas y nivel de confianza visible | Alta |
| Analista de control operativo | Revisa historicos, valida comportamientos atipicos y analiza patrones por recurso | Entender comportamiento pasado, contrastar dias comparables y revisar detalle por filtro | Historicos comparables, trazabilidad temporal y analitica complementaria por filtro | Media |
| Responsable tactico o de supervision | Revisa desempeno general, necesidades de capacidad y comportamiento agregado de la operacion | Contar con una vista sintetica del comportamiento esperado y observado para seguimiento operativo | Resumen agregado por zona, franjas criticas del dia y comparacion general contra historico | Media-baja |

### Usuario priorizado

El usuario principal priorizado es el coordinador de operaciones encargado de monitorear flujos, emitir alertas y decidir la habilitacion de recursos en filtros durante el dia.

### Sustento de la priorizacion

La priorizacion se soporta en el anexo [03_anexo_entrevista_funcional_y_validacion_de_datos.md](03_anexo_entrevista_funcional_y_validacion_de_datos.md) y en la naturaleza operativa del caso:

- en la entrevista, el usuario consultado se identifica como coordinador de operaciones y declara que sus decisiones centrales son habilitar filtros, alertar congestion y redistribuir recursos;
- el horizonte de mayor valor declarado es de 2h a 4h, lo cual corresponde a decisiones intradia y no a seguimiento directivo de largo plazo;
- la granularidad requerida de 15 minutos y la necesidad de una alerta por zona evidencian un uso operativo de alta frecuencia;
- el requerimiento de acceso visual simple y sin codigo confirma que la primera capa del artefacto debe responder a un usuario de accion rapida;
- la necesidad de revisar historicos por filtro sugiere un segundo perfil analitico, orientado a validacion y seguimiento;
- la lectura agregada por zona tambien puede ser consumida por un perfil de supervision, pero no es el usuario critico para definir el MVP, dado que el valor diferencial del artefacto se concentra en la anticipacion operativa.

### Necesidad a resolver

La operacion hoy reacciona tarde a cambios de demanda. El usuario necesita anticipar el flujo de pasajeros con granularidad de 15 minutos para tomar decisiones tacticas sobre habilitacion de filtros y distribucion de recursos, con especial foco en horizontes cortos del mismo dia. Aunque algunas fuentes operativas se registran a nivel de minuto, el artefacto consolida la lectura y la prediccion en franjas de 15 minutos para reducir ruido y facilitar decisiones operativas.

## 3. Problema de negocio

Como anticipar, con granularidad de 15 minutos y horizontes operativos de 2, 4, 6 y hasta 24 horas, las franjas con mayor flujo esperado en filtros de la zona internacional objetivo para apoyar decisiones de habilitacion y distribucion de recursos.

## 4. Modelo logico de impacto

### Input

- programacion de vuelos,
- registros de validacion de ingreso al muelle,
- sensores de paso por filtros,
- variables calendario y catalogos auxiliares.

### Output

- pronostico por franja de 15 minutos,
- semaforo de criticidad por zona,
- vista operativa `Ahora` para seguimiento intradia,
- vista `Historico` para comparacion retrospectiva,
- historico comparable,
- detalle historico por filtro,
- distribucion actual del flujo por filtro y recurso con mayor carga,
- capacidad de referencia visible en la lectura principal, en unidades absolutas y relativas,
- porcentaje de ocupacion estimada respecto a la capacidad disponible,
- nivel visible de confianza o calidad de la prediccion.

### Outcome esperado

- mejor anticipacion de franjas criticas,
- menor reaccion tardia ante congestion,
- mejor habilitacion tactica de filtros.

## 5. KPIs y metrica de impacto esperada

En esta fase se priorizan indicadores proxy evaluables offline:

- capacidad de identificar franjas criticas,
- mejora frente a baseline historico simple,
- cobertura de las franjas y horizontes utiles para planeacion,
- confiabilidad visible de la alerta para el usuario.

## 6. Alcance del MVP

### Must

- integracion de tres fuentes prioritarias,
- prediccion cada 15 minutos,
- alerta principal por zona,
- doble vista global `Ahora / Historico`,
- parametro manual para definir cantidad de filtros activos,
- historicos por filtro,
- comparacion contra baseline,
- horizontes de 2h, 4h, 6h y 24h,
- muestra anonimizada o controlada para visualizacion.

### Should

- indicador visible de confianza,
- prediccion por filtro cuando el recurso tenga estabilidad suficiente.

### Could

- recomendacion simple basada en reglas,
- tiempos de proceso como senal de anomalia operacional.

### Fuera de alcance

- optimizacion completa de dotaciones,
- despliegue productivo,
- medicion real de ahorros,
- adopcion real en operacion,
- integracion corporativa completa.

## 7. Forma de uso esperada

El usuario accede a un tablero de consulta sin codigo y puede:

- elegir la vista general del informe entre `Ahora` y `Historico`,
- seleccionar fecha, zona y granularidad de lectura,
- definir manualmente la cantidad de filtros activos para el corte o escenario consultado,
- escoger horizonte de consulta cuando se encuentre en la vista `Ahora`,
- escoger rango de comparacion cuando se encuentre en la vista `Historico`,
- revisar el estado de criticidad de la zona y su contraste contra capacidad de referencia,
- revisar la ocupacion estimada frente a la capacidad disponible en numero de pasajeros y porcentaje,
- comparar pronostico contra historico comparable,
- consultar distribucion actual del flujo por filtro o analitica historica por filtro segun la vista elegida,
- revisar el nivel de confianza visible.

## 8. Flujo de interaccion del usuario

1. El coordinador ingresa a la interfaz al inicio de la jornada o durante la operacion intradia.
2. Define la vista general del informe segun la necesidad del momento: `Ahora` para seguimiento operativo o `Historico` para analisis retrospectivo.
3. Si se encuentra en `Ahora`, selecciona fecha, horizonte operativo y cantidad de filtros activos; si se encuentra en `Historico`, selecciona la fecha analizada y el rango de comparacion.
4. Revisa la vista principal de zona para identificar rapidamente el nivel de criticidad esperado, su relacion con la capacidad de referencia y el porcentaje de ocupacion estimado.
5. Contrasta la demanda estimada u observada con el historico comparable para determinar si el comportamiento es normal, de alerta o atipico.
6. Consulta la tabla de franjas priorizadas para ubicar los periodos en los que podria requerirse habilitacion adicional de filtros.
7. Navega al detalle por filtro: en `Ahora` revisa distribucion actual del flujo y recurso con mayor carga; en `Historico` revisa comportamiento pasado por fecha y comparativo.
8. Con base en la lectura agregada y el detalle complementario, decide habilitar filtros, redistribuir recursos o mantener la configuracion actual.
9. En cortes posteriores del dia, repite la consulta para actualizar la lectura operativa y verificar si la criticidad prevista se mantiene, aumenta o disminuye.

### Salidas que consume cada perfil

- coordinador de operaciones:
  semaforo por zona, franjas criticas, linea temporal y nivel visible de confianza;
- analista de control operativo:
  historicos comparables, detalle por filtro y trazabilidad del comportamiento observado;
- responsable tactico o de supervision:
  resumen agregado, comparacion general contra historico y lectura sintetica del estado esperado de la operacion.

## 9. Decisiones de diseño justificadas

### El tablero es la forma de uso principal del artefacto

- el caso requiere lectura rapida de multiples elementos al mismo tiempo: criticidad, linea temporal, comparacion historica y detalle por filtro;
- la consulta principal se realiza en un contexto de monitoreo operativo donde una vista consolidada tiene mayor valor que una interaccion movil reducida;
- un tablero facilita comparacion visual, jerarquia de alertas y navegacion entre zona y filtro sin aumentar complejidad de desarrollo;
- una aplicacion movil puede ser una extension futura, pero no es la forma prioritaria para el MVP dado el tipo de decision y el entorno de uso esperado.

### La interfaz de consulta tiene prioridad sobre una API como producto visible

- la necesidad del usuario no es consumir un servicio tecnico aislado, sino interpretar rapidamente una situacion operativa;
- la salida requiere semaforos, historicos comparables y una lectura visual de franjas criticas, elementos que una API por si sola no resuelve para el usuario final;
- una API podria existir como componente tecnico interno, pero la forma de uso principal del artefacto debe ser una interfaz de consulta.

### La actualizacion por cortes es suficiente para el valor operativo buscado

- el valor principal de la solucion esta en anticipar ventanas de 2h a 4h para apoyar decisiones tacticas, no en reaccionar a eventos de segundos;
- la granularidad operativa definida es de 15 minutos, lo cual hace viable una logica de actualizacion por cortes temporales sin perder utilidad funcional;
- una arquitectura de streaming completo incrementaria complejidad de integracion, monitoreo y validacion sin ser indispensable para demostrar utilidad del artefacto en esta fase;
- por tanto, la solucion se plantea con procesamiento reproducible por ventanas de tiempo y posibilidad de evolucionar hacia una mayor frecuencia de actualizacion.

### La alerta principal se concentra a nivel zona

- la decision primaria del usuario se toma a nivel zona, donde se evalua la necesidad de habilitar recursos adicionales;
- el comportamiento por filtro es valioso como analitica complementaria, pero no siempre todos los filtros estan habilitados ni tienen estabilidad suficiente para soportar una alerta principal independiente;
- priorizar la zona mejora robustez del MVP y deja el detalle por filtro como segunda capa de analisis.

### La capacidad operativa se controla con un parametro manual de filtros activos

- la operacion requiere evaluar escenarios con diferente cantidad de filtros habilitados durante el dia;
- permitir al usuario ajustar manualmente el numero de filtros activos mantiene el artefacto conectado con la decision operativa real sin exigir una capa prescriptiva completa;
- este parametro modifica la capacidad disponible y, por tanto, la lectura de ocupacion y criticidad;
- la definicion manual del numero de filtros activos es suficientemente simple para el MVP y evita comprometer una programacion operativa completa de recursos.

### La separacion entre `Ahora` e `Historico` mejora la lectura del artefacto

- el usuario operativo necesita una lectura rapida de corto plazo, mientras que el perfil analitico necesita explorar comparativos retrospectivos sin contaminar la vista principal de monitoreo;
- mantener ambos usos en una sola pantalla sin separacion contextual aumenta carga cognitiva y dificulta la interpretacion inmediata;
- la vista `Ahora` prioriza horizonte, criticidad, capacidad de referencia y concentracion actual por filtro;
- la vista `Historico` prioriza fecha analizada, rango de comparacion, comportamiento observado y patrones repetitivos;
- esta separacion conserva coherencia funcional entre perfiles y evita duplicar productos distintos para una misma necesidad.

### Los controles cambian segun la vista seleccionada para reducir ambiguedad

- en `Ahora` el usuario necesita elegir horizonte de anticipacion, porque la pregunta es que pasara en las proximas horas;
- en `Historico` el usuario necesita elegir rango de comparacion, porque la pregunta es como se comporto una fecha frente a periodos comparables;
- cambiar los controles junto con la vista reduce ambiguedad y hace que cada modo del tablero responda a una tarea concreta.

## 10. Funcionalidades esperadas

- consulta sin codigo,
- selector global de vista `Ahora / Historico`,
- visualizacion de pronostico cada 15 minutos,
- visualizacion del volumen proyectado en personas,
- linea de capacidad de referencia en la grafica principal,
- visualizacion de ocupacion estimada en porcentaje respecto a capacidad,
- tabla de franjas priorizadas,
- semaforo por zona,
- ajuste manual del numero de filtros activos,
- distribucion actual por filtro en la vista `Ahora`,
- analitica historica por filtro en la vista `Historico`,
- identificacion del filtro con mayor carga en la lectura actual,
- trazabilidad minima del dato y de la fecha de actualizacion disponible.

## 11. Tipos de analisis y modelos

### Baselines

- naive por ultima observacion,
- promedio historico por franja.

### Pregunta analitica 1. Como anticipar el flujo agregado por zona en intervalos de 15 minutos?

**Alternativa 1: modelos de series de tiempo con variables exogenas**

- ejemplos: regresion dinamica, SARIMAX, Prophet o modelos equivalentes con componentes temporales;
- se consideran porque la variable objetivo tiene estructura temporal clara, estacionalidad intradia y dependencia secuencial;
- permiten incorporar senales externas como programacion de vuelos y conteos de ingreso al muelle sin perder interpretabilidad;
- son especialmente pertinentes para horizontes cortos, donde la dinamica reciente del flujo tiene alto valor predictivo.

**Alternativa 2: modelos de regresion supervisada basados en arboles**

- ejemplos: Random Forest, XGBoost, LightGBM o equivalentes;
- se consideran porque el problema combina lags temporales, variables calendario, vuelos programados y senales operativas recientes;
- pueden capturar interacciones no lineales entre la demanda observada en filtros, el ingreso al muelle y la programacion;
- resultan adecuados cuando se espera que la relacion entre entradas y salida no sea estrictamente lineal ni puramente estacional.

**Justificacion comparativa**

- los modelos de series de tiempo priorizan trazabilidad e interpretacion del comportamiento intradia;
- los modelos de arboles priorizan flexibilidad predictiva y capacidad para capturar relaciones complejas entre fuentes heterogeneas;
- ambos deben compararse contra baselines simples para verificar que exista ganancia real de desempeno.

### Pregunta analitica 2. Como identificar franjas criticas para la emision de alertas operativas?

**Alternativa 1: clasificacion derivada del pronostico**

- consiste en transformar el pronostico continuo en niveles de criticidad mediante umbrales, percentiles historicos o capacidad operativa de referencia;
- se considera porque conserva coherencia con la necesidad funcional principal: convertir una prediccion de flujo en una alerta interpretable;
- facilita justificar cada alerta a partir de una variable continua y de reglas de negocio transparentes.

**Alternativa 2: modelo de clasificacion directa**

- ejemplos: clasificacion binaria o multiclase para estimar si una franja sera normal, de alerta o critica;
- se considera porque la salida operativa final es una decision categorica y no solo un valor numerico;
- permite optimizar metricas orientadas a deteccion de eventos criticos, como recall y F1, aun cuando el error promedio de regresion no capture del todo el costo operativo de perder un pico.

**Justificacion comparativa**

- el enfoque derivado del pronostico es mas trazable y mantiene una sola cadena analitica principal;
- la clasificacion directa puede ser mas util si el objetivo operacional privilegia no omitir franjas criticas por encima de la precision puntual;
- ambos enfoques son validos y deben contrastarse segun estabilidad de las etiquetas de criticidad y facilidad de adopcion por el usuario.

### Pregunta analitica 3. Como representar el comportamiento por filtro individual sin perder viabilidad?

**Alternativa 1: desagregacion desde el pronostico de zona**

- consiste en proyectar el total por zona y distribuirlo por filtro a partir de participaciones historicas, reglas operativas o perfiles de uso;
- se considera porque reduce complejidad, requiere menos datos por unidad y mantiene estable el MVP;
- es apropiada cuando no todos los filtros estan siempre habilitados o cuando existe alta variabilidad en la activacion individual.

**Alternativa 2: modelos independientes por filtro**

- consiste en entrenar modelos separados para filtros con suficiente actividad y estabilidad;
- se considera porque puede capturar diferencias reales de comportamiento entre recursos y mejorar el detalle analitico;
- es pertinente solo si existe volumen suficiente por filtro y una trazabilidad consistente de aperturas, cierres y uso.

**Justificacion comparativa**

- la desagregacion top-down es mas simple y robusta para una primera implementacion;
- los modelos por filtro ofrecen mayor granularidad, pero exigen mejor calidad de datos y una definicion clara de recursos activos e inactivos;
- por esta razon, el detalle predictivo por filtro se mantiene como capacidad deseable y no como requisito central del MVP.

### Criterio general de seleccion

- el baseline sirve como referencia operacional minima;
- las series de tiempo con exogenas aportan interpretabilidad y buen ajuste a la naturaleza secuencial del problema;
- la regresion supervisada aporta capacidad para capturar no linealidades e interacciones entre multiples fuentes;
- la clasificacion de criticidad permite alinear la salida con la decision operativa final;
- la desagregacion o modelado por filtro se evalua segun estabilidad y cobertura real de los recursos.

La optimizacion se deja fuera del MVP porque incrementa complejidad y no es necesaria para demostrar viabilidad analitica del prototipo.

## 12. Fuentes de datos y mini diccionario

| Fuente | Granularidad | Variable clave | Mecanismo de acceso previsto | Uso principal |
|---|---|---|---|---|
| Programacion de vuelos | vuelo / tiempo programado | hora programada, destino, aerolinea, pasajeros programados | extraccion desde tablas SQL Server integradas al entorno corporativo o desde exportaciones controladas derivadas de una capa refinada de esa arquitectura | senal planificada |
| Validacion de ingreso al muelle | evento individual / registro base a minuto, agregable a 15 min | timestamp de paso, vuelo, aerolinea | consulta a registros operativos anonimizados, provenientes de tablas SQL Server o vistas consolidadas del entorno analitico | senal operativa intermedia |
| Sensores de filtros | conteo por recurso / registro base a minuto, agregable a 15 min | timestamp, filtro, conteo | extraccion desde historicos de sensores consolidados en el entorno analitico o desde repositorios derivados de SQL Server | variable objetivo y validacion de flujo real |
| Catalogos auxiliares | dimension | aerolinea, operador, recurso | tablas maestras o dimensiones corporativas | homologacion y enriquecimiento |

## 13. Acceso, ETL y data lineage

### Flujo general

1. Extraccion de fuentes historicas desde una capa refinada del entorno corporativo.
2. Paso por arquitectura medallion o capa analitica equivalente en el entorno fuente.
3. Homologacion temporal y limpieza.
4. Filtrado a la zona objetivo.
5. Agregacion desde resolucion base a minuto hacia franjas de 15 minutos.
6. Construccion de lags y variables calendario.
7. Consolidacion del dataset maestro.
8. Entrenamiento, evaluacion y scoring.
9. Publicacion de salida para tablero de consulta.

### Contexto de arquitectura de datos

Las fuentes operativas del caso residen en bases de datos SQL Server y, en el entorno corporativo, su integracion analitica se soporta sobre una arquitectura medallion o una capa equivalente de refinamiento progresivo del dato. Para este prototipo no se plantea una conexion productiva directa a esa arquitectura completa; por consideraciones de confidencialidad y alcance, la solucion se construye sobre una muestra controlada y anonimizada, derivada de una capa refinada de dichas fuentes y suficiente para reproducir el flujo analitico del MVP.

### Regla de capacidad operativa

La capacidad de referencia de la zona se calcula a partir del numero de filtros activos definido manualmente por el usuario y del tiempo promedio de proceso por pasajero. En esta version del prototipo se toma como referencia un tiempo promedio de 23 segundos por persona. El calculo base se formula a nivel de minuto y luego se agrega a la franja operativa de 15 minutos, de modo consistente con la resolucion del tablero. La capacidad estimada se expresa tanto en numero de pasajeros como en porcentaje de ocupacion sobre dicha capacidad, de modo que el tablero pueda clasificar las franjas en condiciones normales, de alerta y criticas.

De manera inicial, la lectura de criticidad se plantea con estos umbrales:

- alerta desde 70% de ocupacion estimada;
- criticidad desde 85% de ocupacion estimada.

### Desarrollos requeridos para acceso y procesamiento

- identificacion de la capa fuente y de la capa refinada desde la cual se extraera la muestra de trabajo;
- homologacion de llaves temporales entre las tres fuentes principales;
- definicion de reglas de filtrado para la zona objetivo;
- agregacion y consolidacion de eventos desde resolucion base a minuto hacia una granularidad de 15 minutos;
- construccion de variables derivadas y lags para representar anticipacion operativa;
- incorporacion del parametro de filtros activos en la capa de salida para recalcular capacidad y ocupacion;
- preparacion de salidas consumibles por la interfaz de consulta.

### Riesgos de calidad y mitigacion

- desalineacion temporal entre fuentes:
  mitigacion: homologacion horaria y reglas de ventana comun;
- recursos con comportamiento inestable:
  mitigacion: exclusion o agrupacion justificada;
- datos sensibles:
  mitigacion: uso de muestra anonimizada en repositorio y entorno de visualizacion.

## 14. Diagrama esquematico del artefacto

La Figura 1 presenta el prototipo fachada del artefacto, integrando usuario, requerimientos, forma de uso, modelos, datos y procesos de ETL.

![Figura 1. Prototipo fachada del artefacto](<Diagrama 1.png>)

### Nota de alcance del diagrama

El diagrama representa la logica funcional del MVP. No implica despliegue productivo ni integracion completa con la arquitectura corporativa.

## 15. Arquitectura prevista

Adicionalmente al diagrama esquematico del artefacto, se plantea una arquitectura simplificada de la POC para representar la implementacion minima de la solucion:

La Figura 2 muestra la arquitectura prevista de la solucion, desde las fuentes historicas hasta la capa de consumo del resultado.

![Figura 2. Arquitectura prevista de la solucion](<Diagrama 2.png>)

Esta arquitectura complementa el prototipo fachada y permite visualizar la ruta minima desde las fuentes hasta el consumo del resultado, sin representar la arquitectura corporativa completa.

## 16. Representacion visual de la interfaz

La representacion visual de la interfaz se incluye en:

- [mockup_prototipo.html](assets/mockup_prototipo.html)

Esta representacion incluye:

- vista global `Ahora` para seguimiento operativo,
- vista global `Historico` para comparacion retrospectiva,
- semaforo por zona,
- linea temporal de demanda,
- capacidad de referencia,
- porcentaje de ocupacion respecto a capacidad,
- volumen proyectado en personas,
- parametro manual de filtros activos,
- distribucion actual por filtro,
- reporte historico por filtro,
- cambio de controles segun la vista seleccionada.

## 17. Coherencia back-end / front-end

- la alerta por zona depende del motor de scoring y la clasificacion de criticidad;
- la vista `Ahora` depende del motor de pronostico, de la clasificacion de criticidad y de la disponibilidad de los ultimos cortes de datos;
- la vista `Historico` depende del historico consolidado y de la logica de comparacion por fecha o ventana equivalente;
- la distribucion actual por filtro depende del detalle de sensores y de la identificacion de recursos activos;
- el historico por filtro depende del detalle de sensores;
- la confiabilidad visible depende de la evaluacion del modelo;
- la fecha de actualizacion visible depende del flujo ETL reproducido.

## 18. Supuestos

- existe acceso a las tres fuentes historicas necesarias;
- las llaves de union entre fuentes pueden homologarse;
- la muestra de trabajo corresponde a 3 meses historicos anonimizados;
- el horizonte con mayor valor operativo es 2h a 4h;
- 6h y 24h forman parte del artefacto, con menor confiabilidad esperada frente a los horizontes cortos;
- el prototipo se valida offline y en entorno controlado.

## 19. Limitaciones

- no se medira impacto real en operacion,
- no se incluye optimizacion completa,
- no se garantiza despliegue productivo,
- la actualizacion frecuente del dato se emulara mediante replay o recortes historicos y no mediante una integracion en tiempo real.
