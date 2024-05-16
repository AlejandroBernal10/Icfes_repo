import streamlit as st

st.set_page_config(page_title="Antecedentes", page_icon=":📑", layout="wide")


st.title("Investigación.")
col1, col2, col3 = st.columns([1, 2, 6])

# Dejando espacio vacío en las columnas externas
with col1:
    st.write("")

with col3:
    st.write("")

# Mostrando la imagen en la columna central
with col2:
    st.image("a_rural.png", width=900)

st.write("Se registró el preocupante indicador que muestra que solo el 22.7% de las sedes educativas rurales cuentan con internet, mientras que el 90.8% de las urbanas sí tienen esta posibilidad tecnológica.")
st.write("Recuperado de.")
st.write("Colombia Aprende. (s.f.). La educación rural: un gran desafío para Colombia. https://www.colombiaaprende.edu.co/agenda/tips-y-orientaciones/la-educacion-rural-un-gran-desafio-para-colombia")

st.subheader("Educación rural en Colombia una brecha histórica en desigualdad.")
st.write("Históricamente los colegios de la zona urbana obtienen mejores puntajes en las pruebas ICFES que los colegios rurales.")
st.write("Recuperado de.")
st.write("Alianza Verde. (2023, 15 de abril). Educación Rural en Colombia: una brecha histórica en desigualdad.  https://alianzaverde.org.co/blog-verde/educacion-rural-en-colombia-una-brecha-historica-en-desigualdad")


st.subheader("Balance Pruebas Saber 11: ¿Cómo le fue a los estudiantes?")
st.write("Datos del Icfes muestran que “por cada dos estudiantes evaluados que residen en una zona rural, se evalúan 9 estudiantes de zonas urbanas, lo cual evidencia una diferencia de 64 puntos porcentuales”.")
st.write("Recuperado de.")
st.write("El Espectador. (2024, 12 de mayo). Balance pruebas saber 11, ¿cómo le fue a los estudiantes?  https://www.elespectador.com/educacion/balance-pruebas-saber-11-como-le-fue-a-los-estudiantes")



