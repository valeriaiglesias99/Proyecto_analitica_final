"""
Tablero Predictivo — Habilitación de Filtros y Alertas de Congestión
"""

import datetime
import requests
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go


#Configuración de la página

st.set_page_config(
    page_title="Tablero Predictivo · Zona Internacional",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded",
)

API_URL = "http://137.184.102.248"

# Umbrales

ALERT_THRESHOLD = 356.09
CRITICAL_THRESHOLD = 432.39
MAX_CAPACITY = 508.7

st.markdown("""
<style>
/* Fondo oscuro principal */
[data-testid="stAppViewContainer"] { background: #1a1a1a; }
[data-testid="stSidebar"] { background: #111111; }
[data-testid="stHeader"] { background: transparent; }

/* Tarjetas */
.card {
    background: #242424;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 12px;
}
.card-light {
    background: #f9f8f4;
    border-radius: 12px;
    padding: 18px 22px;
    margin-bottom: 12px;
    color: #111;
}

/* Métricas personalizadas */
.metric-label {
    font-size: 10px;
    font-weight: 600;
    letter-spacing: .08em;
    text-transform: uppercase;
    color: #888;
    margin-bottom: 2px;
}
.metric-value {
    font-size: 28px;
    font-weight: 700;
    color: #f9f8f4;
    line-height: 1.1;
}
.metric-value-dark {
    font-size: 28px;
    font-weight: 700;
    color: #111;
    line-height: 1.1;
}
.metric-sub {
    font-size: 11px;
    color: #888;
    margin-top: 2px;
}

/* Badges de estado */
.badge-ok    { background:#1a3a1a; color:#4caf50; border-radius:6px; padding:3px 10px; font-size:12px; font-weight:700; }
.badge-alert { background:#3a2e00; color:#f5c518; border-radius:6px; padding:3px 10px; font-size:12px; font-weight:700; }
.badge-crit  { background:#3a1010; color:#f44336; border-radius:6px; padding:3px 10px; font-size:12px; font-weight:700; }

/* Gauge text */
.gauge-pct { font-size:42px; font-weight:800; text-align:center; }

/* Títulos de sección */
h1,h2,h3 { color: #f9f8f4 !important; }
p, .stMarkdown p { color: #ccc; }

/* Sidebar labels */
[data-testid="stSidebar"] label { color: #aaa !important; font-size:12px !important; }
[data-testid="stSidebar"] .stSlider p { color: #aaa !important; }
</style>
""", unsafe_allow_html=True)


#Alarmas

def status_badge(is_alert: bool, is_critical: bool) -> str:
    if is_critical:
        return '<span class="badge-crit">🔴 CRÍTICO</span>'
    if is_alert:
        return '<span class="badge-alert">🟡 ALERTA</span>'
    return '<span class="badge-ok">🟢 NORMAL</span>'

def gauge_color(pct: float) -> str:
    if pct >= 85:
        return "#f44336"
    if pct >= 70:
        return "#f5c518"
    return "#4caf50"

def call_predict(payload: dict) -> dict | None:
    try:
        r = requests.post(f"{API_URL}/predict", json=payload, timeout=8)
        r.raise_for_status()
        return r.json()
    except Exception as e:
        st.error(f"Error llamando a la API: {e}")
        return None

def check_health() -> bool:
    try:
        r = requests.get(f"{API_URL}/health", timeout=4)
        return r.status_code == 200
    except Exception:
        return False

def build_gauge(value: float, max_val: float = MAX_CAPACITY) -> go.Figure:
    pct = min(value / max_val * 100, 100)
    color = gauge_color(pct)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        number={"suffix": " pax", "font": {"size": 28, "color": color}},
        gauge={
            "axis": {"range": [0, max_val], "tickcolor": "#555", "tickfont": {"color": "#888"}},
            "bar": {"color": color, "thickness": 0.7},
            "bgcolor": "#333",
            "borderwidth": 0,
            "steps": [
                {"range": [0, ALERT_THRESHOLD], "color": "#1a3a1a"},
                {"range": [ALERT_THRESHOLD, CRITICAL_THRESHOLD], "color": "#3a2e00"},
                {"range": [CRITICAL_THRESHOLD, max_val], "color": "#3a1010"},
            ],
            "threshold": {
                "line": {"color": "#f44336", "width": 3},
                "thickness": 0.75,
                "value": CRITICAL_THRESHOLD,
            },
        },
    ))
    fig.update_layout(
        paper_bgcolor="#242424", plot_bgcolor="#242424",
        margin=dict(t=20, b=10, l=20, r=20), height=220,
        font={"color": "#f9f8f4"},
    )
    return fig

def build_history_chart(history: list[dict]) -> go.Figure:
    """Simulated 2-hour history sparkline."""
    if not history:
        return go.Figure()
    slots = [h["slot"] for h in history]
    vals  = [h["flow"] for h in history]

    ma = pd.Series(vals).rolling(4, min_periods=1).mean().tolist()

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=slots, y=vals, mode="lines", name="Observado",
        line=dict(color="#f5c518", width=2),
    ))
    fig.add_trace(go.Scatter(
        x=slots, y=ma, mode="lines", name="Promedio comparable",
        line=dict(color="#888", width=1.5, dash="dash"),
    ))
    # Alert band
    fig.add_hrect(
        y0=ALERT_THRESHOLD, y1=CRITICAL_THRESHOLD,
        fillcolor="rgba(245,197,24,.08)", line_width=0,
    )
    fig.add_hrect(
        y0=CRITICAL_THRESHOLD, y1=MAX_CAPACITY,
        fillcolor="rgba(244,67,54,.10)", line_width=0,
    )
    fig.update_layout(
        paper_bgcolor="#242424", plot_bgcolor="#242424",
        margin=dict(t=10, b=10, l=10, r=10), height=180,
        legend=dict(font=dict(size=10, color="#aaa"), bgcolor="rgba(0,0,0,0)"),
        xaxis=dict(showgrid=False, tickfont=dict(color="#666"), color="#666"),
        yaxis=dict(showgrid=True, gridcolor="#333", tickfont=dict(color="#666"), color="#666"),
        font=dict(color="#f9f8f4"),
    )
    return fig

#  Crendo historia en la sesión

if "history" not in st.session_state:
    st.session_state.history = []   # lista de dicts {slot, flow, ts}
if "last_result" not in st.session_state:
    st.session_state.last_result = None
if "view" not in st.session_state:
    st.session_state.view = "Ahora"

#Entradas del modelo
with st.sidebar:
    st.markdown("## ⚙️ Parámetros de entrada")

    st.markdown("### 📅 Contexto temporal")
    now = datetime.datetime.now()
    slot_minute = (now.hour * 60 + (now.minute // 15) * 15)
    dia_semana  = now.weekday()
    es_fin_semana = int(dia_semana >= 5)
    mes = now.month

    st.caption(f"Franja actual: **{now.strftime('%H:%M')}** · Slot `{slot_minute}` min")
    st.caption(f"Día semana: `{dia_semana}` ({'Fin de semana' if es_fin_semana else 'Laboral'})")

    st.markdown("---")
    st.markdown("### ✈️ Programa de vuelos")
    vuelos_programados    = st.slider("Vuelos programados",     0, 20, 3)
    pasajeros_programados = st.slider("Pasajeros programados", 0, 800, 400, step=10)

    st.markdown("---")
    st.markdown("### 🛂 VeriPax — franja actual")
    veripax_total     = st.slider("Total VeriPax",      0, 500, 150, step=5)
    veripax_0_60      = st.slider("VeriPax 0–60 min",   0, 200, 40,  step=5)
    veripax_60_120    = st.slider("VeriPax 60–120 min", 0, 200, 60,  step=5)
    veripax_120_180   = st.slider("VeriPax 120–180 min",0, 200, 30,  step=5)
    veripax_180_mas   = st.slider("VeriPax >180 min",   0, 200, 10,  step=5)
    veripax_sin_sobt  = st.slider("VeriPax sin SOBT",   0, 100, 10,  step=5)

    st.markdown("---")
    st.markdown("### 📡 Rezagos del sensor")
    sensor_lag_1 = st.number_input("Sensor hace 15 min",  value=120.0, step=5.0)
    sensor_lag_2 = st.number_input("Sensor hace 30 min",  value=110.0, step=5.0)
    sensor_lag_4 = st.number_input("Sensor hace 1 hora",  value=95.0,  step=5.0)
    sensor_lag_8 = st.number_input("Sensor hace 2 horas", value=80.0,  step=5.0)

    st.markdown("---")
    st.markdown("### 🔄 Rezagos VeriPax")
    veripax_lag_1 = st.number_input("VeriPax hace 15 min",  value=140.0, step=5.0)
    veripax_lag_2 = st.number_input("VeriPax hace 30 min",  value=130.0, step=5.0)
    veripax_lag_4 = st.number_input("VeriPax hace 1 hora",  value=110.0, step=5.0)
    veripax_lag_8 = st.number_input("VeriPax hace 2 horas", value=90.0,  step=5.0)

    st.markdown("---")
    st.markdown("### 📊 Promedios móviles")
    sensor_roll_mean_4  = st.number_input("Sensor roll mean 1h",  value=105.0, step=5.0)
    sensor_roll_mean_8  = st.number_input("Sensor roll mean 2h",  value=98.0,  step=5.0)
    veripax_roll_mean_4 = st.number_input("VeriPax roll mean 1h", value=132.0, step=5.0)
    veripax_roll_mean_8 = st.number_input("VeriPax roll mean 2h", value=120.0, step=5.0)

    # VeriPax ratio
    veripax_to_pax_ratio = (
        veripax_total / pasajeros_programados
        if pasajeros_programados > 0 else 0.0
    )
    st.caption(f"veripax_to_pax_ratio calculado: `{veripax_to_pax_ratio:.3f}`")

    st.markdown("---")
    predict_btn = st.button("Predecir próxima franja", use_container_width=True, type="primary")

# Valores que se cargan al modelo

payload = {
    "veripax_total": float(veripax_total),
    "veripax_0_60": float(veripax_0_60),
    "veripax_60_120": float(veripax_60_120),
    "veripax_120_180": float(veripax_120_180),
    "veripax_180_mas": float(veripax_180_mas),
    "veripax_sin_sobt": float(veripax_sin_sobt),
    "vuelos_programados": float(vuelos_programados),
    "pasajeros_programados": float(pasajeros_programados),
    "dia_semana": int(dia_semana),
    "es_fin_semana": int(es_fin_semana),
    "mes": int(mes),
    "slot_minute": int(slot_minute),
    "sensor_lag_1": float(sensor_lag_1),
    "sensor_lag_2": float(sensor_lag_2),
    "sensor_lag_4": float(sensor_lag_4),
    "sensor_lag_8": float(sensor_lag_8),
    "veripax_lag_1": float(veripax_lag_1),
    "veripax_lag_2": float(veripax_lag_2),
    "veripax_lag_4": float(veripax_lag_4),
    "veripax_lag_8": float(veripax_lag_8),
    "sensor_roll_mean_4": float(sensor_roll_mean_4),
    "sensor_roll_mean_8": float(sensor_roll_mean_8),
    "veripax_roll_mean_4": float(veripax_roll_mean_4),
    "veripax_roll_mean_8": float(veripax_roll_mean_8),
    "veripax_to_pax_ratio": float(veripax_to_pax_ratio),
}

#  Llamada a la API

if predict_btn:
    with st.spinner("Consultando modelo rf_iter_2…"):
        result = call_predict(payload)
    if result:
        st.session_state.last_result = result
        st.session_state.history.append({
            "slot": now.strftime("%H:%M"),
            "flow": result["predicted_flow"],
            "ts": now,
        })
        # Mantener solo las últimas 16 franjas (4 horas)
        st.session_state.history = st.session_state.history[-16:]

result = st.session_state.last_result


col_title, col_health = st.columns([5, 1])
with col_title:
    st.markdown("# ✈️ Tablero Predictivo — Habilitación de Filtros")
    st.caption("Muelle Internacional - Granularidad 15 min - Modelo `rf_iter_2`")
with col_health:
    healthy = check_health()
    if healthy:
        st.success("API ✅ online")
    else:
        st.error("API ❌ offline")

st.markdown("---")

# Paginas, ahora e histórico
view_col1, view_col2 = st.columns([1, 4])
with view_col1:
    view = st.radio("Vista del informe", ["Ahora", "Histórico"],
                    horizontal=True, label_visibility="collapsed")
    st.session_state.view = view

# Página de Ahora

if st.session_state.view == "Ahora":

    if result is None:
        st.info("👈 Ajusta los parámetros en el panel izquierdo y presiona **Predecir próxima franja**.")
    else:
        flow   = result["predicted_flow"]
        pct    = flow / MAX_CAPACITY * 100
        is_a   = result["is_alert"]
        is_c   = result["is_critical"]

        # KPIs
        st.markdown("### 📊 Resumen de la predicción")
        k1, k2, k3, k4, k5 = st.columns(5)

        with k1:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Franja analizada</div>
                <div class="metric-value">{now.strftime('%H:%M')}</div>
                <div class="metric-sub">{now.strftime('%d %b %Y')}</div>
            </div>""", unsafe_allow_html=True)

        with k2:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Flujo predicho</div>
                <div class="metric-value" style="color:{'#f44336' if is_c else '#f5c518' if is_a else '#4caf50'}">{flow:.0f}</div>
                <div class="metric-sub">pasajeros · próximos 15 min</div>
            </div>""", unsafe_allow_html=True)

        with k3:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Capacidad utilizada</div>
                <div class="metric-value" style="color:{'#f44336' if is_c else '#f5c518' if is_a else '#4caf50'}">{pct:.1f}%</div>
                <div class="metric-sub">de {MAX_CAPACITY:.0f} pax máx.</div>
            </div>""", unsafe_allow_html=True)

        with k4:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Estado</div>
                <div style="margin-top:6px">{status_badge(is_a, is_c)}</div>
                <div class="metric-sub" style="margin-top:6px">Umbral alerta: {ALERT_THRESHOLD} pax</div>
            </div>""", unsafe_allow_html=True)

        with k5:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">VeriPax actual</div>
                <div class="metric-value">{veripax_total}</div>
                <div class="metric-sub">Ratio: {veripax_to_pax_ratio:.2f}</div>
            </div>""", unsafe_allow_html=True)

        # Gauge + Breakdown 
        st.markdown("---")
        g_col, b_col = st.columns([1, 1])

        with g_col:
            st.markdown("#### Indicador de carga")
            st.plotly_chart(build_gauge(flow), use_container_width=True, config={"displayModeBar": False})
            # Umbral visual
            st.markdown(f"""
            <div style="display:flex; gap:12px; margin-top:4px">
                <span class="badge-ok">🟢 Normal &lt;{ALERT_THRESHOLD:.0f}</span>
                <span class="badge-alert">🟡 Alerta ≥{ALERT_THRESHOLD:.0f}</span>
                <span class="badge-crit">🔴 Crítico ≥{CRITICAL_THRESHOLD:.0f}</span>
            </div>""", unsafe_allow_html=True)

        with b_col:
            st.markdown("#### Distribución VeriPax")
            cats = ["0–60 min", "60–120 min", "120–180 min", ">180 min", "Sin SOBT"]
            vals = [veripax_0_60, veripax_60_120, veripax_120_180, veripax_180_mas, veripax_sin_sobt]
            colors = ["#f5c518", "#c8a000", "#9a7a00", "#6b5600", "#444"]
            fig_bar = go.Figure(go.Bar(
                x=cats, y=vals, marker_color=colors,
                text=[f"{v}" for v in vals], textposition="outside",
                textfont=dict(color="#ccc", size=11),
            ))
            fig_bar.update_layout(
                paper_bgcolor="#242424", plot_bgcolor="#242424",
                margin=dict(t=10, b=10, l=10, r=10), height=220,
                xaxis=dict(tickfont=dict(color="#888"), color="#888", showgrid=False),
                yaxis=dict(tickfont=dict(color="#555"), color="#555",
                           gridcolor="#333", range=[0, max(vals) * 1.3 + 5]),
                font=dict(color="#f9f8f4"),
                showlegend=False,
            )
            st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})

        #Recomendación operativa
        st.markdown("---")
        st.markdown("#### 💡 Recomendación operativa")
        if is_c:
            st.error(
                f"**🔴 Nivel CRÍTICO** — Se predicen **{flow:.0f} pax** en los próximos 15 min "
                f"({pct:.1f}% de capacidad). Activar todos los filtros de seguridad disponibles "
                f"y abrir carriles adicionales inmediatamente."
            )
        elif is_a:
            st.warning(
                f"**🟡 Nivel ALERTA** — Se predicen **{flow:.0f} pax** ({pct:.1f}% de capacidad). "
                f"Considerar habilitar filtros adicionales en los próximos minutos."
            )
        else:
            st.success(
                f"**🟢 Operación Normal** — Se predicen **{flow:.0f} pax** ({pct:.1f}% de capacidad). "
                f"Los filtros actuales son suficientes para la próxima franja."
            )

        # Historial de la sesión 
        if len(st.session_state.history) > 1:
            st.markdown("---")
            st.markdown("#### 📈 Evolución en la sesión")
            st.plotly_chart(
                build_history_chart(st.session_state.history),
                use_container_width=True,
                config={"displayModeBar": False},
            )

# Página Histórico

else:
    st.markdown("### 📅 Vista Histórica — Análisis comparativo")

    if len(st.session_state.history) == 0:
        st.info("Aún no hay predicciones en esta sesión. Ejecuta al menos una predicción en la vista **Ahora**.")
    else:
        df = pd.DataFrame(st.session_state.history)
        df["pct"] = df["flow"] / MAX_CAPACITY * 100
        df["estado"] = df["flow"].apply(
            lambda f: "🔴 Crítico" if f >= CRITICAL_THRESHOLD
            else ("🟡 Alerta" if f >= ALERT_THRESHOLD else "🟢 Normal")
        )

        # KPIs históricos
        h1, h2, h3, h4 = st.columns(4)
        with h1:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Pico del día</div>
                <div class="metric-value">{df['flow'].max():.0f} pax</div>
                <div class="metric-sub">máximo predicho</div>
            </div>""", unsafe_allow_html=True)
        with h2:
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Promedio sesión</div>
                <div class="metric-value">{df['flow'].mean():.0f} pax</div>
                <div class="metric-sub">por franja</div>
            </div>""", unsafe_allow_html=True)
        with h3:
            alerts = (df["flow"] >= ALERT_THRESHOLD).sum()
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Franjas en alerta</div>
                <div class="metric-value" style="color:#f5c518">{alerts}</div>
                <div class="metric-sub">de {len(df)} predicciones</div>
            </div>""", unsafe_allow_html=True)
        with h4:
            crits = (df["flow"] >= CRITICAL_THRESHOLD).sum()
            st.markdown(f"""
            <div class="card">
                <div class="metric-label">Franjas críticas</div>
                <div class="metric-value" style="color:#f44336">{crits}</div>
                <div class="metric-sub">de {len(df)} predicciones</div>
            </div>""", unsafe_allow_html=True)

        st.markdown("---")
        # Gráfico comparativo
        st.plotly_chart(
            build_history_chart(st.session_state.history),
            use_container_width=True,
            config={"displayModeBar": False},
        )

        # Tabla detallada
        st.markdown("#### 📋 Detalle por franja")
        df_display = df[["slot", "flow", "pct", "estado"]].copy()
        df_display.columns = ["Franja", "Flujo predicho (pax)", "Capacidad (%)", "Estado"]
        df_display["Flujo predicho (pax)"] = df_display["Flujo predicho (pax)"].round(1)
        df_display["Capacidad (%)"] = df_display["Capacidad (%)"].round(1)
        st.dataframe(df_display, use_container_width=True, hide_index=True)

        # Exportar CSV
        csv = df_display.to_csv(index=False).encode("utf-8")
        st.download_button(
            "⬇️ Exportar CSV",
            data=csv,
            file_name=f"predicciones_{now.strftime('%Y%m%d_%H%M')}.csv",
            mime="text/csv",
        )

# Información sobre modelo utilizado

st.markdown("---")
st.caption(
    "Modelo `rf_iter_2` · Random Forest 600 estimadores · "
    "WMAPE 17.9% · Zona 15 — Muelle Internacional · "
    f"API: `{API_URL}`"
)
