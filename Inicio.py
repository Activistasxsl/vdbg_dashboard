import streamlit as st

from functions.data_functions import get_data
from functions.graphs import incidence_of_violence, pie_answers_by_sex
from functions.scores_and_tables import (
    average_violence,
    internet_use_growth_percentage,
    known_laws_percentage,
    known_violences_percentage,
    principal_reactions,
)
from functions.widgets import menu, select_period_sex

st.set_page_config(
    page_title="Activistasxsl - Dashboard de VDBG",
    page_icon="static/LOGO 6.png",
    layout="wide",
)

menu()

period, sex = select_period_sex()

if st.session_state.sex == ["Mujer"]:
    string = "una mujer"
elif st.session_state.sex == ["Hombre"]:
    string = "un hombre"
else:
    string = "una persona"

datos = data = get_data(sex=st.session_state.sex, period=st.session_state.period)

st.write("# Caracterización de violencias digitales basadas en género en Venezuela")
st.write(
    """
    Desde el año 2023, [Mujeres Activistas por el Software Libre](http://activistasxsl.org)
    realiza un esfuerzo para generar datos sobre un fenómeno aún invisibilizado en nuestro
    país como las violencias digitales basadas en género.
    """
)
st.write(
    """
    En el 2024, gracias al apoyo del Fondo NUMUN, dimos un paso adelante
    para mostrar un dashboard que permita reunir los resultados encontrados hasta
    ahora.
    """
)
st.write(
    """
    En ambos casos hemos utilizado una encuesta en línea, disponible entre los meses mayo
    y septiembre de cada año.
    """
)
col1, col2 = st.columns([0.35, 0.65])
with col1:
    with st.container(border=True):
        st.metric("Número de respuestas", len(data))
    with st.container(border=True):
        pie_answers_by_sex(data)


with col2:
    with st.container(border=True):
        st.error(
            "En promedio, {} es víctima de {} diferentes tipos de violencias digitales.".format(
                string, average_violence(data)
            ),
            icon="🚨",
        )
    with st.container(border=True):
        incidence_of_violence(data, sex)

c1, c2, c3 = st.columns(3)

with c1:
    with st.container(border=True):
        st.metric(
            "Conocen leyes o normativas en el país que contemplan \n\n las violencias digitales",
            "{}%".format(known_laws_percentage(data)),
        )
with c2:
    with st.container(border=True):
        st.metric(
            "Han aumentado su tiempo de conexión a internet \n\n luego del COVID-19",
            "{}%".format(internet_use_growth_percentage(data)),
        )

with c3:
    with st.container(border=True):
        st.metric(
            "Han escuchado antes el término \n\n Violencia Digital Basada en Género",
            "{}%".format(known_violences_percentage(data)),
        )
r1, v1, r2, v2 = principal_reactions(data)

with st.container(border=True):
    st.write("Las principales reacciones de las víctimas ante sus agresores fueron:")
    st.warning(
        """
        **{}** (**{}%**) y/o **{}** (**{}%**).
        """.format(r1, v1, r2.casefold(), v2)
    )
