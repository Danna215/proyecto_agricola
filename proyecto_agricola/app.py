# app.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# --- Configuración de la Página ---
st.set_page_config(
    page_title="Análisis Agrícola Interactivo",
    page_icon="🌱",
    layout="wide"
)

# --- Carga de Datos ---
@st.cache_data
def load_data():
    df = pd.read_csv('Crop_recommendation.csv')
    return df

df = load_data()

# --- Barra Lateral ---
st.sidebar.title("Panel de Control")
st.sidebar.markdown("Selecciona el tipo de análisis que quieras visualizar.")

plot_type = st.sidebar.selectbox(
    "Selecciona un tipo de análisis:",
    [
        "Visión General del Dataset",
        "Distribución de una Variable",
        "Relación entre Dos Variables",
        "Correlación General"
    ]
)

# --- Cuerpo Principal ---
st.title("🌱 Panel de Análisis Exploratorio de Cultivos")
st.markdown("Esta aplicación permite explorar cómo las condiciones del suelo y el clima influyen en el cultivo recomendado.")

# --- Visión General ---
if plot_type == "Visión General del Dataset":
    st.header("1. Vistazo General a los Datos")
    st.dataframe(df.head())

    st.header("2. Resumen Estadístico")
    st.dataframe(df.describe())

    st.header("3. Metodología")
    st.markdown("""
    Esta sección explica el origen de los datos y los pasos seguidos:
    * **Origen de los Datos:** Dataset obtenido de Kaggle con 2200 registros de condiciones de suelo y clima para 22 cultivos.
    * **Variables Principales:** Nitrógeno (N), Fósforo (P), Potasio (K), temperatura, humedad, pH, lluvia y el cultivo (label).
    * **Limpieza de Datos:** Se revisaron valores nulos y tipos de datos; el dataset ya estaba limpio y no requirió imputaciones.
    """)

# --- Distribución de una Variable ---
elif plot_type == "Distribución de una Variable":
    st.header("Análisis de Distribución")

    numeric_vars = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    selected_var = st.sidebar.selectbox("Selecciona una variable numérica:", numeric_vars)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader(f"Histograma de {selected_var}")
        fig, ax = plt.subplots()
        sns.histplot(df[selected_var], kde=True, ax=ax, color="green")
        st.pyplot(fig)

    with col2:
        st.subheader(f"Boxplot de {selected_var}")
        fig, ax = plt.subplots()
        sns.boxplot(y=df[selected_var], ax=ax, color="lightblue")
        st.pyplot(fig)

# --- Relación entre Dos Variables ---
elif plot_type == "Relación entre Dos Variables":
    st.header("Análisis Bivariado")

    numeric_vars = df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    x_var = st.sidebar.selectbox("Selecciona la variable para el eje X:", numeric_vars, index=0)
    y_var = st.sidebar.selectbox("Selecciona la variable para el eje Y:", numeric_vars, index=1)

    st.subheader(f"Dispersión: {x_var} vs. {y_var}")
    fig, ax = plt.subplots()
    sns.regplot(x=x_var, y=y_var, data=df, ax=ax, scatter_kws={'alpha':0.5}, line_kws={"color": "red"})
    st.pyplot(fig)

    st.header("Visualización Avanzada (Puntos Extra)")
    st.markdown("Gráfico 3D interactivo con **Plotly** que muestra la relación entre N, P y K, coloreado por cultivo.")
    fig_plotly = px.scatter_3d(
        df, x='N', y='P', z='K', color='label',
        title="Relación 3D de Nutrientes (N, P, K) por Cultivo",
        height=600
    )
    st.plotly_chart(fig_plotly, use_container_width=True)

# --- Correlación General ---
elif plot_type == "Correlación General":
    st.header("Mapa de Calor de Correlación")

    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    st.pyplot(fig)
