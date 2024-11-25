import streamlit as st

from functions.constants_values import KEY_VIOLENCE_NAMES


def update_selections():
    st.session_state.period = st.session_state.selected_period
    st.session_state.sex = st.session_state.selected_sex
    with st.sidebar:
        st.success("Filtros actualizados", icon="✅")


def menu():
    st.sidebar.image("static/LOGO 1.png", width=200)
    (
        st.sidebar.page_link(
            "Inicio.py",
            label="Inicio",
            icon=":material/home:",
            help="Página Inicial",
        ),
    )
    (
        st.sidebar.page_link(
            "pages/1_Datos_demográficos.py",
            label="Datos demográficos",
            icon=":material/demography:",
            help="Datos demográficos",
        ),
    )
    (
        st.sidebar.page_link(
            "pages/2_Uso_de_internet_y_redes_sociales.py",
            label="Uso de internet y redes sociales",
            icon=":material/travel_explore:",
            help="Uso de internet y redes sociales",
        ),
    )
    (
        st.sidebar.page_link(
            "pages/3_Incidencia_por_tipo_de_violencia.py",
            label="Incidencia por tipo de violencia",
            icon=":material/emergency:",
            help="Incidencia por tipo de violencia",
        ),
    )
    (
        st.sidebar.page_link(
            "pages/4_Conocimiento_sobre_VDBG.py",
            label="Conocimiento sobre VDBG",
            icon=":material/menu_book:",
            help="Conocimiento sobre VDBG",
        ),
    )
    (
        st.sidebar.page_link(
            "pages/5_Cruce_de_variables.py",
            label="Cruce de variables",
            icon=":material/compare_arrows:",
            help="Cruce de variables",
        ),
    )
    (
        st.sidebar.page_link(
            "pages/6_Acerca_de.py",
            label="Acerca de",
            icon=":material/partner_exchange:",
            help="Acerca del proyecto",
        ),
    )

    with st.sidebar:
        st.divider()


def select_period_sex():
    if "period" and "sex" not in st.session_state:
        st.session_state.period = [2023, 2024]
        st.session_state.sex = ["Mujer", "Hombre"]

    period = st.sidebar.multiselect(
        "Selecciona el periodo a consultar",
        options=[2023, 2024],
        default=st.session_state.get("period"),
        placeholder="Selecciona un año",
        key="selected_period",
        on_change=update_selections,
    )

    sex = st.sidebar.multiselect(
        "Selecciona el sexo a consultar",
        options=["Mujer", "Hombre"],
        default=st.session_state.get("sex"),
        placeholder="Selecciona una opción",
        key="selected_sex",
        on_change=update_selections,
    )

    return period, sex


def violence_selection(index=None):
    title = st.selectbox(
        "Selecciona la violencia que deseas ver",
        KEY_VIOLENCE_NAMES.keys(),
        index=None,
        key="tipo_violencia",
    )
    if title is not None:
        selected_violence = KEY_VIOLENCE_NAMES[title]
    else:
        selected_violence = None
    return title, selected_violence
