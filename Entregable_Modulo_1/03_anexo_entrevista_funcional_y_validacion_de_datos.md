# Anexo: Entrevista Funcional y Validacion de Datos

![Banner del prototipo](assets/Banner_PAAD_01.jpg)

## 1. Propósito

Este anexo documenta una entrevista semiestructurada realizada con un usuario funcional del área operativa y una validación complementaria sobre el significado y uso de las fuentes de datos del caso. El objetivo es fortalecer la trazabilidad entre:

- problema de negocio,
- requerimientos del prototipo,
- definición del artefacto,
- y criterios de evaluación del prototipo.

## 2. Características de la entrevista

- Tipo: entrevista semiestructurada.
- Modalidad: conversación directa con usuario funcional y aclaraciones posteriores sobre datos.
- Enfoque: decisiones operativas, salidas esperadas del artefacto y entendimiento de las fuentes.
- Nivel de anonimato: se omiten nombres propios y referencias explicitas a la organización.

## 3. Perfil del usuario entrevistado

- Rol: coordinador de operaciones.
- Perfil: usuario operativo.
- Responsabilidad: monitoreo de flujos, generacion de alertas y apoyo a decisiones sobre habilitación de recursos en filtros.

## 3.1 Perfiles de usuario derivados del caso

Aunque la entrevista se realizó con un usuario operativo, del caso se desprenden al menos tres perfiles de uso con necesidades diferenciadas:

- coordinador de operaciones:
  requiere anticipación intradía, alerta por zona y lectura inmediata para habilitacion de filtros;
- analista de control operativo:
  requiere historicos comparables, seguimiento de patrones y detalle por filtro para validación y análisis posterior;
- responsable tactico o de supervisión:
  requiere una vista sintética del comportamiento agregado, las franjas críticas del día y la comparación general frente a históricos.

La priorización recae sobre el coordinador de operaciones porque es el perfil asociado a la decisión más sensible al tiempo y al principal dolor identificado: reaccion tardía frente a picos de demanda.

## 4. Bloque 1. Entrevista funcional

### Pregunta 1. Cuál es su rol dentro de la operacion?

**Respuesta resumida:** el usuario se desempeña como coordinador de operaciones y revisa como se comportan los flujos para alertar sobre congestión y distribuir mejor los recursos en filtros de seguridad.

### Pregunta 2. Qué decisiones toma hoy que esta solución deberia mejorar?

**Respuesta resumida:** decide cuantos filtros habilitar, cuando ampliar capacidad, cuando emitir alertas y como hacer una programación estimada del comportamiento del día.

### Pregunta 3. Cuál es el principal dolor operativo?

**Respuesta resumida:** no existe suficiente previsibilidad; en algunos momentos la congestón se forma rapidamente y no se detecta con la anticipación necesaria.

### Pregunta 4. Qué pasa si esa decisión sale mal?

**Respuesta resumida:** se forman colas, quedan recursos mal utilizados y la operacion proyecta una mala imagen.

### Pregunta 5. Qué le gustaría ver con anticipación?

**Respuesta resumida:** el número de pasajeros y los picos esperados con algun tipo de referencia operativa, idealmente expresada como criticidad o porcentaje de capacidad.

### Pregunta 6. Cuánto horizonte le aporta valor?

**Respuesta resumida:** el usuario considera útiles varias escalas:

- una vista de corto plazo para las próximas 2 a 4 horas,
- una vista ampliada a 6 horas,
- y una vista de 24 horas o del día siguiente, entendiendo que la confiabilidad disminuye con el horizonte, pero manteniendo su utilidad como opción disponible del artefacto.

### Pregunta 7. Sobre qué nivel necesita ver el resultado?

**Respuesta resumida:** la alerta principal debería mostrarse por zona, pero el usuario tambien necesita consultar históricos por filtro. Las predicciones por filtro son útiles si no vuelven demasiado complejo el MVP. Tambien se considera deseable que la interfaz permita ajustar manualmente la cantidad de filtros activos para recalcular la capacidad operativa del escenario consultado.

### Pregunta 8. Qué se considera una franja crítica?

**Respuesta resumida:** no solo una franja tipicamente cargada; tambien interesa identificar comportamientos atípicos o picos inusuales.

### Pregunta 9. Qué accion espera tomar cuando el sistema muestre criticidad?

**Respuesta resumida:** alertar a la operación, habilitar mas filtros o redistribuir recursos.

### Pregunta 10. Como le gustaría consumir la solución?

**Respuesta resumida:** mediante un tablero con:

- semáforo de criticidad,
- línea temporal del día,
- comparación con históricos,
- y acceso visual inmediato a la informacion.

### Pregunta 11. Qué tan importante es entender por que el modelo predice algo?

**Respuesta resumida:** el resultado es mas importante que la explicación detallada, pero el usuario necesita un nivel visible de confianza o confiabilidad.

### Pregunta 12. Qué no puede fallar para que la herramienta sea útil?

**Respuesta resumida:** la herramienta debe ser fácil de leer, confiable y no exigir un analisis excesivo por parte del usuario operativo.

### Síntesis funcional

De este bloque se concluye que el usuario principal:

- es operativo,
- necesita anticipación de corto plazo,
- toma decisiones sobre habilitación de filtros,
- requiere una salida simple y confiable,
- y prioriza alerta por zona sobre detalles técnicos.

También se concluye que existe un segundo nivel de uso analítico, asociado a la revisión de históricos por filtro y a la explicación posterior de comportamientos atípicos, asi como un nivel agregado de supervisión que puede consumir el resultado de forma sintética.

## 5. Bloque 2. Validación funcional de datos

### Pregunta 13. Cuál es la variable objetivo más natural para el problema?

**Respuesta resumida:** el objetivo principal es el conteo de personas medido por sensores en filtros.

### Pregunta 14. Cuál es la granularidad adecuada para el prototipo?

**Respuesta resumida:** la granularidad objetivo del artefacto es de 15 minutos. Sin embargo, se reconoce que las fuentes operativas de validación y sensores se registran a una resolución base de minuto y deben agregarse para construir la lectura operativa del tablero.

### Pregunta 15. Cuáles son las fuentes principales del caso?

**Respuesta resumida:** existen tres fuentes operativas principales:

- programación de vuelos,
- registros de validacion de ingreso al muelle,
- sensores de flujo en filtros.

Adicionalmente, existen tablas auxiliares de apoyo como catalogos de aerol´´ineas.

En la fuente de vuelos, la variable operativa priorizada para el MVP es la de pasajeros programados.

### Pregunta 16. Qué representa cada fuente en el proceso operativo?

**Respuesta resumida:**

- la programación de vuelos representa la senal planificada;
- la validación de ingreso al muelle representa el momento en que el pasajero cruza el acceso al muelle;
- los sensores capturan el momento en que el flujo pasa por filtros.

Esto define una secuencia funcional clara:

programación -> ingreso al muelle -> paso por filtros.

### Pregunta 17. Qué tan confiables son las fuentes?

**Respuesta resumida:** el usuario indica que la información operativa principal es confiable para la solución propuesta y que tanto la fuente de vuelos como los sensores y los registros de validación son utiles para modelado. También se establece que, aunque existen horas programadas, estimadas y reales, la referencia prioritaria para este prototipo es la hora programada del vuelo.

### Pregunta 18. Sobre que ámbito debe construirse el MVP?

**Respuesta resumida:** el alcance principal debe concentrarse en los 13 filtros de la zona internacional objetivo.

### Pregunta 19. Qué otras variables podrían aportar contexto?

**Respuesta resumida:** los tiempos de proceso no suelen variar mucho, por lo que no son indispensables para el modelo base. Sin embargo, podrían ser útiles como señal complementaria de anomalía operativa cuando se desvien de su comportamiento usual.

### Pregunta 20. Qué histórico es razonable usar para el prototipo?

**Respuesta resumida:** se considera razonable trabajar con 3 meses de información histórica anonimizados, manteniendo la posibilidad de mostrar el histórico y simular cortes del día actual.

### Pregunta 20.1. Cómo debe entenderse la capacidad operativa?

**Respuesta resumida:** la capacidad debe calcularse a partir del numero de filtros activos y del tiempo promedio de proceso por pasajero. Para este caso se dispone de una referencia de 23 segundos por persona y se espera que la interfaz permita ajustar manualmente la cantidad de filtros activos para recalcular la capacidad del escenario consultado. El calculo base puede formularse a nivel de minuto y agregarse despues a la franja operativa de 15 minutos.

### Pregunta 20.2. Cómo deben interpretarse las franjas de alerta?

**Respuesta resumida:** la lectura de criticidad debe apoyarse en umbrales operativos sobre la ocupación estimada de la capacidad. Como referencia inicial, se consideran alertas desde 70% y condiciones críticas desde 85% de ocupación.

### Pregunta 21. Hay restricciones fuertes de confidencialidad?

**Respuesta resumida:** no se identifican campos sensibles indispensables para el MVP, pero se solicita no mencionar explícitamente el nombre de la organización y trabajar el caso como un aeropuerto internacional de referencia.

### Síntesis de datos

De este bloque se concluye que:

- el target principal es el flujo medido en filtros;
- la granularidad adecuada del artefacto es 15 minutos, aunque parte de las fuentes se registren a minuto;
- la alerta principal debe agregarse por zona;
- el detalle por filtro queda como analítica complementaria;
- la cadena temporal entre fuentes debe reflejarse en el diseño del modelo y en la ingeniería de variables;
- la capacidad operativa debe depender del numero de filtros activos y del tiempo promedio de proceso;
- la hora programada del vuelo es la referencia temporal prioritaria para el modelado base.

## 6. Implicaciones para el prototipo

Las decisiones de diseño derivadas de la entrevista son:

- usuario principal operativo, no estratégico;
- vista principal orientada a semáforo por zona;
- separación entre una vista `Ahora` para seguimiento intradia y una vista `Histórico` para comparación retrospectiva;
- histórico por filtro como apoyo de análisis;
- distribución actual del flujo por filtro como soporte puntual de la decisión operativa;
- predicción por filtro como deseable, no como obligatoria en el MVP;
- granularidad de 15 minutos;
- horizontes 2h y 4h como prioridad, 6h y 24h como opción disponible con mayor incertidumbre esperada;
- ajuste manual de filtros activos como parámetro del escenario operativo;
- referencia de capacidad visible como apoyo para interpretar criticidad;
- ocupación expresada tanto en volúmen como en porcentaje;
- necesidad de mostrar confiabilidad visible junto con la predicción;
- uso de las tres fuentes en secuencia funcional para el diseño del dataset maestro.

## 7. Conclusiones del levantamiento funcional y de datos

El levantamiento realizado permite consolidar los siguientes elementos para el diseño del prototipo:

- el usuario principal es operativo y requiere una visualización simple, directa y confiable;
- la necesidad funcional central es anticipar condiciones de congestión para apoyar la habilitación de filtros y la redistribución de recursos;
- la salida principal del artefacto debe ser una alerta agregada por zona, complementada con una vista operativa actual y una vista histórica de comparación;
- el detalle por filtro debe existir en dos niveles: distribución actual del flujo para la lectura intradía y consulta histórica para el análisis retrospectivo;
- la granularidad de analisis adecuada para el MVP es de 15 minutos;
- los horizontes de mayor valor operativo son 2h y 4h, mientras que 6h y 24h deben mantenerse disponibles con una lectura explícita de mayor incertidumbre;
- el target principal debe construirse con el flujo observado en filtros, usando como soporte la secuencia entre programación de vuelos, ingreso al muelle y paso por filtros;
- la capacidad operativa debe calcularse con base en filtros activos y tiempo promedio de proceso;
- el alcance del prototipo debe concentrarse en los 13 filtros de la zona internacional objetivo, manteniendo el detalle por filtro como analítica complementaria.
