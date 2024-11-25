import streamlit as st


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
