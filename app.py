import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer los datos

car_data = pd.read_csv('vehicles_us.csv')

st.header("Proyecto de Análisis de Datos de Vehículos.")

hist_button = st.button('Construir histograma')

# Lógica a ejecutar cuando se hace clic en el botón
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Constuir diagrama de dispersión')
if disp_button:
    st.write(
        'Creación de un diagrama de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un diagrama de dispersión utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de dispersión
    fig2 = go.Figure(data=go.Scatter(
        x=car_data['model_year'], y=car_data['price'], mode='markers'))

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig2.update_layout(title_text='Relación entre Año y Precio')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig2, use_container_width=True)
