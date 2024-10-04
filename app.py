import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#st.header('Prueba')
hist_button = st.button('Construir histograma') # crear un botón
scatter_button = st.button('Construir gráfico de dispersión')  # nuevo botón para grafico de dispersión
build_histogram = st.checkbox('Construir un histograma')
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scatter_button:  # al hacer clic en el botón de gráfico de dispersión
    st.write('Construyendo un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    scatter_fig = px.scatter(car_data, x="year", y="price")
    
    # mostrar el gráfico de dispersión
    st.plotly_chart(scatter_fig, use_container_width=True)