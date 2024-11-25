import streamlit as st

from functions.data_functions import get_data
from functions.graphs import knowledge_violence_graph, violence_term_graph
from functions.scores_and_tables import quantile_for_number_violences
from functions.widgets import select_period_sex

st.set_page_config(
    page_title="Conocimiento sobre VDBG - Dashboard de VDBG",
    page_icon="static/LOGO 6.png",
    layout="wide",
)

st.write("# Conocimiento sobre violencias digitales basadas en género")

period, sex = select_period_sex()

datos = data = get_data(sex=sex, period=period)

if st.session_state.sex == ["Mujer"]:
    string = "las mujeres"
elif st.session_state.sex == ["Hombre"]:
    string = "los hombres"
else:
    string = "las personas"

c1, c2 = st.columns(2)
with c1.container(border=True):
    violence_term_graph(data)

with c2.container(border=True):
    knowledge_violence_graph(data, sex)

st.info(
    "El 75% de {} conocen al menos {} violencias por su nombre.".format(
        string, quantile_for_number_violences(data)
    )
)
