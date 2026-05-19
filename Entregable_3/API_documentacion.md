# API de Predicción de Flujo de Pasajeros

> Predice el número de pasajeros esperados en los filtros de seguridad de la zona internacional del aeropuerto para la siguiente franja de 15 minutos, basándose en rezagos de sensores en tiempo real, datos de VeriPax y características del programa de vuelos.

**URL Base:** `http://137.184.102.248`  
**Versión:** 1.0  
**Autenticación:** No requerida

---

## Tabla de Contenidos

- [Sobre el Modelo](#sobre-el-modelo)
- [Umbrales de Criticidad](#umbrales-de-criticidad)
- [Endpoints](#endpoints)
  - [GET /](#get-)
  - [GET /health](#get-health)
  - [POST /predict](#post-predict)
- [Variables de Entrada](#variables-de-entrada)
- [Esquema de Respuesta](#esquema-de-respuesta)
- [Códigos de Error](#códigos-de-error)
- [Ejemplos de Código](#ejemplos-de-código)
  - [cURL](#curl)
  - [Python](#python)
  - [JavaScript](#javascript)
- [Documentación Interactiva](#documentación-interactiva)
- [Desarrollo Local](#desarrollo-local)

---

## Sobre el Modelo

| Propiedad | Valor |
|---|---|
| Algoritmo | Random Forest (`rf_iter_2`) |
| Árboles | 600 estimadores |
| Granularidad | Franjas de 15 minutos |
| Horizonte de pronóstico | Próximos 15 minutos (1 paso adelante) |
| WMAPE (validación) | 17.9% (~28 pax de error promedio) |
| Período de entrenamiento | 1 Ene – 24 Feb, 2026 |
| Período de prueba | 20 Mar – 31 Mar, 2026 |

> **Importante:** El modelo requiere las últimas 2 horas de historial del sensor para calcular las variables de rezago (`sensor_lag_1` hasta `sensor_lag_8`). Tu cliente o backend debe rastrear y precalcular estos valores antes de llamar a `/predict`.

---

## Umbrales de Criticidad

Basado en 13 filtros activos con rendimiento de 23 pax/min por franja de 15 min (capacidad máxima: 508.7 pax).

| Estado | Umbral | Capacidad | Campo en respuesta |
|---|---|---|---|
| 🟢 Normal | < 356.09 pax | < 70% | `is_alert: false`, `is_critical: false` |
| 🟡 Alerta | ≥ 356.09 pax | ≥ 70% | `is_alert: true` |
| 🔴 Crítico | ≥ 432.39 pax | ≥ 85% | `is_critical: true` |

---

## Endpoints

### GET /

Retorna información básica sobre la API en ejecución.

**Respuesta `200 OK`**
```json
{
  "status": "ok",
  "model": "rf_iter_2",
  "version": "1.0"
}
```

---

### GET /health

Verifica que el servicio está activo y respondiendo. Úsalo para monitores de disponibilidad o verificaciones de salud de balanceadores de carga.

```bash
curl http://137.184.102.248/health
```

**Respuesta `200 OK`**
```json
{
  "status": "healthy"
}
```

---

### POST /predict

Acepta un cuerpo JSON con 25 variables de entrada y retorna el conteo predicho de pasajeros para la siguiente franja de 15 minutos, junto con indicadores de alerta y criticidad.

**Cabeceras**
```
Content-Type: application/json
```

> Los 25 campos son **obligatorios**. Un campo faltante o con tipo incorrecto retorna un error `422 Unprocessable Entity`.

---

## Variables de Entrada

Envía todos los campos como un objeto JSON plano en el cuerpo de la solicitud.

### Señales VeriPax

| Campo | Tipo | Descripción |
|---|---|---|
| `veripax_total` | float | Total de validaciones VeriPax en la franja actual |
| `veripax_0_60` | float | Pasajeros con 0–60 min para el despegue |
| `veripax_60_120` | float | Pasajeros con 60–120 min para el despegue |
| `veripax_120_180` | float | Pasajeros con 120–180 min para el despegue |
| `veripax_180_mas` | float | Pasajeros con >180 min para el despegue |
| `veripax_sin_sobt` | float | Validaciones sin vuelo emparejado (SOBT) |

### Programa de vuelos

| Campo | Tipo | Descripción |
|---|---|---|
| `vuelos_programados` | float | Número de vuelos programados en la franja |
| `pasajeros_programados` | float | Total de pasajeros programados en la franja |

### Variables de calendario

| Campo | Tipo | Descripción |
|---|---|---|
| `dia_semana` | int | Día de la semana (0 = Lunes … 6 = Domingo) |
| `es_fin_semana` | int | Indicador de fin de semana (0 o 1) |
| `mes` | int | Número de mes (1–12) |
| `slot_minute` | int | Minutos desde medianoche (0–1425, paso de 15) |

### Rezagos del sensor — últimas 2 horas de lecturas

| Campo | Tipo | Descripción |
|---|---|---|
| `sensor_lag_1` | float | Flujo del sensor hace 15 min |
| `sensor_lag_2` | float | Flujo del sensor hace 30 min |
| `sensor_lag_4` | float | Flujo del sensor hace 1 hora |
| `sensor_lag_8` | float | Flujo del sensor hace 2 horas |

### Rezagos VeriPax

| Campo | Tipo | Descripción |
|---|---|---|
| `veripax_lag_1` | float | Total VeriPax hace 15 min |
| `veripax_lag_2` | float | Total VeriPax hace 30 min |
| `veripax_lag_4` | float | Total VeriPax hace 1 hora |
| `veripax_lag_8` | float | Total VeriPax hace 2 horas |

### Promedios móviles

| Campo | Tipo | Descripción |
|---|---|---|
| `sensor_roll_mean_4` | float | Promedio móvil del sensor de 1 hora (últimas 4 franjas) |
| `sensor_roll_mean_8` | float | Promedio móvil del sensor de 2 horas (últimas 8 franjas) |
| `veripax_roll_mean_4` | float | Promedio móvil VeriPax de 1 hora |
| `veripax_roll_mean_8` | float | Promedio móvil VeriPax de 2 horas |

### Variable derivada

| Campo | Tipo | Descripción |
|---|---|---|
| `veripax_to_pax_ratio` | float | `veripax_total / pasajeros_programados` (usar `0.0` si el denominador es 0) |

---

## Esquema de Respuesta

| Campo | Tipo | Descripción |
|---|---|---|
| `predicted_flow` | float | Pasajeros predichos para la siguiente franja de 15 min (recortado ≥ 0) |
| `is_alert` | bool | `true` si `predicted_flow` ≥ 356.09 (70% de capacidad) |
| `is_critical` | bool | `true` si `predicted_flow` ≥ 432.39 (85% de capacidad) |
| `alert_threshold` | float | Constante de umbral de alerta: `356.09` |
| `critical_threshold` | float | Constante de umbral crítico: `432.39` |

**Ejemplo de respuesta `200 OK`**
```json
{
  "predicted_flow": 118.5,
  "is_alert": false,
  "is_critical": false,
  "alert_threshold": 356.09,
  "critical_threshold": 432.39
}
```

---

## Códigos de Error

| Código | Significado | Solución |
|---|---|---|
| `200` | OK — predicción retornada | — |
| `422` | Entidad no procesable — campo faltante o tipo incorrecto | Verificar que los 25 campos estén presentes con los tipos correctos |
| `500` | Error interno del servidor | Revisar logs: `journalctl -u passenger-api -n 50` |

---

## Ejemplos de Código

### cURL

```bash
curl -X POST http://137.184.102.248/predict \
  -H "Content-Type: application/json" \
  -d '{
    "veripax_total": 150,
    "veripax_0_60": 40,
    "veripax_60_120": 60,
    "veripax_120_180": 30,
    "veripax_180_mas": 10,
    "veripax_sin_sobt": 10,
    "vuelos_programados": 3,
    "pasajeros_programados": 400,
    "dia_semana": 2,
    "es_fin_semana": 0,
    "mes": 3,
    "slot_minute": 480,
    "sensor_lag_1": 120,
    "sensor_lag_2": 110,
    "sensor_lag_4": 95,
    "sensor_lag_8": 80,
    "veripax_lag_1": 140,
    "veripax_lag_2": 130,
    "veripax_lag_4": 110,
    "veripax_lag_8": 90,
    "sensor_roll_mean_4": 105,
    "sensor_roll_mean_8": 98,
    "veripax_roll_mean_4": 132,
    "veripax_roll_mean_8": 120,
    "veripax_to_pax_ratio": 0.375
  }'
```

---

### Python

```python
import requests

payload = {
    "veripax_total": 150,
    "veripax_0_60": 40,
    "veripax_60_120": 60,
    "veripax_120_180": 30,
    "veripax_180_mas": 10,
    "veripax_sin_sobt": 10,
    "vuelos_programados": 3,
    "pasajeros_programados": 400,
    "dia_semana": 2,
    "es_fin_semana": 0,
    "mes": 3,
    "slot_minute": 480,
    "sensor_lag_1": 120,
    "sensor_lag_2": 110,
    "sensor_lag_4": 95,
    "sensor_lag_8": 80,
    "veripax_lag_1": 140,
    "veripax_lag_2": 130,
    "veripax_lag_4": 110,
    "veripax_lag_8": 90,
    "sensor_roll_mean_4": 105,
    "sensor_roll_mean_8": 98,
    "veripax_roll_mean_4": 132,
    "veripax_roll_mean_8": 120,
    "veripax_to_pax_ratio": 0.375,
}

respuesta = requests.post(
    "http://137.184.102.248/predict",
    json=payload
)

datos = respuesta.json()
print(f"Flujo predicho: {datos['predicted_flow']} pax")
print(f"Alerta: {datos['is_alert']} | Crítico: {datos['is_critical']}")
```

---

### JavaScript

```javascript
const payload = {
  veripax_total: 150,
  veripax_0_60: 40,
  veripax_60_120: 60,
  veripax_120_180: 30,
  veripax_180_mas: 10,
  veripax_sin_sobt: 10,
  vuelos_programados: 3,
  pasajeros_programados: 400,
  dia_semana: 2,
  es_fin_semana: 0,
  mes: 3,
  slot_minute: 480,
  sensor_lag_1: 120,
  sensor_lag_2: 110,
  sensor_lag_4: 95,
  sensor_lag_8: 80,
  veripax_lag_1: 140,
  veripax_lag_2: 130,
  veripax_lag_4: 110,
  veripax_lag_8: 90,
  sensor_roll_mean_4: 105,
  sensor_roll_mean_8: 98,
  veripax_roll_mean_4: 132,
  veripax_roll_mean_8: 120,
  veripax_to_pax_ratio: 0.375,
};

const res = await fetch("http://137.184.102.248/predict", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify(payload),
});

const datos = await res.json();
console.log(`Predicho: ${datos.predicted_flow} pax`);
console.log(`Alerta: ${datos.is_alert} | Crítico: ${datos.is_critical}`);
```

---

## Documentación Interactiva

FastAPI genera documentación interactiva de forma automática:

| Interfaz | URL |
|---|---|
| Swagger UI | http://137.184.102.248/docs |
| ReDoc | http://137.184.102.248/redoc |

---

## Desarrollo Local

Para ejecutar la API localmente:

```bash
# Clonar el repositorio
git clone https://github.com/danilosuarez/Proyecto_analitica_final.git
cd Proyecto_analitica_final

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install fastapi uvicorn scikit-learn joblib numpy pydantic

# Ejecutar el servidor
uvicorn api:app --host 0.0.0.0 --port 8000
```

---

*Modelo: `rf_iter_2` · Random Forest · 600 estimadores · Entrenado con datos de la Zona 15 del aeropuerto, 2026*
