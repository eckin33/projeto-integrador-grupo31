import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
from pathlib import Path

# ── configuração da página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Tecnologia & Saúde Mental",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── tema / CSS ───────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
        /* Fundo geral */
        .stApp { background-color: #0D0D0D; }

        /* Cabeçalho */
        .main-title {
            font-size: 2.2rem;
            font-weight: 700;
            color: #818CF8;
            margin-bottom: 0.2rem;
        }
        .subtitle {
            font-size: 1rem;
            color: #6B7280;
            margin-bottom: 1.5rem;
        }

        /* KPI cards */
        .kpi-card {
            background: #141414;
            border-left: 4px solid #6366F1;
            border-radius: 8px;
            padding: 1rem 1.2rem;
        }
        .kpi-value { font-size: 1.8rem; font-weight: 700; color: #F9FAFB; }
        .kpi-label { font-size: 0.8rem; color: #6B7280; text-transform: uppercase; }

        /* Títulos de seção */
        .section-title {
            font-size: 1.15rem;
            font-weight: 600;
            color: #A5B4FC;
            margin-top: 1.5rem;
            margin-bottom: 0.5rem;
        }

        /* Sidebar */
        [data-testid="stSidebar"] { background: #000000; }
        [data-testid="stSidebar"] * { color: #E5E7EB; }
        [data-testid="stSidebar"] h3 { color: #818CF8; }
        [data-testid="stSidebar"] hr { border-color: #1F2937; }

        /* Divisores */
        hr { border-color: #1F2937; }

        /* Texto geral */
        p, label, .stCaption { color: #9CA3AF; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── carrega dados ────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent.parent
DATA_PATH = BASE_DIR / "data" / "base_tratada.csv"


@st.cache_data
def load_data() -> pd.DataFrame:
    df = pd.read_csv(DATA_PATH, encoding="utf-8")
    df.columns = df.columns.str.strip()
    df["Faixa_Etaria"] = df["Faixa_Etaria"].fillna("Não informado")
    return df


df_full = load_data()

# ── paletas ──────────────────────────────────────────────────────────────────
STATUS_COLORS = {
    "Excelente": "#22C55E",
    "Bom": "#84CC16",
    "Regular": "#F59E0B",
    "Ruim": "#EF4444",
}
STRESS_COLORS = {
    "Baixo": "#22C55E",
    "Médio": "#F59E0B",
    "Alto": "#EF4444",
}
FAIXAS_ORDER = ["18-25", "26-40", "41-60", "60+"]

# cores de destaque para radar / faixas etárias
ACCENT_COLORS = ["#818CF8", "#34D399", "#FBBF24", "#F87171"]

# layout base aplicado a todos os gráficos Plotly
CHART_LAYOUT = dict(
    paper_bgcolor="#141414",
    plot_bgcolor="#141414",
    font=dict(color="#E5E7EB", family="sans-serif"),
    title_font=dict(color="#A5B4FC", size=14),
    legend=dict(bgcolor="#1F2937", bordercolor="#374151", borderwidth=1),
    xaxis=dict(gridcolor="#1F2937", zerolinecolor="#374151", color="#9CA3AF"),
    yaxis=dict(gridcolor="#1F2937", zerolinecolor="#374151", color="#9CA3AF"),
)


def apply_theme(fig, **extra):
    """Aplica CHART_LAYOUT + qualquer override extra ao figura."""
    fig.update_layout(**{**CHART_LAYOUT, **extra})
    return fig

# ── sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 🔎 Filtros")

    generos = ["Todos"] + sorted(df_full["Gênero"].dropna().unique().tolist())
    genero_sel = st.selectbox("Gênero", generos)

    faixas = ["Todas"] + [f for f in FAIXAS_ORDER if f in df_full["Faixa_Etaria"].unique()]
    faixa_sel = st.selectbox("Faixa Etária", faixas)

    status_opts = sorted(df_full["Status de Saúde Mental"].dropna().unique().tolist())
    status_sel = st.multiselect("Status de Saúde Mental", status_opts, default=status_opts)

    st.markdown("---")
    st.markdown("**Horas de Tela**")
    tela_min, tela_max = float(df_full["Horas de Tempo na Tela"].min()), float(df_full["Horas de Tempo na Tela"].max())
    tela_range = st.slider("", tela_min, tela_max, (tela_min, tela_max), step=0.5)

    st.markdown("---")
    st.caption("Fonte: Kaggle — Mental Health & Technology Usage Dataset")

# ── filtragem ────────────────────────────────────────────────────────────────
df = df_full.copy()
if genero_sel != "Todos":
    df = df[df["Gênero"] == genero_sel]
if faixa_sel != "Todas":
    df = df[df["Faixa_Etaria"] == faixa_sel]
if status_sel:
    df = df[df["Status de Saúde Mental"].isin(status_sel)]
df = df[df["Horas de Tempo na Tela"].between(*tela_range)]

# ── cabeçalho ────────────────────────────────────────────────────────────────
st.markdown('<p class="main-title">🧠 Tecnologia & Saúde Mental</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Análise do impacto do uso de tecnologia e redes sociais no bem-estar psicológico</p>',
    unsafe_allow_html=True,
)

if df.empty:
    st.warning("Nenhum registro corresponde aos filtros selecionados.")
    st.stop()

# ── KPIs ─────────────────────────────────────────────────────────────────────
total = len(df)
media_sono = df["Horas de Sono"].mean()
media_tela = df["Horas de Tempo na Tela"].mean()
pct_alerta = (df["Alerta_Saude"] == "Sim").mean() * 100
media_stress = df["Estresse_Score"].mean()

col1, col2, col3, col4, col5 = st.columns(5)
for col, val, label in [
    (col1, f"{total:,}", "Participantes"),
    (col2, f"{media_tela:.1f}h", "Tela / dia (média)"),
    (col3, f"{media_sono:.1f}h", "Sono / dia (média)"),
    (col4, f"{media_stress:.1f}/3", "Estresse Médio"),
    (col5, f"{pct_alerta:.1f}%", "Em Alerta de Saúde"),
]:
    col.markdown(
        f'<div class="kpi-card"><div class="kpi-value">{val}</div>'
        f'<div class="kpi-label">{label}</div></div>',
        unsafe_allow_html=True,
    )

st.markdown("---")

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 1 — Distribuição geral
# ════════════════════════════════════════════════════════════════════════════
st.markdown('<p class="section-title">📊 Distribuição & Perfil</p>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

# Donut — Status de Saúde Mental
with c1:
    counts = df["Status de Saúde Mental"].value_counts().reset_index()
    counts.columns = ["Status", "Qtd"]
    fig = px.pie(
        counts,
        names="Status",
        values="Qtd",
        hole=0.55,
        color="Status",
        color_discrete_map=STATUS_COLORS,
        title="Status de Saúde Mental",
    )
    fig.update_traces(textposition="outside", textinfo="percent+label")
    apply_theme(fig, showlegend=False, margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Barras — Nível de Estresse
with c2:
    stress_counts = df["Nivel_Estresse"].value_counts().reindex(["Baixo", "Médio", "Alto"]).reset_index()
    stress_counts.columns = ["Nível", "Qtd"]
    fig = px.bar(
        stress_counts,
        x="Nível",
        y="Qtd",
        color="Nível",
        color_discrete_map=STRESS_COLORS,
        title="Nível de Estresse",
        text="Qtd",
    )
    fig.update_traces(textposition="outside")
    apply_theme(fig, showlegend=False, yaxis_title="", xaxis_title="", margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Barras — Faixa Etária
with c3:
    faixa_counts = (
        df["Faixa_Etaria"]
        .value_counts()
        .reindex([f for f in FAIXAS_ORDER if f in df["Faixa_Etaria"].unique()])
        .reset_index()
    )
    faixa_counts.columns = ["Faixa", "Qtd"]
    fig = px.bar(
        faixa_counts,
        x="Faixa",
        y="Qtd",
        color="Faixa",
        title="Distribuição por Faixa Etária",
        text="Qtd",
    )
    fig.update_traces(textposition="outside")
    apply_theme(fig, showlegend=False, yaxis_title="", xaxis_title="", margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 2 — Impacto no Sono
# ════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<p class="section-title">😴 Impacto no Descanso</p>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

# Scatter — Tela vs Sono
with c1:
    fig = px.scatter(
        df,
        x="Horas de Tempo na Tela",
        y="Horas de Sono",
        color="Status de Saúde Mental",
        color_discrete_map=STATUS_COLORS,
        opacity=0.6,
        trendline="ols",
        trendline_scope="overall",
        trendline_color_override="#818CF8",
        title="Tempo de Tela × Horas de Sono",
        labels={
            "Horas de Tempo na Tela": "Horas de Tela/dia",
            "Horas de Sono": "Horas de Sono/dia",
        },
    )
    apply_theme(fig, margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Box — Sono por Status
with c2:
    status_order = ["Excelente", "Bom", "Regular", "Ruim"]
    fig = px.box(
        df,
        x="Status de Saúde Mental",
        y="Horas de Sono",
        color="Status de Saúde Mental",
        color_discrete_map=STATUS_COLORS,
        category_orders={"Status de Saúde Mental": status_order},
        title="Distribuição do Sono por Status de Saúde",
        points="outliers",
    )
    apply_theme(fig, showlegend=False, margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Sono médio por faixa etária e gênero
sono_faixa = (
    df.groupby(["Faixa_Etaria", "Gênero"])["Horas de Sono"]
    .mean()
    .reset_index()
    .rename(columns={"Horas de Sono": "Média de Sono"})
)
sono_faixa["Faixa_Etaria"] = pd.Categorical(sono_faixa["Faixa_Etaria"], categories=FAIXAS_ORDER, ordered=True)
sono_faixa = sono_faixa.sort_values("Faixa_Etaria")

fig = px.bar(
    sono_faixa,
    x="Faixa_Etaria",
    y="Média de Sono",
    color="Gênero",
    barmode="group",
    title="Média de Horas de Sono por Faixa Etária e Gênero",
    text_auto=".1f",
)
apply_theme(fig, margin=dict(t=40, b=10), xaxis_title="Faixa Etária", yaxis_title="Horas de Sono (média)")
st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 3 — Estresse & Redes Sociais
# ════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<p class="section-title">😰 Bem-Estar Emocional & Redes Sociais</p>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

# Scatter — Redes Sociais vs Estresse Score
with c1:
    fig = px.scatter(
        df,
        x="Horas de Uso de Redes Sociais",
        y="Estresse_Score",
        color="Nivel_Estresse",
        color_discrete_map=STRESS_COLORS,
        opacity=0.55,
        trendline="ols",
        trendline_scope="overall",
        trendline_color_override="#818CF8",
        title="Redes Sociais × Score de Estresse",
        labels={
            "Horas de Uso de Redes Sociais": "Horas em Redes Sociais/dia",
            "Estresse_Score": "Score de Estresse",
        },
    )
    apply_theme(fig, margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Violin — Redes Sociais por Nível de Estresse
with c2:
    fig = px.violin(
        df,
        x="Nivel_Estresse",
        y="Horas de Uso de Redes Sociais",
        color="Nivel_Estresse",
        color_discrete_map=STRESS_COLORS,
        box=True,
        points="outliers",
        category_orders={"Nivel_Estresse": ["Baixo", "Médio", "Alto"]},
        title="Distribuição do Uso de Redes Sociais por Nível de Estresse",
    )
    apply_theme(fig, showlegend=False, margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Heatmap — Média de Estresse por Faixa Etária × Status
pivot = df.pivot_table(
    index="Faixa_Etaria",
    columns="Status de Saúde Mental",
    values="Estresse_Score",
    aggfunc="mean",
)
pivot = pivot.reindex([f for f in FAIXAS_ORDER if f in pivot.index])
pivot = pivot.reindex(columns=[c for c in ["Excelente", "Bom", "Regular", "Ruim"] if c in pivot.columns])

fig = px.imshow(
    pivot,
    text_auto=".2f",
    color_continuous_scale="RdYlGn_r",
    title="Estresse Médio: Faixa Etária × Status de Saúde Mental",
    labels={"color": "Score Estresse"},
)
apply_theme(fig, margin=dict(t=40, b=10))
st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 4 — Comportamento Digital por Faixa Etária
# ════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<p class="section-title">👤 Comportamento Digital por Faixa Etária</p>', unsafe_allow_html=True)

cols_uso = [
    "Horas de Uso de Tecnologia",
    "Horas de Uso de Redes Sociais",
    "Horas de Jogos",
    "Horas de Tempo na Tela",
    "Horas de Atividade Física",
]
medias_faixa = (
    df.groupby("Faixa_Etaria")[cols_uso].mean().reset_index()
)
medias_faixa["Faixa_Etaria"] = pd.Categorical(medias_faixa["Faixa_Etaria"], categories=FAIXAS_ORDER, ordered=True)
medias_faixa = medias_faixa.sort_values("Faixa_Etaria")

medias_long = medias_faixa.melt(id_vars="Faixa_Etaria", var_name="Indicador", value_name="Média (h)")

fig = px.bar(
    medias_long,
    x="Faixa_Etaria",
    y="Média (h)",
    color="Indicador",
    barmode="group",
    title="Média de Horas por Atividade Digital e Faixa Etária",
    text_auto=".1f",
)
apply_theme(fig, margin=dict(t=40, b=10), xaxis_title="Faixa Etária")
st.plotly_chart(fig, use_container_width=True)

# Radar — perfil médio por faixa etária
radar_cols = ["Horas de Uso de Tecnologia", "Horas de Uso de Redes Sociais", "Horas de Jogos", "Horas de Sono", "Horas de Atividade Física"]
medias_faixa_radar = (
    df.groupby("Faixa_Etaria")[radar_cols].mean().reset_index()
)
medias_faixa_radar["Faixa_Etaria"] = pd.Categorical(
    medias_faixa_radar["Faixa_Etaria"], categories=FAIXAS_ORDER, ordered=True
)
medias_faixa_radar = medias_faixa_radar.sort_values("Faixa_Etaria")
fig_radar = go.Figure()
colors_radar = ACCENT_COLORS
for i, faixa in enumerate([f for f in FAIXAS_ORDER if f in medias_faixa_radar["Faixa_Etaria"].values]):
    row = medias_faixa_radar[medias_faixa_radar["Faixa_Etaria"] == faixa]
    if row.empty:
        continue
    vals = row[radar_cols].values.flatten().tolist()
    vals.append(vals[0])
    fig_radar.add_trace(
        go.Scatterpolar(
            r=vals,
            theta=radar_cols + [radar_cols[0]],
            fill="toself",
            name=faixa,
            line_color=colors_radar[i % len(colors_radar)],
            opacity=0.6,
        )
    )
apply_theme(
    fig_radar,
    polar=dict(
        bgcolor="#141414",
        radialaxis=dict(visible=True, gridcolor="#1F2937", color="#6B7280"),
        angularaxis=dict(gridcolor="#1F2937", color="#9CA3AF"),
    ),
    title="Perfil de Hábitos Digitais por Faixa Etária (Radar)",
    margin=dict(t=60, b=10),
)
st.plotly_chart(fig_radar, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 5 — Fatores de Proteção
# ════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<p class="section-title">🛡️ Fatores de Proteção & Ambiente</p>', unsafe_allow_html=True)

c1, c2 = st.columns(2)

# Atividade Física vs Estresse
with c1:
    fig = px.scatter(
        df,
        x="Horas de Atividade Física",
        y="Estresse_Score",
        color="Status de Saúde Mental",
        color_discrete_map=STATUS_COLORS,
        opacity=0.55,
        trendline="ols",
        trendline_scope="overall",
        trendline_color_override="#34D399",
        title="Atividade Física × Score de Estresse",
    )
    apply_theme(fig, margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Ambiente de Trabalho × Status de Saúde
with c2:
    amb_status = (
        df.groupby(["Impacto do Ambiente de Trabalho", "Status de Saúde Mental"])
        .size()
        .reset_index(name="Qtd")
    )
    fig = px.bar(
        amb_status,
        x="Impacto do Ambiente de Trabalho",
        y="Qtd",
        color="Status de Saúde Mental",
        color_discrete_map=STATUS_COLORS,
        barmode="group",
        title="Ambiente de Trabalho × Status de Saúde Mental",
        text="Qtd",
    )
    apply_theme(fig, showlegend=True, margin=dict(t=40, b=10))
    st.plotly_chart(fig, use_container_width=True)

# Acesso a Suporte × Alerta de Saúde
suporte_alerta = (
    df.groupby(["Acesso a Sistemas de Suporte", "Alerta_Saude"])
    .size()
    .reset_index(name="Qtd")
)
fig = px.bar(
    suporte_alerta,
    x="Acesso a Sistemas de Suporte",
    y="Qtd",
    color="Alerta_Saude",
    barmode="group",
    title="Acesso a Sistemas de Suporte × Alerta de Saúde",
    color_discrete_map={"Sim": "#F87171", "Não": "#34D399"},
    text="Qtd",
)
apply_theme(fig, margin=dict(t=40, b=10), legend_title="Alerta de Saúde")
st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 6 — Correlação geral (heatmap)
# ════════════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown('<p class="section-title">🔗 Matriz de Correlação</p>', unsafe_allow_html=True)

num_cols = [
    "Idade",
    "Horas de Uso de Tecnologia",
    "Horas de Uso de Redes Sociais",
    "Horas de Jogos",
    "Horas de Tempo na Tela",
    "Horas de Sono",
    "Horas de Atividade Física",
    "Estresse_Score",
]
corr = df[num_cols].corr()
fig = px.imshow(
    corr,
    text_auto=".2f",
    color_continuous_scale="RdBu_r",
    zmin=-1,
    zmax=1,
    title="Correlação entre Variáveis Numéricas",
    aspect="auto",
)
apply_theme(fig, margin=dict(t=50, b=10))
st.plotly_chart(fig, use_container_width=True)

# ════════════════════════════════════════════════════════════════════════════
# SEÇÃO 7 — Tabela de dados
# ════════════════════════════════════════════════════════════════════════════
st.markdown("---")
with st.expander("📋 Ver dados filtrados", expanded=False):
    st.dataframe(df.reset_index(drop=True), use_container_width=True, height=350)
    st.caption(f"{len(df):,} registros exibidos após filtros.")
