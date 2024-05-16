import streamlit as st

st.set_page_config(page_title="Estadistica", page_icon=":📊:", layout="wide")


st.title("Análisis descriptivo")

st.subheader("Comparativa del rendimiento en las pruebas Saber 11 entre estudiantes de colegios de zonas rurales y urbanas.")

#Diagrama de torta
col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("diagrama de torta.png", width=900)
st.write("Los resultados  de los estudiantes que asisten a colegios ubicados en las zonas urbanas del país es superior al rendimiento de los estudiantes que asisten a colegios en las zonas rurales del país en las pruebas saber 11.")




st.subheader("Impacto del acceso a internet en el rendimiento académico.")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("internet.png", width=900)
st.write("La disponibilidad de acceso a internet en los hogares se correlaciona positivamente con un mayor puntaje global de los estudiantes, independientemente de si asisten a colegios en zonas urbanas o rurales")


st.subheader("Impacto del acceso a una computadora en el rendimiento en las pruebas saber 11")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("PC.png", width=900)
st.write("La disponibilidad de una computadora en los hogares se correlaciona positivamente con un mayor puntaje global de los estudiantes, independientemente de si asisten a colegios en zonas urbanas o rurales.")




st.subheader("Influencia del número de libros en el hogar.")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("lectura.png", width=900)
st.write("Existe una correlación significativa entre el número de libros en el hogar y el puntaje global de las pruebas. Esta relación sugiere que a medida que aumenta el número de libros en la familia, también tiende a incrementarse el puntaje obtenido por los estudiantes en las pruebas independientemente si asiste a un colegio en una zona rural o urbana")




st.subheader("Boxplot zona rural.")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("box_rural.png", width=900)
st.write("Q1: El 25% de los estudiantes que asisten a colegios en zonas rurales, tiene un puntaje menor o igual a 195 puntos globales")
st.write("Q2: El 50% de los estudiantes que asisten a colegios en zonas rurales, tiene un puntaje menor o igual a 225 puntos globales")
st.write("Q3: El 75% de los estudiantes que asisten a colegios en zonas rurales, tiene un puntaje menor o igual a 262 puntos globales")


st.subheader("Boxplot zona urbana.")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("box_urbano.png", width=900)
st.write("Q1: El 25% de los estudiantes que asisten a colegios en zonas rurales, tiene un puntaje menor o igual a 218 puntos globales ")
st.write("Q2: El 50% de los estudiantes que asisten a colegios en zonas rurales, tiene un puntaje menor o igual a 254 puntos globales ")
st.write("Q3: El 75% de los estudiantes que asisten a colegios en zonas rurales, tiene un puntaje menor o igual a 293 puntos globales")




st.subheader("Link del dashboard")

st.write("https://app.powerbi.com/view?r=eyJrIjoiODgxMWY0NTgtMjFlMi00ZGUwLTlmYzUtOWY3OWMzNDIyY2E4IiwidCI6IjNiOTQ0ZDlhLTEwNTEtNDY4NS1iMDlkLTlhOTVlZTJkYmQ5OSIsImMiOjR9&embedImagePlaceholder=true")

