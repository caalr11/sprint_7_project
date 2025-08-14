import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos

car_data = pd.read_csv('vehicles_us.csv')

st.header("Proyecto de Análisis de Datos de Vehículos.")
