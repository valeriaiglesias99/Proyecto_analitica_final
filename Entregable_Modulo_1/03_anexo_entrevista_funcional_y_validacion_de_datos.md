# Anexo: Entrevista Funcional y Validacion de Datos

![Banner del prototipo](assets/Banner_PAAD_01.jpg)

## 1. Proposito

Este anexo documenta una entrevista semiestructurada realizada con un usuario funcional del area operativa y una validacion complementaria sobre el significado y uso de las fuentes de datos del caso. El objetivo es fortalecer la trazabilidad entre:

- problema de negocio,
- requerimientos del prototipo,
- definicion del artefacto,
- y criterios de evaluacion del prototipo.

## 2. Caracteristicas de la entrevista

- Tipo: entrevista semiestructurada.
- Modalidad: conversacion directa con usuario funcional y aclaraciones posteriores sobre datos.
- Enfoque: decisiones operativas, salidas esperadas del artefacto y entendimiento de las fuentes.
- Nivel de anonimato: se omiten nombres propios y referencias explicitas a la organizacion.

## 3. Perfil del usuario entrevistado

- Rol: coordinador de operaciones.
- Perfil: usuario operativo.
- Responsabilidad: monitoreo de flujos, generacion de alertas y apoyo a decisiones sobre habilitacion de recursos en filtros.

## 3.1 Perfiles de usuario derivados del caso

Aunque la entrevista se realizo con un usuario operativo, del caso se desprenden al menos tres perfiles de uso con necesidades diferenciadas:

- coordinador de operaciones:
  requiere anticipacion intradia, alerta por zona y lectura inmediata para habilitacion de filtros;
- analista de control operativo:
  requiere historicos comparables, seguimiento de patrones y detalle por filtro para validacion y analisis posterior;
- responsable tactico o de supervision:
  requiere una vista sintetica del comportamiento agregado, las franjas criticas del dia y la comparacion general frente a historicos.

La priorizacion recae sobre el coordinador de operaciones porque es el perfil asociado a la decision mas sensible al tiempo y al principal dolor identificado: reaccion tardia frente a picos de demanda.

## 4. Bloque 1. Entrevista funcional

### Pregunta 1. Cual es su rol dentro de la operacion?

**Respuesta resumida:** el usuario se desempena como coordinador de operaciones y revisa como se comportan los flujos para alertar sobre congestion y distribuir mejor los recursos en filtros de seguridad.

### Pregunta 2. Que decisiones toma hoy que esta solucion deberia mejorar?

**Respuesta resumida:** decide cuantos filtros habilitar, cuando ampliar capacidad, cuando emitir alertas y como hacer una programacion estimada del comportamiento del dia.

### Pregunta 3. Cual es el principal dolor operativo?

**Respuesta resumida:** no existe suficiente previsibilidad; en algunos momentos la congestion se forma rapidamente y no se detecta con la anticipacion necesaria.

### Pregunta 4. Que pasa si esa decision sale mal?

**Respuesta resumida:** se forman colas, quedan recursos mal utilizados y la operacion proyecta una mala imagen.

### Pregunta 5. Que le gustaria ver con anticipacion?

**Respuesta resumida:** el numero de pasajeros y los picos esperados con algun tipo de referencia operativa, idealmente expresada como criticidad o porcentaje de capacidad.

### Pregunta 6. Cuanto horizonte le aporta valor?

**Respuesta resumida:** el usuario considera utiles varias escalas:

- una vista de corto plazo para las proximas 2 a 4 horas,
- una vista ampliada a 6 horas,
- y una vista de 24 horas o del dia siguiente, entendiendo que la confiabilidad disminuye con el horizonte, pero manteniendo su utilidad como opcion disponible del artefacto.

### Pregunta 7. Sobre que nivel necesita ver el resultado?

**Respuesta resumida:** la alerta principal deberia mostrarse por zona, pero el usuario tambien necesita consultar historicos por filtro. Las predicciones por filtro son utiles si no vuelven demasiado complejo el MVP. Tambien se considera deseable que la interfaz permita ajustar manualmente la cantidad de filtros activos para recalcular la capacidad operativa del escenario consultado.

### Pregunta 8. Que se considera una franja critica?

**Respuesta resumida:** no solo una franja tipicamente cargada; tambien interesa identificar comportamientos atipicos o picos inusuales.

### Pregunta 9. Que accion espera tomar cuando el sistema muestre criticidad?

**Respuesta resumida:** alertar a la operacion, habilitar mas filtros o redistribuir recursos.

### Pregunta 10. Como le gustaria consumir la solucion?

**Respuesta resumida:** mediante un tablero con:

- semaforo de criticidad,
- linea temporal del dia,
- comparacion con historicos,
- y acceso visual inmediato a la informacion.

### Pregunta 11. Que tan importante es entender por que el modelo predice algo?

**Respuesta resumida:** el resultado es mas importante que la explicacion detallada, pero el usuario necesita un nivel visible de confianza o confiabilidad.

### Pregunta 12. Que no puede fallar para que la herramienta sea util?

**Respuesta resumida:** la herramienta debe ser facil de leer, confiable y no exigir un analisis excesivo por parte del usuario operativo.

### Sintesis funcional

De este bloque se concluye que el usuario principal:

- es operativo,
- necesita anticipacion de corto plazo,
- toma decisiones sobre habilitacion de filtros,
- requiere una salida simple y confiable,
- y prioriza alerta por zona sobre detalles tecnicos.

Tambien se concluye que existe un segundo nivel de uso analitico, asociado a la revision de historicos por filtro y a la explicacion posterior de comportamientos atipicos, asi como un nivel agregado de supervision que puede consumir el resultado de forma sintetica.

## 5. Bloque 2. Validacion funcional de datos

### Pregunta 13. Cual es la variable objetivo mas natural para el problema?

**Respuesta resumida:** el objetivo principal es el conteo de personas medido por sensores en filtros.

### Pregunta 14. Cual es la granularidad adecuada para el prototipo?

**Respuesta resumida:** la granularidad objetivo del artefacto es de 15 minutos. Sin embargo, se reconoce que las fuentes operativas de validacion y sensores se registran a una resolucion base de minuto y deben agregarse para construir la lectura operativa del tablero.

### Pregunta 15. Cuales son las fuentes principales del caso?

**Respuesta resumida:** existen tres fuentes operativas principales:

- programacion de vuelos,
- registros de validacion de ingreso al muelle,
- sensores de flujo en filtros.

Adicionalmente, existen tablas auxiliares de apoyo como catalogos de aerolineas.

En la fuente de vuelos, la variable operativa priorizada para el MVP es la de pasajeros programados.

### Pregunta 16. Que representa cada fuente en el proceso operativo?

**Respuesta resumida:**

- la programacion de vuelos representa la senal planificada;
- la validacion de ingreso al muelle representa el momento en que el pasajero cruza el acceso al muelle;
- los sensores capturan el momento en que el flujo pasa por filtros.

Esto define una secuencia funcional clara:

programacion -> ingreso al muelle -> paso por filtros.

### Pregunta 17. Que tan confiables son las fuentes?

**Respuesta resumida:** el usuario indica que la informacion operativa principal es confiable para la solucion propuesta y que tanto la fuente de vuelos como los sensores y los registros de validacion son utiles para modelado. Tambien se establece que, aunque existen horas programadas, estimadas y reales, la referencia prioritaria para este prototipo es la hora programada del vuelo.

### Pregunta 18. Sobre que ambito debe construirse el MVP?

**Respuesta resumida:** el alcance principal debe concentrarse en los 13 filtros de la zona internacional objetivo.

### Pregunta 19. Que otras variables podrian aportar contexto?

**Respuesta resumida:** los tiempos de proceso no suelen variar mucho, por lo que no son indispensables para el modelo base. Sin embargo, podrian ser utiles como senal complementaria de anomalia operativa cuando se desvien de su comportamiento usual.

### Pregunta 20. Que historico es razonable usar para el prototipo?

**Respuesta resumida:** se considera razonable trabajar con 3 meses de informacion historica anonimizados, manteniendo la posibilidad de mostrar el historico y simular cortes del dia actual.

### Pregunta 20.1. Como debe entenderse la capacidad operativa?

**Respuesta resumida:** la capacidad debe calcularse a partir del numero de filtros activos y del tiempo promedio de proceso por pasajero. Para este caso se dispone de una referencia de 23 segundos por persona y se espera que la interfaz permita ajustar manualmente la cantidad de filtros activos para recalcular la capacidad del escenario consultado. El calculo base puede formularse a nivel de minuto y agregarse despues a la franja operativa de 15 minutos.

### Pregunta 20.2. Como deben interpretarse las franjas de alerta?

**Respuesta resumida:** la lectura de criticidad debe apoyarse en umbrales operativos sobre la ocupacion estimada de la capacidad. Como referencia inicial, se consideran alertas desde 70% y condiciones criticas desde 85% de ocupacion.

### Pregunta 21. Hay restricciones fuertes de confidencialidad?

**Respuesta resumida:** no se identifican campos sensibles indispensables para el MVP, pero se solicita no mencionar explicitamente el nombre de la organizacion y trabajar el caso como un aeropuerto internacional de referencia.

### Sintesis de datos

De este bloque se concluye que:

- el target principal es el flujo medido en filtros;
- la granularidad adecuada del artefacto es 15 minutos, aunque parte de las fuentes se registren a minuto;
- la alerta principal debe agregarse por zona;
- el detalle por filtro queda como analitica complementaria;
- la cadena temporal entre fuentes debe reflejarse en el diseno del modelo y en la ingenieria de variables;
- la capacidad operativa debe depender del numero de filtros activos y del tiempo promedio de proceso;
- la hora programada del vuelo es la referencia temporal prioritaria para el modelado base.

## 6. Implicaciones para el prototipo

Las decisiones de diseno derivadas de la entrevista son:

- usuario principal operativo, no estrategico;
- vista principal orientada a semaforo por zona;
- separacion entre una vista `Ahora` para seguimiento intradia y una vista `Historico` para comparacion retrospectiva;
- historico por filtro como apoyo de analisis;
- distribucion actual del flujo por filtro como soporte puntual de la decision operativa;
- prediccion por filtro como deseable, no como obligatoria en el MVP;
- granularidad de 15 minutos;
- horizontes 2h y 4h como prioridad, 6h y 24h como opcion disponible con mayor incertidumbre esperada;
- ajuste manual de filtros activos como parametro del escenario operativo;
- referencia de capacidad visible como apoyo para interpretar criticidad;
- ocupacion expresada tanto en volumen como en porcentaje;
- necesidad de mostrar confiabilidad visible junto con la prediccion;
- uso de las tres fuentes en secuencia funcional para el diseno del dataset maestro.

## 7. Conclusiones del levantamiento funcional y de datos

El levantamiento realizado permite consolidar los siguientes elementos para el diseno del prototipo:

- el usuario principal es operativo y requiere una visualizacion simple, directa y confiable;
- la necesidad funcional central es anticipar condiciones de congestion para apoyar la habilitacion de filtros y la redistribucion de recursos;
- la salida principal del artefacto debe ser una alerta agregada por zona, complementada con una vista operativa actual y una vista historica de comparacion;
- el detalle por filtro debe existir en dos niveles: distribucion actual del flujo para la lectura intradia y consulta historica para el analisis retrospectivo;
- la granularidad de analisis adecuada para el MVP es de 15 minutos;
- los horizontes de mayor valor operativo son 2h y 4h, mientras que 6h y 24h deben mantenerse disponibles con una lectura explicita de mayor incertidumbre;
- el target principal debe construirse con el flujo observado en filtros, usando como soporte la secuencia entre programacion de vuelos, ingreso al muelle y paso por filtros;
- la capacidad operativa debe calcularse con base en filtros activos y tiempo promedio de proceso;
- el alcance del prototipo debe concentrarse en los 13 filtros de la zona internacional objetivo, manteniendo el detalle por filtro como analitica complementaria.
