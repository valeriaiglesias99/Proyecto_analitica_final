# Prompt para generar el Diagrama 1

## Prototipo fachada del artefacto

Genera un diagrama horizontal, limpio y profesional, para un prototipo analitico de prediccion de demanda operativa en filtros de una zona internacional de control. No menciones nombres reales de organizaciones. El diagrama debe verse como una slide ejecutiva de consultoria, con fondo claro uniforme, cajas limpias, flechas claras, texto en espanol y apariencia autocontenida.

El objetivo de este diagrama es representar el **prototipo fachada completo del artefacto**, conectando en un flujo coherente:

usuario -> necesidad -> requerimientos -> forma de uso -> modelos/analisis -> datos -> ETL -> salida

El diagrama debe ser entendible sin explicacion adicional y debe incluir una pequena leyenda o nota de alcance.

## Estructura obligatoria

Incluye estos bloques principales, en disposicion horizontal de izquierda a derecha:

1. Usuario
- Coordinador de operaciones
- Analista de control operativo

2. Necesidad
- anticipar franjas de mayor flujo;
- habilitar filtros con menor reaccion tardia;
- visualizar ocupacion esperada y comportamiento historico.

3. Requerimientos
- alerta principal por zona;
- prediccion en franjas de 15 minutos;
- vistas `Ahora` e `Historico`;
- detalle por filtro como analitica complementaria;
- ajuste manual de filtros activos;
- horizontes disponibles: 2h, 4h, 6h y 24h.

4. Forma de uso
- tablero principal;
- semaforo por zona;
- linea temporal de demanda;
- tabla de franjas criticas;
- selector global `Ahora / Historico`;
- detalle complementario por filtro;
- lectura de capacidad y porcentaje de ocupacion.

5. Modelos y analisis
- baseline operativo;
- modelo interpretable de serie de tiempo;
- modelo supervisado;
- evaluacion temporal;
- comparacion entre alternativas.

6. Datos
- programacion de vuelos;
- registros de validacion de ingreso al muelle;
- sensores de paso por filtros;
- catalogos auxiliares.

7. ETL
- homologacion temporal;
- limpieza y validacion;
- tratamiento de faltantes;
- control de atipicos;
- regla de ventana comun;
- agregacion desde fuentes con resolucion base a minuto hacia franjas de 15 minutos;
- construccion de variables derivadas;
- muestra controlada y anonimizada para el MVP.

8. Salida
- pronostico por zona;
- criticidad por zona;
- historico comparable;
- distribucion actual por filtro;
- historico por filtro;
- capacidad visible en unidades absolutas y relativas;
- porcentaje de ocupacion estimada;
- nivel visible de confianza.

## Mensajes que deben verse reflejados

- La alerta principal se emite a nivel zona.
- El detalle por filtro es analitica complementaria.
- Las fuentes operativas pueden venir con resolucion base a minuto, pero el tablero y la prediccion trabajan en franjas de 15 minutos.
- La capacidad depende del numero de filtros activos y de un tiempo promedio de proceso por pasajero.
- El calculo de capacidad se estima a minuto y se consolida en la franja operativa de 15 minutos.
- Umbrales de referencia:
  - alerta desde 70% de ocupacion;
  - criticidad desde 85% de ocupacion.
- El horizonte prioritario es de 2h a 4h, pero 6h y 24h siguen disponibles con mayor incertidumbre esperada.
- El artefacto se valida offline y no representa un despliegue productivo completo.

## Restricciones importantes

- No incluir optimizacion de turnos.
- No incluir asignacion automatica de personal.
- No incluir planificacion prescriptiva de recursos.
- No presentar el artefacto como una app movil.
- No presentar el diagrama como arquitectura corporativa completa.

## Estilo visual

- fondo blanco o marfil muy claro;
- sin sombras fuertes ni gradientes oscuros;
- misma paleta sobria en verde oscuro, arena y gris;
- bordes suaves;
- iconos simples para usuario, datos, modelo y dashboard;
- contraste medio-alto con texto negro o grafito;
- composicion ordenada y corporativa;
- incluir una pequena leyenda de convenciones.

Si este diagrama se va a usar junto con otro de arquitectura de la POC, ambos deben compartir exactamente el mismo estilo visual, mismo fondo, misma exposicion y misma jerarquia tipografica.

## Version corta

Genera un diagrama horizontal, profesional y autocontenido del prototipo fachada de un tablero predictivo para demanda operativa en filtros. Debe conectar usuario, necesidad, requerimientos, forma de uso, modelos, datos y ETL en un flujo coherente. La alerta principal es por zona, el detalle por filtro es complementario, las fuentes operativas pueden venir a minuto pero la lectura final es en 15 minutos, la capacidad depende de filtros activos y de 23 segundos por pasajero, y el tablero incluye vistas `Ahora` e `Historico`, ocupacion estimada y criticidad por zona. No incluyas optimizacion de turnos ni arquitectura empresarial completa.
