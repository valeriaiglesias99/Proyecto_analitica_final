![Banner del proyecto](Banner_PAAD_01.jpg)

# Manual de Usuario
## Tablero Predictivo para Habilitación de Filtros y Alertas de Congestión

**Proyecto Aplicado en Analítica de Datos, Universidad de los Andes, 2026**  
Grupo 23
- Danilo Suárez Vargas
- Valeria Iglesias Miranda
- Sergio Andrés Perdomo Murcia

---

## Tabla de Contenidos

1. [Qué es y qué hace el artefacto](#1-qué-es-y-qué-hace-el-artefacto)
2. [Puesta en funcionamiento](#2-puesta-en-funcionamiento)
3. [Casos de uso y paso a paso](#3-casos-de-uso-y-paso-a-paso)
4. [Anexo técnico](#4-anexo-técnico)



## 1. Drescripción general del Artefacto

### 1.1 Descripción general

El **Tablero Predictivo de Flujo de Pasajeros** es una inrterfaz web interactiva que permite a los coordinadores operativos del aeropuerto anticipar la congestión en los filtros de seguridad en la zona internacional. A partir de señales en tiempo real (lecturas VeriPax, sensores de flujo y programa de vuelos), el tablero predice cuántos pasajeros llegarán a los filtros en los **próximos 15 minutos** y emite una alerta de semáforo operativo (normal, alerta y crítico),  para apoyar 
la decisión de habilitar filtros adicionales.

El artefacto tiene dos componentes:

| Componente | Descripción |
|---|---|
| **API**  | Servicio FastAPI desplegado en `http://137.184.102.248` que ejecuta el modelo Random Forest entrenado con datos históricos del aeropuerto (enero–marzo 2026). Su documentación se encuentra en el archivo `API_documentacion.md`. |
| **Tablero Streamlit** | App que permite al operador ingresar los valores de la franja actual, consultar la predicción y visualizar la evolución histórica. |

### 1.2 Funcionalidad del artefacto

- **Predice** el flujo de pasajeros en los filtros para la siguiente franja de 15 minutos.
- **Clasifica** el nivel de congestión esperada en tres categorías operativas con umbrales calibrados para 13 filtros activos.
- **Visualiza** un indicador de carga, la distribución de pasajeros VeriPax por ventana de anticipación, y la evolución histórica de predicciones en la sesión de consulta del usuario.
- **Recomienda** acciones operativas concretas según el nivel de alerta detectado. Se generan alertas según la predicción obtenida.
- **Exporta** el historial de predicciones de la sesión en formato CSV para análisis posterior y utilización del equipo.

### 1.3 Umbrales operativos

| Estado | Umbral | Capacidad | Acción sugerida |
|---|---|---|---|
| Normal | < 356 pax | < 70% | Operación estándar y normal. Filtros actuales suficientes, no es necesaria ninguna acción. |
| Alerta | ≥ 356 pax | ≥ 70% | Considerar habilitación de filtros adicionales. |
| Crítico | ≥ 432 pax | ≥ 85% | Activar todos los filtros disponibles inmediatamente. |


> **Cálculo de referencia:** capacidad máxima = 13 filtros × 39.1 pax/filtro/franja = 508.7 pax. Los umbrales corresponden al 70% y 85% de esa capacidad, calibrados con base en la dotación estándar de la zona internacional.

### 1.4 Ventajas del artefacto

- **Anticipación operativa:** la combinación de señales VeriPax (pasajeros ya en el muelle) y rezagos de sensores permite predecir la congestión con suficiente tiempo para reaccionar.
- **Sin instalación para el usuario final:** el tablero corre completamente en streamlit, accesible desde cualquier dispositivo con internet, ya sea computador o celular.
- **Exportación de datos:** el historial de predicciones de cada sesión puede descargarse en CSV para informes y seguimientos futuros.
- **Indicador visual:** el velocímetro y los rangos de color permiten identificar el estado en menos de 2 segundos sin leer números, generando una alerta rápida.

### 1.5 Limitaciones y advertencias

| Limitación | Descripción |
|---|---|
| **Requiere datos manuales** | El operador debe ingresar los valores de sensores y VeriPax de la franja actual, cada uno de los valores de forma manual. En el prototipo no hay integración automática con los sistemas del aeropuerto. |
| **Error promedio de ~28 pax** | El modelo tiene un WMAPE de 17.9% sobre datos de validación, equivalente a ~28 pasajeros de error en promedio, no debe usarse como único criterio de decisión en situaciones límite y se debe tener presente este error. |
| **Subestima picos extremos** | El modelo tiende a subestimar flujos por encima de 400 pax debido a eventos no observables, como lostiempos de migración variables o pasajeros de conexión sin validación VeriPax. |
| **Sin historial entre sesiones** | El historial de las predicciones se pierde al cerrar o recargar la página. Por esto es necesario descargar los csv de las predicciones. |
| **API debe estar activa** | Si la API en `http://137.184.102.248` no responde, el tablero no puede generar predicciones. |
| **Datos de entrenamiento** | El modelo fue entrenado con datos de enero a marzo de 2026, si los patrones del aeropuerto cambian respecto al periodo de entrenamiento, la capacidad de predicción del modelo puede empeorar. |

## 2. Puesta en funcionamiento

### 2.1 Acceso al prototipo, usuario final:

El tablero está desplegado públicamente y no requiere instalación:

> 🔗 **URL de acceso:** ` https://proyecto-final-dsa.streamlit.app/

**Requisitos del usuario/operador:**
- Conexión a internet
- No se requieren conocimientos técnicos ni instalación de software

### 2.2 Instalación local, usuario técnico:

Para ejecutar el tablero localmente desde el repositorio:

**Pasos:**

```bash
# 1. Clonar el repositorio
git clone https://github.com/danilosuarez/Proyecto_analitica_final.git
cd Proyecto_analitica_final/Entregable_3

# 2. Crear entorno virtual
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la aplicación
streamlit run app.py
```

La aplicación se abre automáticamente en una página del navegador.

Las dependencias requeridas se encuentran en `requirements.txt`.


### 2.3 Verificación de funcionamiento

Para verificar la correcta ejecución de la aplicación, al cargar la página se debe observar:

- El título **"Tablero Predictivo — Habilitación de Filtros"** en la 
  parte superior.
- Los controles deslizantes en el panel lateral izquierdo.
- El mensaje **"API online"** en verde en la esquina superior derecha, al lado del título.

Si aparece **"API offline"**, la APPI no está disponible. Será necesario verificar la conexión a internet y recargar la página.

## 3. Casos de uso y paso a paso

### Primer caso: Análisis en tiempo real, página "Ahora":

**Perfil de usuario:** Coordinador operativo de turno  
**Objetivo:** Saber cuántos pasajeros llegarán a los filtros en los próximos 15 minutos y si debe habilitar filtros adicionales.

**Paso a paso:**

**Paso 1 : Ingresar el programa de vuelos**
En el panel izquierdo es necesario ajustar:
- `Vuelos programados`: número de vuelos internacionales en la franja actual
- `Pasajeros programados`: total de pasajeros en esos vuelos.

**Paso 2 : Ingresar valores VeriPax**
Ingresar las lecturas del sistema VeriPax para la franja actual de manera manual:
- `Total VeriPax`: total de validaciones de acceso al muelle
- `VeriPax 0–60 min`: pasajeros con menos de 1 hora para su vuelo
- `VeriPax 60–120 min`: pasajeros entre 1 y 2 horas para su vuelo
- `VeriPax 120–180 min`: pasajeros entre 2 y 3 horas
- `VeriPax >180 min`: pasajeros con más de 3 horas
- `VeriPax sin SOBT`: validaciones sin vuelo emparejado

**Paso 3 : Ingresar rezagos de sensores**
Ingresar el flujo medido por los sensores de filtros en las últimas 2 horas:
- `Sensor hace 15 min`: flujo de la franja anterior
- `Sensor hace 30 min`: flujo de hace 2 franjas
- `Sensor hace 1 hora`: flujo de hace 4 franjas
- `Sensor hace 2 horas`: flujo de hace 8 franjas

**Paso 4 : Ingresar rezagos VeriPax y promedios móviles**
De forma similar, ingresar los valores históricos de VeriPax y los promedios móviles calculados sobre las últimas 1 y 2 horas.

Los campos de fecha, hora, día de semana y mes se calculan automáticamente del reloj de la aplicación.

**Paso 5 : Generar la predicción**
Clic en el botón **" Predecir próxima franja"** en la parte inferior del panel izquierdo.

**Paso 6 : Análisis de resultados**
El tablero muestra:

| Elemento | Qué significa |
|---|---|
| **Velocímetro** | Nivel de carga esperado sobre la capacidad máxima |
| **Flujo predicho** | Número de pasajeros esperados en los próximos 15 min |
| **Capacidad utilizada** | Porcentaje de la capacidad máxima de 13 filtros |
| **Clasificación del estado** | Verde-  Normal / Amarillo - Alerta / Rojo - Crítico |
| **Recomendación operativa** | Acción sugerida |
| **Gráfico de barras VeriPax** | Distribución de pasajeros por ventana de anticipación |

**Paso 7 — Actuar según la recomendación**
- **Normal**: continuar con los filtros actuales
- **Alerta**: evaluar habilitar 1–2 filtros adicionales en los próximos minutos
- **Crítico**: activar todos los filtros disponibles de inmediato y alertar al supervisor

En esta versión del prototipo, los datos para generar predicciones se ingresan de forma manual: valores de VeriPax, rezagos de sensores y programa de vuelos. En versiones futuras se contempla la integración directa con los sistemas operativos del aeropuerto (VeriPax, sensores y DCS) para automatizar el ingreso de datos y permitir la generación de múltiples predicciones por franja de forma continua.

### Sgundo caso : Análisis de histórico, página de "Histórico":

**Perfil de usuario:** Coordinador de turno o supervisor  
**Objetivo:** Revisar el comportamiento de la demanda durante el turno y generar un reporte.

**Paso a paso:**

**Paso 1 : Guardar predicciones**
Realizar al menos 2 predicciones en la Vista "Ahora" durante el turno (una por franja de 15 minutos).

**Paso 2 : Cambiar a vista histórica**
En la parte superior del tablero, seleccionar **"Histórico"** en el cambio de páginas.

**Paso 3 : Revisar los KPIs del turno**
El tablero muestra automáticamente:
- Pico máximo predicho durante la sesión
- Promedio de flujo por franja
- Número de franjas que superaron el umbral de alerta
- Número de franjas que alcanzaron nivel crítico

**Paso 4 : Analizar la gráfica de evolución**
La gráfica de líneas muestra:
- Línea amarilla: flujos predichos por franja
- Línea gris punteada: promedio móvil de la sesión
- Bandas de color: zonas de alerta y crítico

**Paso 5 : Exportar el reporte**
Clic en **"Exportar CSV"** para descargar la tabla completa con todas las franjas, flujos predichos, porcentajes de capacidad y estados. El archivo se guarda con el nombre `predicciones_YYYYMMDD_HHMM.csv`.



## 4. Anexo técnico

### 4.1 Diagrama de la arquitectura

```
┌─────────────────────────────────────────────────────────────────┐
│                    FUENTES DE DATOS                             │
│  [Sensores filtros]  [Sistema VeriPax]  [Programa de vuelos]    │
└──────────────────────────┬──────────────────────────────────────┘
                           │ Features (25 variables)
                           ▼
┌─────────────────────────────────────┐
│         API de Predicción           │
│  FastAPI · rf_iter_2.joblib         │
│  Random Forest · 600 estimadores    │
│  http://137.184.102.248/predict     │
│  POST → predicted_flow + alertas    │
└──────────────────┬──────────────────┘
                   │ JSON response
                   ▼
┌─────────────────────────────────────┐
│      Tablero Streamlit              │
│  Vista Ahora  │  Vista Histórico    │
│  Velocimetro · KPIs · Recomendación │
│  Historial · Exportar CSV           │
│  proyecto-final-dsa.streamlit.app/  │
└─────────────────────────────────────┘
                   │
                   ▼
        Coordinador operativo
```

### 4.2 Modelo utilizado

| Propiedad | Valor |
|---|---|
| Algoritmo | Random Forest (`rf_iter_2`) |
| Estimadores | 600 árboles |
| Granularidad | Franjas de 15 minutos |
| Horizonte | 1 paso adelante (próximos 15 min) |
| WMAPE validación | 17.9% (~28 pax error promedio) |
| WMAPE test | Documentado en `train_val_test_comparison.csv` |
| Período entrenamiento | 1 Ene – 24 Feb 2026 |
| Período prueba | 20 Mar – 31 Mar 2026 |
| Artefacto | `best_model.joblib` |

### 4.3 Variables de entrada del modelo, 25 variables

| Grupo | Variables |
|---|---|
| VeriPax actual | `veripax_total`, `veripax_0_60`, `veripax_60_120`, `veripax_120_180`, `veripax_180_mas`, `veripax_sin_sobt` |
| Vuelos | `vuelos_programados`, `pasajeros_programados` |
| Calendario | `dia_semana`, `es_fin_semana`, `mes`, `slot_minute` |
| Rezagos sensor | `sensor_lag_1`, `sensor_lag_2`, `sensor_lag_4`, `sensor_lag_8` |
| Rezagos VeriPax | `veripax_lag_1`, `veripax_lag_2`, `veripax_lag_4`, `veripax_lag_8` |
| Promedios móviles | `sensor_roll_mean_4`, `sensor_roll_mean_8`, `veripax_roll_mean_4`, `veripax_roll_mean_8` |
| Derivada | `veripax_to_pax_ratio` |

### 4.4 Repositorio de código

| Recurso | Ubicación |
|---|---|
| Repositorio GitHub | `https://github.com/danilosuarez/Proyecto_analitica_final` |
| Código del tablero | `Entregable_3/app.py` |
| Notebook de modelado | `Entregable_2_v2/notebooks/Notebook_Modelado_Modulo2_PAAD2026.ipynb` |
| Reporte de modelos | `Entregable_2_v2/Reporte_de_seleccion_y_parametrizacion_de_modelos.md` |
| Modelo entrenado | `Entregable_2_v2/resultados_modelado/artifacts/best_model.joblib` |
| Dataset de modelado | `Entregable_2_v2/bases_limpias/dataset_zona_15m.csv` |

### 4.5 Escenarios de degradación y contingencia

| Escenario | Señal | Acción |
|---|---|---|
| API offline | Badge "API offline" | Verificar conectividad. Contactar responsable técnico. |
| VeriPax < 1,000/día | Predicciones anómalas | Usar solo rezagos de sensores como referencia operativa. |
| WMAPE rolling > 25% | Predicciones sistemáticamente altas o bajas | Evaluar reentrenamiento del modelo. |
| Cambio en dotación de filtros | Umbral crítico no refleja realidad | Recalibrar umbrales en el código de la API. |
