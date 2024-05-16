import pandas as pd  
import streamlit as st  

st.set_page_config(page_title="Base", page_icon=":🌐:", layout="wide")
 
df = pd.read_excel(
    io="Presentacion_icfes_2023_version_final.xlsx",
    engine="openpyxl",
    sheet_name="SB11_20232",
    skiprows=0,
    usecols="A:AQ",
    nrows=100,
)

st.title("Análisis de datos Icfes")

#st.sidebar.image("icfes.png", use_column_width=True) 

st.sidebar.header("Por favor filtra aquí")
area_ubicación = st.sidebar.multiselect(
    "Selecciona el área:",
    options=df["Area_ubicación"].unique(),
    default=df["Area_ubicación"].unique()
)

df_selection = df.query(
    "Area_ubicación == @area_ubicación"
)

st.image("icfes.png", use_column_width=True)

st.subheader("Base de datos")
st.dataframe(df_selection)



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
