import streamlit as st

from functions.data_functions import get_data
from functions.graphs import (
    age_graph,
    frequency_violence_graph,
    incidence_of_violence,
    kinship_graph,
    sex_of_aggressor_graph,
    social_media_violence_graph,
    temporality_graph,
)
from functions.scores_and_tables import incidence_table_by_violence_name
from functions.widgets import select_period_sex, violence_selection
from menu import menu

st.set_page_config(
    page_title="Incidencia por tipo de violencia - Dashboard de VDBG",
    page_icon="static/LOGO 6.png",
    layout="wide",
)

menu()

period, sex = select_period_sex()

if sex == ["Mujer"]:
    string = "mujeres"
elif sex == ["Hombre"]:
    string = "hombres"
else:
    string = "personas"

st.write("# Incidencia por tipo de violencia")

datos = data = get_data(sex=sex, period=period)

col1, col2 = st.columns([0.7, 0.3])

with col1.container(border=True):
    incidence_of_violence(data, sex)
with col2.container(border=True):
    title, selected_violence = violence_selection()

if title is None:
    st.stop()

with st.expander("Información sobre la violencia seleccionada:", expanded=True):
    with st.container(border=True):
        st.write("### {}".format(title))

    df_violence = incidence_table_by_violence_name(data, selected_violence)

    st.write(
        """
    El número de **{}** que sufrieron **{}** es **{}**.""".format(
            string, title.casefold(), len(df_violence)
        )
    )

    c1, c2 = st.columns(2)
    with c1:
        with st.container(border=True):
            frequency_violence_graph(df_violence, sex, title)
        with st.container(border=True):
            age_graph(df_violence, sex, title)
        with st.container(border=True):
            sex_of_aggressor_graph(df_violence, sex, title)
    with c2:
        with st.container(border=True):
            temporality_graph(df_violence, sex, title)
        with st.container(border=True):
            kinship_graph(df_violence, sex, title, selected_violence)
        with st.container(border=True):
            social_media_violence_graph(df_violence, sex, title)
