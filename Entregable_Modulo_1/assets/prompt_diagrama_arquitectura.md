# Prompt para generar los diagramas del prototipo

Usa este prompt en otra IA para generar una imagen limpia de los diagramas del prototipo.

## Prompt

Crea dos diagramas complementarios para un prototipo analitico de prediccion de demanda operativa en filtros de una zona internacional de control. El estilo debe ser profesional, limpio, corporativo, legible y con fondo claro. No menciones nombres reales de organizaciones. Usa una disposicion horizontal de izquierda a derecha, con cajas, flechas y etiquetas claras.

Ambos diagramas deben verse como parte de una misma serie visual:
- mismo tamano de lienzo y misma proporcion;
- mismo fondo claro, uniforme y luminoso;
- misma paleta y mismo contraste;
- misma jerarquia tipografica;
- evitar sombras fuertes, gradientes oscuros o fondos grises que hagan que uno de los diagramas se vea mas oscuro que el otro;
- exportar ambos con brillo y exposicion homogena, como si fueran dos slides del mismo deck ejecutivo.

Diagrama 1: prototipo fachada del artefacto
- Debe enfatizar la logica funcional completa del artefacto.
- Debe conectar claramente:
  usuario -> necesidad -> requerimientos -> forma de uso -> modelos/analisis -> datos -> ETL.
- Debe integrar en un solo flujo coherente los seis elementos del prototipo, no solo listarlos.
- Debe mostrar de manera visible la trazabilidad:
  usuario -> requerimiento -> funcionalidad -> modelo -> datos -> ETL -> salida.
- Debe verse como un artefacto autocontenido que un stakeholder pueda entender sin explicacion adicional.
- Debe incluir una pequena leyenda o nota de alcance que aclare convenciones y limite del MVP.

Diagrama 2: arquitectura simplificada de la POC
- Debe representar la implementacion minima de la solucion.
- Debe mostrar el flujo:
  fuentes historicas -> extraccion y consolidacion -> pipeline analitico -> capa de consumo.
- Debe verse claramente como un diagrama de data lineage desde la fuente hasta el consumo.
- Debe indicar, para cada fuente principal, el mecanismo previsto de acceso o extraccion.
- Debe reflejar que la solucion es reproducible y no corresponde a la arquitectura corporativa completa.

Los diagramas deben incluir estos bloques, distribuidos segun corresponda:

1. Fuentes de datos
- Programacion de vuelos
- Registros de validacion de ingreso al muelle
- Sensores de paso por filtros
- Catalogos auxiliares
- Mostrar tambien, junto a cada fuente o en una subetiqueta:
  - acceso mediante tablas SQL Server integradas al entorno corporativo o exportaciones controladas;
  - consulta a registros operativos anonimizados provenientes de SQL Server o vistas consolidadas;
  - extraccion desde historicos de sensores consolidados en el entorno analitico;
  - tablas maestras o dimensiones corporativas.

2. Capa de integracion y calidad
- Mostrar que, en el entorno corporativo, las fuentes pasan por una arquitectura medallion o una capa equivalente de refinamiento progresivo del dato.
- Homologacion temporal
- Limpieza y validacion
- Filtrado de zona objetivo
- Agregacion cada 15 minutos
- Incluir explicitamente actividades ETL clave:
  - limpieza de formatos;
  - tratamiento de faltantes;
  - control de atipicos;
  - regla de ventana comun;
  - exclusiones o agrupaciones justificadas.
- Incluir una nota clara de confidencialidad:
  el prototipo consume una muestra controlada y anonimizada derivada de la arquitectura analitica, no una conexion productiva completa.
- Incluir una nota pequena de riesgos de calidad con mitigaciones.

3. Dataset maestro
- Variables planificadas
- Variables de ingreso al muelle
- Variables de flujo en filtros
- Variables calendario
- Lags y variables derivadas

4. Motor analitico
- Baseline operativo
- Modelo interpretable de serie de tiempo
- Modelo supervisado
- Evaluacion temporal

5. Salidas del modelo
- Pronostico por franjas de 15 minutos
- Criticidad por zona
- Historico comparable
- Nivel de confianza
- Historico por filtro
- Distribucion actual del flujo por filtro
- Referencia de capacidad visible

6. Interfaz de consulta
- Tablero principal
- Semaforo por zona
- Linea temporal de demanda
- Tabla de franjas criticas
- Vista `Ahora`
- Vista `Historico`
- Vista historica por filtro

Incluye estas notas visuales:
- La alerta principal se emite a nivel zona.
- El detalle por filtro es analitica complementaria.
- El horizonte prioritario es de 2h a 4h; 6h y 24h son extensiones.
- La solucion se valida offline y es reproducible, sin despliegue productivo.
- El segundo diagrama debe incluir una nota: "Arquitectura simplificada de la POC; no representa la arquitectura empresarial completa".
- Incluir una pequena leyenda de convenciones:
  fuentes, procesos ETL, dataset, modelos y capa de consumo.

Estilo visual:
- cajas con bordes suaves,
- paleta sobria en verde oscuro, arena y gris,
- iconos simples para datos, modelo y dashboard,
- texto en espanol,
- flechas claras entre bloques,
- apariencia de slide corporativa o de consultoria,
- incluir leyenda breve y convenciones visuales sencillas,
- fondo blanco o marfil muy claro, uniforme en ambos diagramas,
- sombras minimas o inexistentes,
- contraste medio-alto con texto negro o grafito,
- evitar cualquier viñeta o borde que oscurezca uno de los diagramas frente al otro.

## Version corta

Genera dos diagramas horizontales, limpios y profesionales, con exactamente el mismo estilo visual, mismo fondo claro y misma exposicion. El primero debe ser el prototipo fachada completo del artefacto, conectando usuario, requerimientos, forma de uso, modelos, datos y ETL en un flujo coherente y autocontenido. El segundo debe ser una arquitectura simplificada de la POC con data lineage completo: Fuentes -> mecanismos de acceso -> ETL/calidad -> dataset maestro -> pipeline analitico -> capa de consumo. Alerta principal por zona, historico por filtro como complemento, granularidad de 15 minutos, horizontes 2h y 4h como foco, validacion offline reproducible y sin despliegue productivo.
