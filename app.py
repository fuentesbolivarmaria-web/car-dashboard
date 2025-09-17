import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# Leer los datos del CSV
car_data = pd.read_csv('vehicles_us.csv')

# Título principal
st.header("Panel de control de anuncios de coches")

# Casillas de verificación para mostrar gráficos
build_hist = st.checkbox("Mostrar histograma del odómetro")
build_scatter = st.checkbox("Mostrar gráfico de dispersión precio vs odómetro")

# Histograma
if build_hist:
    st.write("Histograma de la columna 'odometer'")
    fig_hist = go.Figure(data=[go.Histogram(x=car_data['odometer'])])
    fig_hist.update_layout(title_text="Distribución del Odómetro")
    st.plotly_chart(fig_hist, use_container_width=True)

# Gráfico de dispersión
if build_scatter:
    st.write("Gráfico de dispersión: Precio vs Odómetro")
    fig_scatter = go.Figure(data=[go.Scatter(x=car_data['odometer'],
                                              y=car_data['price'],
                                              mode='markers')])
    fig_scatter.update_layout(title_text="Relación entre Odómetro y Precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
