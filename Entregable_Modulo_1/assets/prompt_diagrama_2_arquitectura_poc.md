# Prompt para generar el Diagrama 2

## Arquitectura simplificada de la POC

Genera un diagrama horizontal, limpio y profesional, para la arquitectura simplificada de una POC analitica de prediccion de demanda operativa en filtros de una zona internacional de control. No menciones nombres reales de organizaciones. El diagrama debe verse como una slide ejecutiva de consultoria, con fondo claro uniforme, cajas limpias, flechas claras, texto en espanol y data lineage visible de punta a punta.

El objetivo de este diagrama es mostrar la **implementacion minima de la solucion**, sin representar la arquitectura corporativa completa.

## Flujo obligatorio

El flujo debe verse claramente asi:

Fuentes historicas -> mecanismos de acceso -> integracion y calidad -> dataset maestro -> pipeline analitico -> capa de consumo

Debe ser un diagrama de data lineage entendible sin explicacion adicional.

## Bloques obligatorios

1. Fuentes de datos
- Programacion de vuelos
- Registros de validacion de ingreso al muelle
- Sensores de paso por filtros
- Catalogos auxiliares

Para cada fuente, mostrar tambien una subetiqueta de acceso o extraccion:
- tablas SQL Server integradas al entorno corporativo;
- vistas consolidadas o exportaciones controladas;
- historicos anonimizados derivados de la capa analitica.

Indicar que, para el MVP:
- la variable prioritaria de la fuente de vuelos es `pasajeros programados`;
- las fuentes de validacion y sensores tienen resolucion base a minuto;
- la lectura operativa final se consolida a 15 minutos.

2. Capa de integracion y calidad
- arquitectura medallion o capa equivalente de refinamiento progresivo;
- homologacion temporal;
- limpieza y validacion;
- tratamiento de faltantes;
- control de atipicos;
- filtrado de zona objetivo;
- regla de ventana comun;
- agregacion a 15 minutos;
- construccion de variables derivadas;
- muestra controlada y anonimizada para el MVP.

Incluir una nota de confidencialidad:
- el prototipo trabaja con una muestra anonimizada derivada de la arquitectura analitica;
- no usa conexion productiva completa.

3. Dataset maestro
- variables planificadas;
- variables de ingreso al muelle;
- variables de flujo en filtros;
- variables calendario;
- lags y variables derivadas;
- parametro de filtros activos;
- capacidad estimada;
- porcentaje de ocupacion.

4. Motor analitico
- baseline operativo;
- modelo interpretable de serie de tiempo;
- modelo supervisado;
- evaluacion temporal;
- validacion offline reproducible.

5. Salidas del modelo
- pronostico por franjas de 15 minutos;
- criticidad por zona;
- historico comparable;
- nivel visible de confianza;
- distribucion actual por filtro;
- historico por filtro;
- referencia de capacidad visible;
- porcentaje de ocupacion estimada.

6. Capa de consumo
- tablero principal;
- semaforo por zona;
- linea temporal de demanda;
- tabla de franjas criticas;
- vista `Ahora`;
- vista `Historico`;
- consulta complementaria por filtro.

## Mensajes que deben verse reflejados

- La solucion se apoya en una arquitectura medallion corporativa, pero el diagrama representa solo la arquitectura simplificada de la POC.
- La capacidad se estima a nivel minuto a partir de filtros activos y tiempo promedio de proceso por pasajero, y luego se consolida a la franja operativa de 15 minutos.
- La alerta principal se emite a nivel zona.
- El detalle por filtro es analitica complementaria.
- Los horizontes 2h y 4h son prioritarios; 6h y 24h siguen disponibles con mayor incertidumbre esperada.
- Umbrales de referencia:
  - alerta desde 70% de ocupacion;
  - criticidad desde 85% de ocupacion.

## Restricciones importantes

- No incluir optimizacion de turnos.
- No incluir asignacion automatica de personal.
- No representar la totalidad de la arquitectura empresarial.
- No mostrar despliegue productivo en tiempo real.
- No tratar la POC como sistema prescriptivo completo.

## Estilo visual

- fondo blanco o marfil muy claro;
- sin sombras fuertes ni gradientes oscuros;
- misma paleta sobria en verde oscuro, arena y gris;
- bordes suaves;
- iconos simples para fuente, ETL, dataset, modelo y dashboard;
- contraste medio-alto con texto negro o grafito;
- composicion ordenada y corporativa;
- incluir una pequena leyenda de convenciones.

Si este diagrama se va a usar junto con otro del prototipo fachada, ambos deben compartir exactamente el mismo estilo visual, mismo fondo, misma exposicion y misma jerarquia tipografica.

## Version corta

Genera un diagrama horizontal y profesional de la arquitectura simplificada de una POC analitica. Debe mostrar data lineage completo desde fuentes historicas hasta capa de consumo: fuentes SQL Server y vistas consolidadas, capa medallion o equivalente, limpieza y homologacion, agregacion de fuentes base a minuto hacia 15 minutos, dataset maestro, modelos, validacion offline y tablero final. La alerta principal es por zona, el detalle por filtro es complementario, la capacidad depende de filtros activos y tiempo promedio de proceso, y el diagrama no debe representar la arquitectura empresarial completa ni incluir optimizacion de turnos.
