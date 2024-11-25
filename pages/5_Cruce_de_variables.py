import streamlit as st

from functions.data_functions import get_data
from functions.graphs import (
    age_violence_graph,
    frequency_all_violence_graph,
    identification_aggressor_violence_graph,
    kinship_violence_graph,
    knowledge_violences_names_graph,
    location_violence_graph,
    occupations_violences_graph,
    reactions_graph,
    reactions_violence_graph,
    sex_kinship_by_violence_graph,
    sex_violence_graph,
    social_media_violences_graph,
)
from functions.scores_and_tables import process_age_ranges

from functions.widgets import select_period_sex, violence_selection

st.set_page_config(
    page_title="Cruce de variables - Dashboard de VDBG",
    page_icon="static/LOGO 6.png",
    layout="wide",
)

period, sex = select_period_sex()

datos = data = get_data(sex=sex, period=period)

if sex == ["Mujer"]:
    string = "mujeres"
elif sex == ["Hombre"]:
    string = "hombres"
else:
    string = "personas"

ages_ = process_age_ranges(data)

st.write("# Cruce de variables")
with st.container(border=True):
    age_violence_graph(ages_, sex)

with st.container(border=True):
    social_media_violences_graph(data, sex)

with st.container(border=True):
    # st.write("## Parentesco con las personas que han sufrido violencias")
    kinship_violence_graph(data, sex)

with st.container(border=True):
    # st.write("## Identificación de la persona agresora por tipo de violencia")

    identification_aggressor_violence_graph(data, sex)

    st.warning(
        """
        En este escenario no se observa **mobbing**, porque la esencia de esta forma de
        violencia provoca que la víctima reconozca a su agresor(a).
        """
    )

with st.container(border=True):
    # st.write("## Sexo del agresor(a) por tipo de violencia")
    sex_violence_graph(data, sex)

with st.container(border=True):
    st.write(
        "### Sexo del agresor y parentesco con la persona que ha experimentado la violencia"
    )

    title, selected_violence = violence_selection()
    if selected_violence is not None:
        sex_kinship_by_violence_graph(data, selected_violence, title, sex)


with st.container(border=True):
    # st.write("## Ocupaciones frecuentes por tipo de violencia")
    occupations_violences_graph(data, sex)

with st.container(border=True):
    # st.write("## Ubicación de las víctimas por violencia sufrida")
    location_violence_graph(data, sex)

with st.container(border=True):
    # st.write("## Cantidad de veces que la víctima reporta haber sufrido la violencia")
    frequency_all_violence_graph(data, sex)

with st.container(border=True):
    # st.write("## Reacción de la víctima al sufrir la(s) violencia(s)")
    reactions_graph(data, sex)

with st.container(border=True):
    # st.write("## Reacciones de las víctimas por violencia")
    reactions_violence_graph(data, sex)

with st.container(border=True):
    # st.write("## Conocimiento del nombre de la violencia por tipo de violencia")
    knowledge_violences_names_graph(data, sex)
