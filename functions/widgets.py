import streamlit as st

from functions.constants_values import KEY_VIOLENCE_NAMES


def update_selections():
    st.session_state.period = st.session_state.selected_period
    st.session_state.sex = st.session_state.selected_sex
    with st.sidebar:
        st.success("Filtros actualizados", icon="✅")


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
