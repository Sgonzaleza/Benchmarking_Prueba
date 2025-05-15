import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Benchmarking de Carreras Universitarias")
st.markdown("""
Este dashboard muestra comparaciones clave entre carreras similares de distintas universidades chilenas, 
basándose en indicadores como duración, acreditación, cantidad de docentes y antigüedad.
""")

# Carga de datos desde Excel
@st.cache_data
def cargar_datos():
    df = pd.read_excel("Información de las Carreras.xlsx")
    df.columns = df.columns.str.strip()
    df['Años Acreditación Num'] = df['Años de acreditación de la carrera'].apply(extraer_anios_acreditacion)
    return df.dropna(subset=['Universidad', 'Carrera'])

# Función para extraer años de acreditación
def extraer_anios_acreditacion(valor):
    if pd.isna(valor):
        return 0
    try:
        partes = str(valor).split("/")
        numero = ''.join(filter(str.isdigit, partes[0]))
        return int(numero) if numero else 0
    except:
        return 0

df = cargar_datos()

# Títulos para las visualizaciones
st.markdown("---")
st.subheader("📈 Duración de Carreras por Universidad")
fig1 = px.bar(df, x='Universidad', y='Años de duración', color='Carrera', barmode='group',
              title='Duración de Carreras por Universidad')
st.plotly_chart(fig1, use_container_width=True)

st.markdown("---")
st.subheader("👨‍🏫 Cantidad de Profesores por Universidad")
fig2 = px.bar(df, x='Universidad', y='Cantidad de profesores', color='Carrera', barmode='group',
              title='Cantidad de Profesores por Universidad')
st.plotly_chart(fig2, use_container_width=True)

st.markdown("---")
st.subheader("📜 Años de Acreditación por Universidad")
fig3 = px.bar(df, x='Universidad', y='Años Acreditación Num', color='Carrera', barmode='group',
              title='Años de Acreditación por Universidad')
st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")
st.subheader("🏛️ Año de Creación de la Carrera")
fig4 = px.bar(df, x='Universidad', y='Año de creación de la carrera', color='Carrera',
              title='Año de Creación de la Carrera por Universidad')
st.plotly_chart(fig4, use_container_width=True)

st.markdown("---")
st.subheader("📊 Distribución de Duración por Modalidad")
fig5 = px.box(df, x='Modalidad', y='Años de duración', color='Modalidad',
              title='Distribución de Duración por Modalidad')
st.plotly_chart(fig5, use_container_width=True)

st.markdown("---")
st.subheader("🌟 Promedio de Años de Acreditación por Carrera")
acreditacion_media = df.groupby('Carrera')['Años Acreditación Num'].mean().reset_index()
fig6 = px.bar(acreditacion_media, x='Carrera', y='Años Acreditación Num',
              title='Promedio de Años de Acreditación por Carrera')
st.plotly_chart(fig6, use_container_width=True)

# Reflexión
st.markdown("---")
st.markdown("### 💬 Reflexión Final")
st.markdown("""
El análisis comparativo permite identificar brechas y fortalezas entre programas similares. Esta información puede
ser usada estratégicamente para la mejora continua, procesos de acreditación o diseño curricular a nivel institucional.
""")
