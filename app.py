import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# Carga de datos desde un archivo Excel local
@st.cache
def load_data(filepath):
    data = pd.read_excel(filepath)
    data['fecha'] = pd.to_datetime(data['fecha'])  # Asegúrate de que la columna 'fecha' es de tipo datetime
    return data

# Ubicación del archivo Excel en tu sistema
file_path = 'Censo_empresarios.xlsx'  # Cambia esto por la ruta de tu archivo

# Intenta cargar los datos
try:
    df = load_data(file_path)
except Exception as e:
    st.error(f"Error al cargar el archivo: {e}")
    st.stop()

# Sidebar para filtros
st.sidebar.header('Filtros')
fecha_inicio = st.sidebar.date_input("Fecha Inicio", df['fecha'].min().date())
fecha_fin = st.sidebar.date_input("Fecha Fin", df['fecha'].max().date())

nif = st.sidebar.text_input("NIF Empresa")
nombre_empresa = st.sidebar.text_input("Nombre Empresa")
motivo = st.sidebar.text_input("Motivo")
cod_empresario = st.sidebar.text_input("Código Empresario")

# Conversión de las fechas de Streamlit a datetime
fecha_inicio = pd.to_datetime(fecha_inicio)
fecha_fin = pd.to_datetime(fecha_fin)

# Aplicación de filtros
df_filtered = df[(df['fecha'] >= fecha_inicio) & (df['fecha'] <= fecha_fin)]

if nif:
    df_filtered = df_filtered[df_filtered['nif_empresa'].str.contains(nif, case=False, na=False)]
if nombre_empresa:
    df_filtered = df_filtered[df_filtered['nombre_empresa'].str.contains(nombre_empresa, case=False, na=False)]
if motivo:
    df_filtered = df_filtered[df_filtered['motivo'].str.contains(motivo, case=False, na=False)]
if cod_empresario:
    df_filtered = df_filtered[df_filtered['cod_empresario'].str.contains(cod_empresario, case=False, na=False)]

# Mostrar la tabla de datos filtrados
st.dataframe(df_filtered)

# Gráfico de puntos por empresario
if not df_filtered.empty:
    puntos_data = df_filtered.groupby('cod_empresario')['puntos'].sum().reset_index()
    puntos_data['puntos_restantes'] = 12 - puntos_data['puntos']
    fig = px.bar(puntos_data, x='cod_empresario', y='puntos_restantes', title="Puntos Restantes por Empresario")
    st.plotly_chart(fig)
