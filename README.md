# renderApp
TripleTen_Web_App
Primer Commit

 Este código es un ejemplo de una aplicación web simple en Streamlit que interactúa con datos de un archivo CSV ('vehicles_us.csv') y permite al usuario elegir entre construir un histograma o un gráfico de dispersión utilizando Plotly Express. Aquí está una breve descripción de lo que hace el código:

1. Importa las bibliotecas necesarias: `pandas` para el manejo de datos, `plotly.express` como `px` para la creación de gráficos interactivos y `streamlit` como `st` para la creación de la aplicación web.

2. Lee los datos del archivo 'vehicles_us.csv' en un DataFrame `car_data`.

3. Crea dos botones utilizando `st.button()`: uno para construir un histograma con el texto 'Construir histograma' y otro para construir un gráfico de dispersión con el texto 'Construir gráfico de dispersión'.

4. Si el usuario hace clic en el botón de histograma (`hist_button`), se muestra un mensaje indicando que se está creando un histograma para los datos de anuncios de venta de coches. Luego, se crea un histograma utilizando `px.histogram()` con la variable "odometer" como eje x. Finalmente, se muestra el gráfico interactivo utilizando `st.plotly_chart()`.

5. Si el usuario hace clic en el botón de gráfico de dispersión (`scatter_button`), se muestra un mensaje indicando que se está construyendo un gráfico de dispersión para los datos de anuncios de venta de coches. Se crea un gráfico de dispersión utilizando `px.scatter()` con las variables "year" en el eje x y "price" en el eje y. El gráfico de dispersión se muestra interactivo utilizando `st.plotly_chart()`.

En resumen, este código crea una aplicación web simple que permite al usuario explorar visualmente los datos de anuncios de venta de coches mediante la selección de histogramas o gráficos de dispersión.  
-----------------------------------------------------------------

Enlace a la APP: https://renderapp-aalf.onrender.com/