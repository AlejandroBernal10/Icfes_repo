import streamlit as st
st.set_page_config(page_title="modelo", page_icon=":🧠:", layout="wide")



st.title("Modelo")

st.subheader("Esquema")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("esquema.png", width=900)



st.subheader("Data table")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("data_table_general.png", width=900)



st.subheader("Select columns")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("select.png", width=900)






st.subheader("Data table muestra")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("Data_muestra.png", width=900)



st.subheader("Scatter plot")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("scatter.png", width=900)













st.subheader("Test and score")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("test.png", width=900)


st.subheader("Predicciones")

col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("Predicciones.png", width=900)