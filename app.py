
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# 1. CONFIGURACIÓN GENERAL
# ============================================================
st.set_page_config(
    page_title="La Cortina | Financial Intelligence",
    page_icon="🪟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paleta corporativa
NAVY = "#12304A"
BLUE = "#2563EB"
CYAN = "#0891B2"
GREEN = "#059669"
ORANGE = "#EA580C"
RED = "#DC2626"
PURPLE = "#7C3AED"
BG = "#F3F6FA"
TEXT = "#26364A"
MUTED = "#64748B"
PALETTE = [BLUE, CYAN, GREEN, ORANGE, PURPLE, RED]

st.markdown("""
<style>
.stApp {
    background-color: #F3F6FA;
    color: #26364A;
}
[data-testid="stHeader"] {
    background: rgba(243,246,250,0.9);
}
[data-testid="stSidebar"] {
    background-color: #102A43;
}
[data-testid="stSidebar"] * {
    color: #F1F5F9;
}
[data-testid="stSidebar"] [data-baseweb="select"] * {
    color: #26364A;
}
.main-title {
    font-size: 31px;
    font-weight: 800;
    color: #12304A;
    letter-spacing: -0.7px;
    margin-bottom: 0;
}
.subtitle {
    color: #64748B;
    font-size: 14px;
    margin-top: 5px;
    margin-bottom: 20px;
}
.section-title {
    color: #12304A;
    font-size: 21px;
    font-weight: 750;
    margin-top: 8px;
    margin-bottom: 12px;
}
.kpi-card {
    background: #FFFFFF;
    padding: 19px 20px;
    border-radius: 13px;
    border: 1px solid #E2E8F0;
    border-top: 4px solid #2563EB;
    box-shadow: 0 3px 12px rgba(15,23,42,0.045);
    min-height: 115px;
}
.kpi-label {
    color: #64748B;
    font-size: 12px;
    font-weight: 750;
    text-transform: uppercase;
    letter-spacing: 0.45px;
}
.kpi-value {
    color: #12304A;
    font-size: 25px;
    font-weight: 800;
    margin-top: 9px;
}
.kpi-note {
    color: #64748B;
    font-size: 12px;
    margin-top: 5px;
}
.section-card {
    background: white;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 15px;
}
.footer {
    text-align: center;
    color: #64748B;
    font-size: 12px;
    padding: 20px 0 8px 0;
}
div[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    padding: 15px;
    border-radius: 12px;
}
div[data-testid="stTabs"] button {
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# 2. FUNCIONES DE DISEÑO Y GRÁFICOS
# ============================================================
def moneda(valor):
    return f"Q{valor:,.2f}"


def tarjeta(titulo, valor, nota="", color=BLUE):
    st.markdown(
        f"""
        <div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-label">{titulo}</div>
            <div class="kpi-value">{valor}</div>
            <div class="kpi-note">{nota}</div>
        </div>
        """,
        unsafe_allow_html=True
    )


def titulo_seccion(texto):
    st.markdown(
        f'<div class="section-title">{texto}</div>',
        unsafe_allow_html=True
    )


def configurar_grafico(fig, altura=350):
    fig.update_layout(
        height=altura,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#FFFFFF",
        font=dict(family="Arial", color=TEXT, size=12),
        margin=dict(l=20, r=20, t=55, b=25),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="left",
            x=0
        ),
        hoverlabel=dict(
            bgcolor="white",
            font_size=13
        )
    )
    return fig


def grafico_barras(df, x, y, color=None, titulo="", formato=None):
    fig = px.bar(
        df,
        x=x,
        y=y,
        color=color,
        barmode="group",
        text_auto=".2s",
        title=titulo,
        color_discrete_sequence=PALETTE
    )
    fig.update_traces(
        textposition="outside",
        cliponaxis=False
    )
    fig.update_layout(
        yaxis_title="Quetzales (Q)",
        xaxis_title=""
    )
    if formato:
        fig.update_yaxes(tickformat=formato)
    return configurar_grafico(fig)


def mostrar_tabla(df, formatos=None):
    formato = formatos or {}
    st.dataframe(
        df.style.format(formato),
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# 3. ENCABEZADO
# ============================================================
st.markdown(
    '<div class="main-title">🪟 LA CORTINA</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">'
    'FINANCIAL INTELLIGENCE · COSTOS · RENTABILIDAD · PLANIFICACIÓN'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# 4. CATÁLOGO DE PRODUCTOS
# ============================================================
catalogo = {
    "Blackout": {
        "descripcion": "Bloqueo térmico y de luz",
        "precio": 550.0,
        "mp": 180.0,
        "mod": 60.0
    },
    "Screen": {
        "descripcion": "Filtro solar y visibilidad",
        "precio": 450.0,
        "mp": 140.0,
        "mod": 60.0
    },
    "Translúcida": {
        "descripcion": "Paso de luz suave",
        "precio": 350.0,
        "mp": 95.0,
        "mod": 50.0
    },
    "Día y Noche": {
        "descripcion": "Función dual / cebra",
        "precio": 650.0,
        "mp": 220.0,
        "mod": 75.0
    }
}


# ============================================================
# 5. BARRA LATERAL: ESCENARIO ORIGINAL
# ============================================================
st.sidebar.markdown("## LA CORTINA")
st.sidebar.caption("Centro de control financiero")
st.sidebar.markdown("---")
st.sidebar.markdown("### 01 · Producto")

producto = st.sidebar.selectbox(
    "Línea de cortina",
    list(catalogo.keys())
)
base = catalogo[producto]

st.sidebar.caption(base["descripcion"])
st.sidebar.markdown("---")
st.sidebar.markdown("### 02 · Operaciones")

capacidad = st.sidebar.slider(
    "Capacidad normal (unidades)",
    100, 10000, 3000, step=100
)

produccion = st.sidebar.slider(
    "Producción real (unidades)",
    100, 10000, 2600, step=100
)

ventas = st.sidebar.slider(
    "Ventas reales (unidades)",
    100, 10000, 2400, step=100
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 03 · Costos unitarios")

precio = st.sidebar.slider(
    "Precio de venta (Q)",
    100.0, 2000.0, float(base["precio"]), step=25.0
)

mp = st.sidebar.slider(
    "Materia prima (Q/u.)",
    20.0, 1000.0, float(base["mp"]), step=5.0
)

mod = st.sidebar.slider(
    "Mano de obra (Q/u.)",
    10.0, 500.0, float(base["mod"]), step=5.0
)

gifv = st.sidebar.slider(
    "GIF variables (Q/u.)",
    5.0, 200.0, 20.0, step=2.0
)

gasto_venta = st.sidebar.slider(
    "Gastos de venta variables (Q/u.)",
    0.0, 200.0, 30.0, step=2.0
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 04 · Costos fijos")

gif_fijo = st.sidebar.slider(
    "GIF fijos mensuales (Q)",
    5000, 300000, 45000, step=5000
)

admin_fijo = st.sidebar.slider(
    "Administración fija (Q)",
    5000, 300000, 20000, step=5000
)


# ============================================================
# 6. MOTOR FINANCIERO ORIGINAL
# ============================================================
costo_variable_u = mp + mod + gifv
inventario_final = produccion - ventas

tasa_fija = gif_fijo / capacidad if capacidad > 0 else 0

variacion_capacidad = (capacidad - produccion) * tasa_fija

ingresos = ventas * precio
costo_variable_ventas = ventas * costo_variable_u
gif_fijo_ventas = ventas * tasa_fija
gastos_variables_venta = ventas * gasto_venta

margen_contribucion_u = precio - costo_variable_u - gasto_venta
margen_contribucion = ingresos - costo_variable_ventas - gastos_variables_venta

margen_pct = (
    margen_contribucion / ingresos * 100 if ingresos > 0 else 0
)

utilidad_directa = margen_contribucion - gif_fijo - admin_fijo

utilidad_absorbente = (
    ingresos
    - costo_variable_ventas
    - gif_fijo_ventas
    - variacion_capacidad
    - gastos_variables_venta
    - admin_fijo
)

diferencia_utilidades = utilidad_absorbente - utilidad_directa
efecto_inventario = inventario_final * tasa_fija

punto_equilibrio = (
    (gif_fijo + admin_fijo) / margen_contribucion_u
    if margen_contribucion_u > 0 else None
)

# ============================================================
# 7. NAVEGACIÓN
# ============================================================
tab1, tab2, tab3, tab4 = st.tabs([
    "📋  1. Datos",
    "⚙️  2. Motor de cálculo",
    "📊  3. Dashboard ejecutivo",
    "🎛️  4. Simulación What-If"
])


# ============================================================
# PESTAÑA 1: INPUT DE DATOS
# ============================================================
with tab1:

    titulo_seccion("Resumen del escenario operativo")

    st.caption(
        f"Producto seleccionado: {producto} · {base['descripcion']}"
    )

    k1, k2, k3, k4 = st.columns(4)

    with k1:
        tarjeta(
            "Precio de venta",
            moneda(precio),
            "Por unidad",
            BLUE
        )

    with k2:
        tarjeta(
            "Costo variable unitario",
            moneda(costo_variable_u),
            "Producción por unidad",
            CYAN
        )

    with k3:
        tarjeta(
            "Ingresos por ventas",
            moneda(ingresos),
            f"{ventas:,} unidades vendidas",
            GREEN
        )

    with k4:
        tarjeta(
            "Inventario final",
            f"{inventario_final:,} u.",
            "Producción menos ventas",
            ORANGE
        )

    st.markdown("---")
    titulo_seccion("Volumen de operación")

    df_volumen = pd.DataFrame({
        "Concepto": [
            "Capacidad normal",
            "Producción real",
            "Ventas reales"
        ],
        "Unidades": [capacidad, produccion, ventas]
    })

    df_volumen_largo = pd.DataFrame({
        "Indicador": [
            "Capacidad normal",
            "Producción real",
            "Ventas reales"
        ],
        "Unidades": [capacidad, produccion, ventas],
        "Tipo": ["Operación", "Operación", "Comercial"]
    })

    c1, c2 = st.columns([1.25, 1])

    with c1:
        fig = px.bar(
            df_volumen_largo,
            x="Indicador",
            y="Unidades",
            color="Indicador",
            text="Unidades",
            title="Capacidad vs. producción vs. ventas",
            color_discrete_sequence=[BLUE, CYAN, GREEN]
        )
        fig.update_traces(textposition="outside")
        fig.update_layout(showlegend=False, yaxis_title="Unidades")
        st.plotly_chart(
            configurar_grafico(fig),
            use_container_width=True
        )

    with c2:
        df_costos = pd.DataFrame({
            "Componente": [
                "Materia prima",
                "Mano de obra",
                "GIF variables",
                "Gastos de venta variables"
            ],
            "Costo unitario": [mp, mod, gifv, gasto_venta]
        })

        fig = px.pie(
            df_costos,
            names="Componente",
            values="Costo unitario",
            hole=0.60,
            title="Composición de costos variables unitarios",
            color_discrete_sequence=PALETTE
        )
        fig.update_traces(
            textposition="inside",
            textinfo="percent"
        )
        st.plotly_chart(
            configurar_grafico(fig),
            use_container_width=True
        )

    st.markdown("---")
    titulo_seccion("Ficha de parámetros")

    df_parametros = pd.DataFrame({
        "Categoría": [
            "Comercial", "Comercial",
            "Producción", "Producción", "Producción",
            "Costos fijos", "Costos fijos"
        ],
        "Parámetro": [
            "Precio de venta unitario",
            "Unidades vendidas",
            "Capacidad normal",
            "Producción real",
            "Costo variable de producción unitario",
            "GIF fijos mensuales",
            "Gastos administrativos fijos"
        ],
        "Valor": [
            moneda(precio),
            f"{ventas:,} unidades",
            f"{capacidad:,} unidades",
            f"{produccion:,} unidades",
            moneda(costo_variable_u),
            moneda(gif_fijo),
            moneda(admin_fijo)
        ]
    })

    st.dataframe(
        df_parametros,
        use_container_width=True,
        hide_index=True
    )

    if inventario_final < 0:
        st.warning(
            "Las ventas superan la producción. Si no existe inventario "
            "inicial, revisa estos volúmenes antes de interpretar "
            "los resultados."
        )


# ============================================================
# PESTAÑA 2: MOTOR DE CÁLCULO
# ============================================================
with tab2:

    titulo_seccion("Motor de cálculo y análisis contable")

    tasa_col, variacion_col, margen_col = st.columns(3)

    with tasa_col:
        st.metric("Tasa de GIF fijo", moneda(tasa_fija) + "/u.")

    with variacion_col:
        st.metric(
            "Variación de capacidad",
            moneda(variacion_capacidad)
        )

    with margen_col:
        st.metric(
            "Margen de contribución unitario",
            moneda(margen_contribucion_u)
        )

    st.markdown("---")
    titulo_seccion("Comparación de métodos de costeo")

    df_metodos = pd.DataFrame({
        "Concepto": [
            "Ingresos por ventas",
            "Costos variables de producción",
            "GIF fijos aplicados a ventas",
            "Variación de capacidad",
            "Gastos variables de venta",
            "GIF fijos del período",
            "Gastos administrativos fijos",
            "Utilidad operativa"
        ],
        "Costeo absorbente": [
            ingresos,
            -costo_variable_ventas,
            -gif_fijo_ventas,
            -variacion_capacidad,
            -gastos_variables_venta,
            0,
            -admin_fijo,
            utilidad_absorbente
        ],
        "Costeo directo": [
            ingresos,
            -costo_variable_ventas,
            0,
            0,
            -gastos_variables_venta,
            -gif_fijo,
            -admin_fijo,
            utilidad_directa
        ]
    })

    df_metodos_grafico = pd.DataFrame({
        "Método": ["Costeo absorbente", "Costeo directo"],
        "Utilidad operativa": [
            utilidad_absorbente,
            utilidad_directa
        ]
    })

    c1, c2 = st.columns(2)

    with c1:
        fig = px.bar(
            df_metodos_grafico,
            x="Método",
            y="Utilidad operativa",
            color="Método",
            text="Utilidad operativa",
            title="Utilidad por método de costeo",
            color_discrete_sequence=[BLUE, CYAN]
        )
        fig.update_traces(
            texttemplate="Q%{y:,.0f}",
            textposition="outside"
        )
        fig.add_hline(y=0, line_dash="dash", line_color=RED)
        fig.update_layout(showlegend=False, yaxis_title="Quetzales (Q)")
        st.plotly_chart(
            configurar_grafico(fig),
            use_container_width=True
        )

    with c2:
        df_componentes = pd.DataFrame({
            "Componente": [
                "Producción variable",
                "GIF fijos",
                "Gastos de venta variables",
                "Administración fija"
            ],
            "Costo total": [
                costo_variable_ventas,
                gif_fijo,
                gastos_variables_venta,
                admin_fijo
            ]
        })

        fig = px.bar(
            df_componentes,
            x="Componente",
            y="Costo total",
            color="Componente",
            text="Costo total",
            title="Estructura de costos del período",
            color_discrete_sequence=PALETTE
        )
        fig.update_traces(
            texttemplate="Q%{y:,.0f}",
            textposition="outside"
        )
        fig.update_layout(
            showlegend=False,
            yaxis_title="Quetzales (Q)"
        )
        st.plotly_chart(
            configurar_grafico(fig),
            use_container_width=True
        )

    st.markdown("---")
    titulo_seccion("Estado de resultados comparativo")

    mostrar_tabla(
        df_metodos,
        {
            "Costeo absorbente": "Q{:,.2f}",
            "Costeo directo": "Q{:,.2f}"
        }
    )

    st.markdown("---")
    titulo_seccion("Conciliación de utilidades")

    conciliacion = pd.DataFrame({
        "Indicador": [
            "Utilidad operativa absorbente",
            "Utilidad operativa directa",
            "Diferencia entre métodos",
            "Inventario final (unidades)",
            "Efecto teórico del inventario"
        ],
        "Valor": [
            moneda(utilidad_absorbente),
            moneda(utilidad_directa),
            moneda(diferencia_utilidades),
            f"{inventario_final:,} unidades",
            moneda(efecto_inventario)
        ]
    })

    st.dataframe(
        conciliacion,
        use_container_width=True,
        hide_index=True
    )

    st.caption(
        "El tratamiento de las variaciones de capacidad depende de la "
        "metodología contable utilizada. Revisa la política de aplicación "
        "de GIF fijos antes de presentar estos valores como cifras definitivas."
    )


# ============================================================
# PESTAÑA 3: DASHBOARD EJECUTIVO
# ============================================================
with tab3:

    titulo_seccion("Dashboard ejecutivo")

    st.caption(
        f"Resumen de desempeño financiero · Línea {producto}"
    )

    d1, d2, d3, d4 = st.columns(4)

    with d1:
        tarjeta(
            "Ingresos",
            moneda(ingresos),
            "Ventas facturadas estimadas",
            BLUE
        )

    with d2:
        tarjeta(
            "Margen de contribución",
            moneda(margen_contribucion),
            f"{margen_pct:.1f}% de ingresos",
            CYAN
        )

    with d3:
        tarjeta(
            "Utilidad directa",
            moneda(utilidad_directa),
            "Antes de otros conceptos no incluidos",
            GREEN if utilidad_directa >= 0 else RED
        )

    with d4:
        tarjeta(
            "Utilidad absorbente",
            moneda(utilidad_absorbente),
            "Según los supuestos del modelo",
            PURPLE if utilidad_absorbente >= 0 else RED
        )

    st.markdown("---")
    titulo_seccion("Desempeño financiero")

    c1, c2 = st.columns(2)

    with c1:
        df_ventas_costos = pd.DataFrame({
            "Concepto": [
                "Ingresos",
                "Costo variable de producción vendido",
                "Gastos variables de venta",
                "GIF fijos",
                "Gastos administrativos"
            ],
            "Valor": [
                ingresos,
                costo_variable_ventas,
                gastos_variables_venta,
                gif_fijo,
                admin_fijo
            ]
        })

        fig = px.bar(
            df_ventas_costos,
            x="Concepto",
            y="Valor",
            color="Concepto",
            text="Valor",
            title="Ingresos y componentes principales",
            color_discrete_sequence=PALETTE
        )
        fig.update_traces(
            texttemplate="Q%{y:,.0f}",
            textposition="outside"
        )
        fig.update_layout(
            showlegend=False,
            yaxis_title="Quetzales (Q)"
        )
        st.plotly_chart(
            configurar_grafico(fig),
            use_container_width=True
        )

    with c2:
        df_utilidades = pd.DataFrame({
            "Método": ["Costeo absorbente", "Costeo directo"],
            "Utilidad": [utilidad_absorbente, utilidad_directa]
        })

        fig = px.bar(
            df_utilidades,
            x="Método",
            y="Utilidad",
            color="Método",
            text="Utilidad",
            title="Rentabilidad operativa",
            color_discrete_sequence=[PURPLE, GREEN]
        )
        fig.update_traces(
            texttemplate="Q%{y:,.0f}",
            textposition="outside"
        )
        fig.add_hline(y=0, line_dash="dash", line_color=RED)
        fig.update_layout(
            showlegend=False,
            yaxis_title="Quetzales (Q)"
        )
        st.plotly_chart(
            configurar_grafico(fig),
            use_container_width=True
        )

    st.markdown("---")
    titulo_seccion("Indicadores operativos")

    o1, o2, o3 = st.columns(3)

    with o1:
        utilizacion = produccion / capacidad * 100 if capacidad else 0
        st.metric(
            "Utilización de capacidad",
            f"{utilizacion:.1f}%"
        )
        st.progress(min(max(utilizacion / 100, 0.0), 1.0))

    with o2:
        ventas_produccion = ventas / produccion * 100 if produccion else 0
        st.metric(
            "Ventas respecto a producción",
            f"{ventas_produccion:.1f}%"
        )
        st.progress(
            min(max(ventas_produccion / 100, 0.0), 1.0)
        )

    with o3:
        st.metric(
            "Unidades en inventario final",
            f"{inventario_final:,}"
        )

    st.markdown("---")
    titulo_seccion("Punto de equilibrio")

    if punto_equilibrio is not None:
        pe_col1, pe_col2 = st.columns(2)

        with pe_col1:
            st.metric(
                "Unidades estimadas para equilibrio",
                f"{punto_equilibrio:,.0f}"
            )

        with pe_col2:
            st.metric(
                "Ventas de equilibrio",
                moneda(punto_equilibrio * precio)
            )

        if ventas >= punto_equilibrio:
            st.success(
                "Las ventas actuales alcanzan o superan el punto "
                "de equilibrio estimado."
            )
        else:
            st.warning(
                "Las ventas actuales están por debajo del punto "
                "de equilibrio estimado."
            )
    else:
        st.warning(
            "No es posible calcular el punto de equilibrio porque "
            "el margen de contribución unitario no es positivo."
        )


# ============================================================
# PESTAÑA 4: SIMULACIÓN WHAT-IF
# ============================================================
with tab4:

    titulo_seccion("Simulador de escenarios What-If")

    st.write(
        "Cambia las variables para evaluar cómo podrían cambiar "
        "las ventas, los costos y la utilidad. Este escenario es "
        "independiente de los datos originales."
    )

    st.markdown("---")
    titulo_seccion("Parámetros del escenario alternativo")

    with st.form("formulario_what_if"):

        c1, c2, c3 = st.columns(3)

        with c1:
            precio_sim = st.number_input(
                "Precio unitario (Q)",
                min_value=0.0,
                value=float(precio),
                step=10.0
            )

            ventas_sim = st.number_input(
                "Unidades vendidas",
                min_value=0,
                max_value=100000,
                value=int(ventas),
                step=100
            )

            capacidad_sim = st.number_input(
                "Capacidad normal (unidades)",
                min_value=1,
                max_value=100000,
                value=int(capacidad),
                step=100
            )

        with c2:
            mp_sim = st.number_input(
                "Materia prima por unidad (Q)",
                min_value=0.0,
                value=float(mp),
                step=5.0
            )

            mod_sim = st.number_input(
                "Mano de obra por unidad (Q)",
                min_value=0.0,
                value=float(mod),
                step=5.0
            )

            gifv_sim = st.number_input(
                "GIF variables por unidad (Q)",
                min_value=0.0,
                value=float(gifv),
                step=5.0
            )

        with c3:
            gasto_venta_sim = st.number_input(
                "Gasto variable de venta por unidad (Q)",
                min_value=0.0,
                value=float(gasto_venta),
                step=5.0
            )

            produccion_sim = st.number_input(
                "Producción simulada",
                min_value=0,
                max_value=100000,
                value=int(produccion),
                step=100
            )

            gif_fijo_sim = st.number_input(
                "GIF fijos totales (Q)",
                min_value=0.0,
                value=float(gif_fijo),
                step=5000.0
            )

        admin_sim = st.number_input(
            "Gastos administrativos fijos (Q)",
            min_value=0.0,
            value=float(admin_fijo),
            step=5000.0
        )

        ejecutar_simulacion = st.form_submit_button(
            "🚀 Calcular escenario",
            use_container_width=True,
            type="primary"
        )

    # Los valores del formulario se recalculan al enviarlo.
    # En el primer ingreso se usan los valores actuales.
    if ejecutar_simulacion or "what_if_iniciado" not in st.session_state:
        st.session_state["what_if_iniciado"] = True

        st.session_state["what_if_resultados"] = {
            "precio": precio_sim,
            "ventas": ventas_sim,
            "capacidad": capacidad_sim,
            "produccion": produccion_sim,
            "mp": mp_sim,
            "mod": mod_sim,
            "gifv": gifv_sim,
            "gasto_venta": gasto_venta_sim,
            "gif_fijo": gif_fijo_sim,
            "admin": admin_sim
        }

    # Evita perder el último escenario confirmado si se vuelve a ejecutar
    # la aplicación por cambios en otras variables.
    sim = st.session_state.get("what_if_resultados", {
        "precio": precio,
        "ventas": ventas,
        "capacidad": capacidad,
        "produccion": produccion,
        "mp": mp,
        "mod": mod,
        "gifv": gifv,
        "gasto_venta": gasto_venta,
        "gif_fijo": gif_fijo,
        "admin": admin_fijo
    })

    # ------------------------------------------------------------
    # CÁLCULO DEL ESCENARIO SIMULADO
    # ------------------------------------------------------------
    precio_s = sim["precio"]
    ventas_s = sim["ventas"]
    capacidad_s = sim["capacidad"]
    produccion_s = sim["produccion"]
    mp_s = sim["mp"]
    mod_s = sim["mod"]
    gifv_s = sim["gifv"]
    gasto_venta_s = sim["gasto_venta"]
    gif_fijo_s = sim["gif_fijo"]
    admin_s = sim["admin"]

    costo_variable_u_s = mp_s + mod_s + gifv_s
    ingresos_s = precio_s * ventas_s
    costo_variable_ventas_s = costo_variable_u_s * ventas_s
    gastos_variables_venta_s = gasto_venta_s * ventas_s

    margen_unitario_s = precio_s - costo_variable_u_s - gasto_venta_s

    margen_s = (
        ingresos_s
        - costo_variable_ventas_s
        - gastos_variables_venta_s
    )

    margen_pct_s = margen_s / ingresos_s * 100 if ingresos_s > 0 else 0

    tasa_fija_s = gif_fijo_s / capacidad_s if capacidad_s > 0 else 0
    gif_aplicado_s = ventas_s * tasa_fija_s
    variacion_s = (capacidad_s - produccion_s) * tasa_fija_s

    utilidad_directa_s = margen_s - gif_fijo_s - admin_s

    utilidad_absorbente_s = (
        ingresos_s
        - costo_variable_ventas_s
        - gif_aplicado_s
        - variacion_s
        - gastos_variables_venta_s
        - admin_s
    )

    pe_s = (
        (gif_fijo_s + admin_s) / margen_unitario_s
        if margen_unitario_s > 0 else None
    )

    # ------------------------------------------------------------
    # KPI SIMULADOS
    # ------------------------------------------------------------
    st.markdown("---")
    titulo_seccion("Resultados del escenario")

    s1, s2, s3, s4 = st.columns(4)

    with s1:
        tarjeta(
            "Ingresos simulados",
            moneda(ingresos_s),
            f"{ventas_s:,} unidades vendidas",
            BLUE
        )

    with s2:
        tarjeta(
            "Margen de contribución",
            moneda(margen_s),
            f"{margen_pct_s:.1f}% sobre ventas",
            CYAN
        )

    with s3:
        tarjeta(
            "Utilidad directa",
            moneda(utilidad_directa_s),
            "Costeo directo",
            GREEN if utilidad_directa_s >= 0 else RED
        )

    with s4:
        tarjeta(
            "Utilidad absorbente",
            moneda(utilidad_absorbente_s),
            "Costeo absorbente",
            PURPLE if utilidad_absorbente_s >= 0 else RED
        )

    # ------------------------------------------------------------
    # COMPARACIÓN VISUAL
    # ------------------------------------------------------------
    st.markdown("---")
    titulo_seccion("Escenario original frente al simulado")

    df_comparacion = pd.DataFrame({
        "Indicador": [
            "Ingresos",
            "Margen de contribución",
            "Utilidad directa",
            "Utilidad absorbente"
        ],
        "Original": [
            ingresos,
            margen_contribucion,
            utilidad_directa,
            utilidad_absorbente
        ],
        "Simulado": [
            ingresos_s,
            margen_s,
            utilidad_directa_s,
            utilidad_absorbente_s
        ]
    })

    df_comparacion_largo = df_comparacion.melt(
        id_vars="Indicador",
        var_name="Escenario",
        value_name="Quetzales"
    )

    fig = px.bar(
        df_comparacion_largo,
        x="Indicador",
        y="Quetzales",
        color="Escenario",
        barmode="group",
        text="Quetzales",
        title="Comparación financiera de escenarios",
        color_discrete_map={
            "Original": BLUE,
            "Simulado": ORANGE
        }
    )

    fig.update_traces(
        texttemplate="Q%{y:,.0f}",
        textposition="outside"
    )
    fig.add_hline(y=0, line_dash="dash", line_color=RED)
    fig.update_layout(yaxis_title="Quetzales (Q)")
    st.plotly_chart(
        configurar_grafico(fig, 420),
        use_container_width=True
    )

    # ------------------------------------------------------------
    # SENSIBILIDAD DEL PRECIO
    # ------------------------------------------------------------
    st.markdown("---")
    titulo_seccion("Sensibilidad de utilidad ante cambios de precio")

    precios_sensibilidad = [
        max(0.0, precio_s * factor)
        for factor in [0.80, 0.90, 1.00, 1.10, 1.20]
    ]

    df_sensibilidad = pd.DataFrame({
        "Precio unitario": precios_sensibilidad
    })

    df_sensibilidad["Ingresos"] = (
        df_sensibilidad["Precio unitario"] * ventas_s
    )

    df_sensibilidad["Utilidad directa"] = (
        df_sensibilidad["Ingresos"]
        - costo_variable_ventas_s
        - gastos_variables_venta_s
        - gif_fijo_s
        - admin_s
    )

    fig = px.line(
        df_sensibilidad,
        x="Precio unitario",
        y="Utilidad directa",
        markers=True,
        title="Impacto de variaciones de precio en la utilidad directa",
        color_discrete_sequence=[PURPLE]
    )

    fig.update_traces(
        line=dict(width=3),
        marker=dict(size=9)
    )
    fig.add_hline(y=0, line_dash="dash", line_color=RED)
    fig.update_layout(
        xaxis_title="Precio de venta unitario (Q)",
        yaxis_title="Utilidad directa (Q)"
    )
    st.plotly_chart(
        configurar_grafico(fig),
        use_container_width=True
    )

    # ------------------------------------------------------------
    # PUNTO DE EQUILIBRIO
    # ------------------------------------------------------------
    st.markdown("---")
    titulo_seccion("Punto de equilibrio del escenario simulado")

    pe1, pe2, pe3 = st.columns(3)

    with pe1:
        tarjeta(
            "Margen unitario",
            moneda(margen_unitario_s),
            "Precio menos costos variables",
            CYAN
        )

    with pe2:
        tarjeta(
            "Punto de equilibrio",
            f"{pe_s:,.0f} u." if pe_s is not None else "No calculable",
            "Unidades para cubrir costos fijos",
            ORANGE
        )

    with pe3:
        tarjeta(
            "Variación de capacidad",
            moneda(variacion_s),
            "Según capacidad normal y producción",
            PURPLE
        )

    if pe_s is not None:
        limite = max(
            ventas_s * 1.25,
            pe_s * 1.25,
            100
        )

        x_unidades = sorted(set([
            0,
            int(min(limite, 100000)),
            int(min(pe_s, 100000)),
            int(min(ventas_s, 100000))
        ]))

        x_unidades = [x for x in x_unidades if x >= 0]

        df_pe = pd.DataFrame({"Unidades": x_unidades})

        df_pe["Ingresos"] = df_pe["Unidades"] * precio_s

        df_pe["Costos totales"] = (
            df_pe["Unidades"] * (costo_variable_u_s + gasto_venta_s)
            + gif_fijo_s
            + admin_s
        )

        fig = go.Figure()

        fig.add_trace(go.Scatter(
            x=df_pe["Unidades"],
            y=df_pe["Ingresos"],
            mode="lines+markers",
            name="Ingresos",
            line=dict(color=GREEN, width=3)
        ))

        fig.add_trace(go.Scatter(
            x=df_pe["Unidades"],
            y=df_pe["Costos totales"],
            mode="lines+markers",
            name="Costos totales",
            line=dict(color=RED, width=3)
        ))

        fig.add_vline(
            x=pe_s,
            line_dash="dash",
            line_color=ORANGE,
            annotation_text=f"Equilibrio: {pe_s:,.0f} u."
        )

        fig.update_layout(
            title="Ingresos frente a costos totales",
            xaxis_title="Unidades vendidas",
            yaxis_title="Quetzales (Q)"
        )

        st.plotly_chart(
            configurar_grafico(fig, 420),
            use_container_width=True
        )

    else:
        st.warning(
            "El punto de equilibrio no puede calcularse porque el "
            "margen de contribución unitario es cero o negativo."
        )

    # ------------------------------------------------------------
    # ESTADO DE RESULTADOS SIMULADO
    # ------------------------------------------------------------
    st.markdown("---")
    titulo_seccion("Estado de resultados simulado")

    df_estado_s = pd.DataFrame({
        "Concepto": [
            "Ingresos por ventas",
            "(-) Costos variables de producción",
            "(=) Margen después de producción variable",
            "(-) Gastos variables de venta",
            "(=) Margen de contribución",
            "(-) GIF fijos del período",
            "(-) Gastos administrativos fijos",
            "(=) Utilidad operativa directa",
            "(-) GIF fijos aplicados a ventas",
            "(-) Variación de capacidad",
            "(=) Utilidad operativa absorbente"
        ],
        "Valor (Q)": [
            ingresos_s,
            -costo_variable_ventas_s,
            ingresos_s - costo_variable_ventas_s,
            -gastos_variables_venta_s,
            margen_s,
            -gif_fijo_s,
            -admin_s,
            utilidad_directa_s,
            -gif_aplicado_s,
            -variacion_s,
            utilidad_absorbente_s
        ]
    })

    mostrar_tabla(
        df_estado_s,
        {"Valor (Q)": "Q{:,.2f}"}
    )

    st.caption(
        "La sensibilidad de precio mantiene constantes los volúmenes "
        "y los costos unitarios. No representa una predicción de demanda. "
        "La simulación es analítica y no registra operaciones contables."
    )


# ============================================================
# 8. PIE DE PÁGINA
# ============================================================
st.markdown("---")
st.markdown(
    '<div class="footer">'
    'LA CORTINA · SISTEMA DE DIAGNÓSTICO Y PLANIFICACIÓN DE COSTOS'
    '<br>Modelo de análisis gerencial · Cifras expresadas en quetzales (Q)'
    '</div>',
    unsafe_allow_html=True
)
