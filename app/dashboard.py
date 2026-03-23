import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Dashboard Previne Brasil", layout="wide")

# Título
st.title(" Monitoramento de Indicadores - Previne Brasil")
st.markdown("Analise o desempenho da saúde básica por região e estado.")

def load_data():
    data_path = Path(__file__).resolve().parent.parent / 'data/bronze/ccmec25a64.csv'
    if not data_path.exists():
        st.error(f"Arquivo não encontrado: {data_path}")
        return pd.DataFrame()

    df = pd.read_csv(data_path)
    expected_columns = [
        'dt_competencia', 'no_regiao_brasil', 'sg_uf', 'no_municipio',
        'vl_indicador_calculado_mun', 'vl_indicador_calculado_br'
    ]
    missing = [c for c in expected_columns if c not in df.columns]
    if missing:
        st.error(f"Colunas ausentes no CSV: {missing}")
        return pd.DataFrame()

    df['dt_competencia'] = pd.to_datetime(df['dt_competencia'], errors='coerce')
    df = df.dropna(subset=['dt_competencia', 'vl_indicador_calculado_mun', 'vl_indicador_calculado_br'])

    return df


df = load_data()
if df.empty:
    st.stop()

st.sidebar.header("Filtros de Pesquisa")
regiao = st.sidebar.multiselect(
    "Selecione a Região:",
    options=sorted(df["no_regiao_brasil"].dropna().unique()),
    default=sorted(df["no_regiao_brasil"].dropna().unique())
)

df_filtrado = df[df["no_regiao_brasil"].isin(regiao)]
estados = st.sidebar.multiselect(
    "Selecione o Estado (UF):",
    options=sorted(df_filtrado["sg_uf"].dropna().unique()),
    default=sorted(df_filtrado["sg_uf"].dropna().unique())
)

df_final = df_filtrado[df_filtrado["sg_uf"].isin(estados)]

if df_final.empty:
    st.warning("Nenhum registro encontrado para os filtros selecionados. Ajuste os filtros e tente novamente.")


latest_date = df['dt_competencia'].max()
latest_df = df[df['dt_competencia'] == latest_date]

media_nacional = latest_df['vl_indicador_calculado_br'].mean() if not latest_df.empty else 0
municipios_analisados = df_final['no_municipio'].nunique() if not df_final.empty else 0
maior_valor = df_final['vl_indicador_calculado_mun'].max() if not df_final.empty else 0

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Média Nacional (Mês Atual)", f"{media_nacional:,.2f}")
with m2:
    st.metric("Municípios Analisados", municipios_analisados)
with m3:
    st.metric("Maior Valor na Seleção", f"{maior_valor:,.2f}")


col1, col2 = st.columns(2)

with col1:
    st.subheader("Evolução Temporal")
    time_data = (
        df_final.groupby('dt_competencia')['vl_indicador_calculado_mun']
        .mean()
        .reset_index()
    )
    fig_time = px.line(
        time_data,
        x='dt_competencia',
        y='vl_indicador_calculado_mun',
        title="Média do Indicador no Tempo (Seleção)"
    )
    st.plotly_chart(fig_time, width='stretch')

with col2:
    st.subheader("Distribuição por UF")
    fig_bar = px.box(
        df_final,
        x='sg_uf',
        y='vl_indicador_calculado_mun',
        color='sg_uf',
        title="Variabilidade dos Municípios por Estado"
    )
    st.plotly_chart(fig_bar, width='stretch')


st.subheader("Visualização dos Dados Filtrados")
show_table = df_final if not df_final.empty else df.head(100)
st.dataframe(show_table[['dt_competencia', 'no_municipio', 'sg_uf', 'vl_indicador_calculado_mun']].head(100))