import numpy
import pandas as pd
import plotly.express as px
import plotly.graph_objects
import plotly.graph_objects as go
import streamlit as st

from matplotlib import pyplot as plt

from functions.constants_values import (
    BALTLOW_100_SCRAMBLED_SWATCHES,
    COLORS,
    SOCIAL_MEDIA_NAMES,
)
from functions.scores_and_tables import (
    age_tables,
    answers_by_state,
    frequency_violence,
    kinship_identification_violences,
    kinship_violences,
    knowledge_violences,
    knowledge_violences_names,
    location_violence,
    occupations_violences,
    post_covid_internet,
    principal_reactions,
    reactions_violence,
    sex_aggressor_violence,
    sex_kinship_by_violence,
    social_media_use,
    social_media_violences,
    table_by_sex,
    table_gender_sex,
    ten_common_occupations,
    violence_victims_percentages,
)


def pie_answers_by_sex(df: pd.DataFrame) -> plotly.graph_objects.Figure:
    sex_tbl = table_by_sex(df)

    fig = go.Figure(
        data=[go.Pie(labels=sex_tbl.index, values=sex_tbl)],
    )
    fig.update_layout(
        title_text="Respuestas por sexo",
        legend_title="Sexo",
        font=dict(color="black"),
    )
    fig.update_traces(
        marker=dict(
            colors=COLORS,
            line=dict(color="white", width=1),
        )
    )

    st.plotly_chart(fig)


def incidence_of_violence(df: pd.DataFrame, sex: list) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        xaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        xaxes = "% de hombres"
    else:
        xaxes = "% de personas"
    incidence_of_violence = violence_victims_percentages(df)
    fig = px.bar(
        incidence_of_violence[["Sí", "No"]].sort_values("Sí"),
        orientation="h",
        text_auto=True,
        color_discrete_sequence=COLORS,
    )
    fig.update_layout(
        title="Incidencia de violencias",
        yaxis_title="Violencia",
        xaxis_title=xaxes,
        legend_title="¿Sufrió la violencia?",
        font=dict(
            color="black",
        ),
    )
    fig.update_traces(
        textangle=0,
        cliponaxis=False,
        marker_line_color="white",
        texttemplate="%{value: 4} %",
    )
    st.plotly_chart(fig)


def gender_sex_graph(df: pd.DataFrame) -> plotly.graph_objects.Figure:
    tbl_gender_sex = table_gender_sex(df)
    fig = px.bar(
        tbl_gender_sex,
        x="genero",
        y="count",
        color="sexo",
        barmode="group",
        color_discrete_sequence=COLORS,
    )
    fig.update_layout(
        title="Número de personas por sexo y género",
        yaxis_title="Cantidad de personas",
        xaxis_title="Género",
        legend_title="Sexo",
        font=dict(
            color="black",
        ),
    )
    st.plotly_chart(fig)


def ages_graph(df: pd.DataFrame, sex: list) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
    else:
        yaxes = "% de personas"
    ages, ages_percentage = age_tables(df)
    fig = px.bar(ages, text=ages_percentage)
    fig.update_layout(
        title="Rangos de edades",
        xaxis_title="Edades",
        yaxis_title=yaxes,
        font=dict(
            family="Arial",
            color="black",
        ),
    )
    fig.update_traces(
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
        marker_color=COLORS[0],
        marker_line_color="white",
    )
    st.plotly_chart(fig)


def map_graph(df: pd.DataFrame) -> plotly.graph_objects.Figure:
    df_map = answers_by_state(df)
    fig, ax = plt.subplots(1, 1)
    ax.set_title(
        "Ubicación",
        fontdict={"fontsize": 10, "fontweight": "bold"},
        loc="left",
    )
    df_map.plot(
        "Personas",
        ax=ax,
        cmap="Oranges",
        edgecolor="black",
        categorical=True,
        legend=True,
        legend_kwds={"loc": "center left", "bbox_to_anchor": (1, 0.5), "fmt": "{:.0f}"},
    )
    st.pyplot(fig)


def occupation_graph(df: pd.DataFrame, sex: list) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        xaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        xaxes = "% de hombres"
    else:
        xaxes = "% de personas"
    df_occupation = ten_common_occupations(df)
    fig = px.bar(
        df_occupation,
        y="Ocupación",
        x="Nº de personas",
        text="%",
        barmode="group",
        orientation="h",
    )
    fig.update_layout(
        title="Ocupación",
        yaxis_title="Ocupación",
        xaxis_title=xaxes,
        font=dict(
            family="Arial",
            color="black",
        ),
    )
    fig.update_traces(
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
        marker_color="rgb(7, 171, 157)",
        marker_line_color="white",
        texttemplate="%{value} %",
    )
    st.plotly_chart(fig)


def growth_internet_use(df: pd.DataFrame) -> plotly.graph_objects.Figure:
    df_covid = post_covid_internet(df)
    fig = go.Figure(data=[go.Pie(labels=df_covid.index, values=df_covid)])
    fig.update_layout(
        title_text="Aumento del uso de internet luego del Covid-19",
        legend_title="¿Has aumentado tu tiempo de <br> conexión a internet?",
        font=dict(family="Arial", color="black"),
    )
    fig.update_traces(
        marker=dict(
            colors=COLORS,
            line=dict(color="white", width=1),
        )
    )
    st.plotly_chart(fig)


def graph_social_media_use(df: pd.DataFrame) -> plotly.graph_objects.Figure:
    df_social_media = social_media_use(df)
    fig = px.bar(
        df_social_media.sort_values("No la utilizo"),
        orientation="h",
        color_discrete_sequence=BALTLOW_100_SCRAMBLED_SWATCHES,
    )
    fig.update_layout(
        title="Uso diario de aplicaciones/redes sociales",
        xaxis_title="% de mujeres",
        yaxis_title="Aplicación/red social",
        legend_title="Horas de uso diario",
        font=dict(
            family="Arial",
            color="black",
        ),
    )
    st.plotly_chart(fig)


def frequency_violence_graph(
    df_violence: pd.DataFrame, sex: list, title: str
) -> plotly.graph_objects.Figure:
    freq_tbl = (
        df_violence[[s for s in df_violence.columns if "veces_" in s][0]]
        .value_counts()
        .to_frame()
    )
    freq_percentage = round(freq_tbl / freq_tbl.sum() * 100, 2)

    if sex == ["Mujer"]:
        yaxis = "% de mujeres"
        color = "rgb(149, 27, 129)"
    elif sex == ["Hombre"]:
        yaxis = "% de hombres"
        color = "rgb(39, 55, 77)"
    else:
        yaxis = "% de personas"
        color = "rgb(120, 27, 100)"

    fig = px.bar(freq_percentage, text_auto=True)
    fig.update_layout(
        title=" ".join(["Incidencia de", title.casefold()]),
        xaxis_title="Frecuencia",
        yaxis_title=yaxis,
        font=dict(
            family="Arial",
            size=18,
            color="black",
        ),
    )
    fig.update_traces(
        textfont_size=18,
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
        marker_color=color,
        marker_line_color="white",
        texttemplate="%{value:} %",
    )

    st.plotly_chart(fig)


def temporality_graph(
    df_violence: pd.DataFrame, sex: list, title: str
) -> plotly.graph_objects.Figure:
    temp_tbl = (
        df_violence[[s for s in df_violence.columns if "6_" in s][0]]
        .value_counts()
        .to_frame()
    )
    if sex == ["Mujer"]:
        color = {"Sí": "rgb(149, 27, 129)", "No": "rgb(57, 105, 172)"}
    elif sex == ["Hombre"]:
        color = {"Sí": "rgb(39, 55, 77)", "No": "rgb(82, 109, 130)"}
    else:
        color = {"Sí": "rgb(149, 27, 129)", "No": "rgb(57, 105, 172)"}
    if len(temp_tbl) <= 1:
        # TODO Review temp_tbl.index[0].lower()
        st.write(
            "Las personas que sufrieron de {}, manifiestan que {} ocurrió durante los últimos 6 meses".format(
                title.casefold(temp_tbl.index[0].lower()), temp_tbl.index[0].lower()
            )
        )
    else:
        fig = px.pie(
            temp_tbl,
            names=temp_tbl.index,
            values=temp_tbl["count"],
            color=temp_tbl.index,
            color_discrete_map=color,
        )
        fig.update_layout(
            title_text=" ".join(
                [
                    "Porcentaje de víctimas de",
                    title.casefold(),
                    "en los últimos 6 meses",
                ],
            ),
            legend_title="¿Ocurrió en los últimos seis meses?",
            font=dict(family="Arial", size=18, color="black"),
        )
        fig.update_traces(
            marker=dict(
                line=dict(color="white", width=1),
            )
        )
    st.plotly_chart(fig)


def age_graph(
    df_violence: pd.DataFrame, sex: list, title: str
) -> plotly.graph_objects.Figure:
    age_tbl = (
        pd.cut(
            df_violence[[s for s in df_violence.columns if "edad_" in s][0]],
            bins=[0, 10, 15, 18, 25, 30, 40, 50, 60, 75],
            right=False,
        )
        .value_counts()
        .sort_index()
    )
    age_tbl_percentage = round(age_tbl / age_tbl.sum() * 100, 2)
    if sex == ["Mujer"]:
        yaxis = "% de mujeres"
        color = "rgb(7, 171, 157)"
    elif sex == ["Hombre"]:
        yaxis = "% de hombres"
        color = "rgb(157, 178, 191)"
    else:
        yaxis = "% de personas"
        color = "rgb(120, 27, 100)"
    x = age_tbl_percentage.index.astype("string")
    y = age_tbl_percentage.values

    fig = px.bar(age_tbl_percentage, x, y, text_auto=True)
    fig.update_layout(
        title="Rangos de edad en que las víctimas sufrieron {} por primera vez".format(
            title.casefold()
        ),
        xaxis_title="Edades",
        yaxis_title=yaxis,
        font=dict(
            family="Arial",
            size=15,
            color="black",
        ),
    )
    fig.update_traces(
        textfont_size=18,
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
        marker_color=color,
        marker_line_color="white",
        texttemplate="%{value: .4} %",
    )
    fig.update_xaxes(
        labelalias={
            "[0, 10)": "0-9",
            "[10, 15)": "10-14",
            "[15, 18)": "15-17",
            "[18, 25)": "18-24",
            "[25, 30)": "24-29",
            "[30, 40)": "30-39",
            "[40, 50)": "40-49",
            "[50, 60)": "50-59",
            "[60, 75)": "60 y más",
        }
    )
    st.plotly_chart(fig)


def kinship_graph(
    df_violence: pd.DataFrame, sex: list, title: str, selected_violence: str
):
    if selected_violence != "exclusion":
        kinship_tbl = (
            df_violence[
                [
                    s
                    for s in df_violence.columns
                    if "parentesco_" in s or "identificacion_" in s
                ][0]
            ]
            .value_counts()
            .to_frame()
        )
        if len(kinship_tbl) <= 1:
            st.write(
                "Las personas que sufrieron de {} manifiestan que su parentesco con su agresor es: {}".format(
                    title.casefold(), kinship_tbl.index[0].lower()
                )
            )
        if selected_violence not in [
            "grooming",
            "phishing_vs",
            "trata",
            "phishing",
            "mobbing",
        ]:
            if sex == ["Mujer"]:
                yaxis = "las mujeres"
                color = "rgb(57, 105, 172)"
            elif sex == ["Hombre"]:
                yaxis = "los hombres"
                color = "rgb(82, 109, 130)"
            else:
                yaxis = "las personas"
                color = "rgb(120, 27, 100)"

            kinship_tbl_percentage = kinship_tbl.rename_axis(
                index="parentesco"
            ).reset_index()
            kinship_tbl_percentage["percentage"] = round(
                kinship_tbl_percentage["count"] / kinship_tbl["count"].sum() * 100,
                2,
            )
            fig = px.bar(
                kinship_tbl_percentage,
                x="parentesco",
                y="percentage",
                text="count",
            )
            fig.update_layout(
                title="Parentesco de la persona agresora con {} que han sufrido {}".format(
                    yaxis, title.casefold()
                ),
                xaxis_title="Parentesco",
                yaxis_title="% de agresiones",
                font=dict(
                    family="Arial",
                    size=16,
                    color="black",
                ),
            )
            fig.update_traces(
                textangle=0,
                textposition="outside",
                cliponaxis=False,
                showlegend=False,
                marker_color=color,
                marker_line_color="white",
                texttemplate="%{value: .4} %",
            )
        elif selected_violence == "mobbing":
            if sex == ["Mujer"]:
                color = ["rgb(149, 27, 129)", "rgb(57, 105, 172)", "rgb(7, 171, 157)"]
            elif sex == ["Hombre"]:
                color = ["rgb(39, 55, 77)", "rgb(82, 109, 130)", "rgb(157, 178, 191)"]
            else:
                color = ["rgb(149, 27, 129)", "rgb(57, 105, 172)", "rgb(120, 27, 100)"]
            fig = go.Figure(
                data=[go.Pie(labels=kinship_tbl.index, values=kinship_tbl["count"])]
            )
            fig.update_layout(
                title_text="Relación laboral con el agresor",
                legend_title="El agresor era:",
                font=dict(family="Arial", size=18, color="black"),
            )
            fig.update_traces(
                marker=dict(
                    colors=color,
                    line=dict(color="white", width=1),
                )
            )

        else:
            if sex == ["Mujer"]:
                color = ["rgb(149, 27, 129)", "rgb(57, 105, 172)"]
            elif sex == ["Hombre"]:
                color = ["rgb(39, 55, 77)", "rgb(82, 109, 130)", "rgb(157, 178, 191)"]
            else:
                color = ["rgb(149, 27, 129)", "rgb(57, 105, 172)", "rgb(120, 27, 100)"]
            fig = go.Figure(
                data=[go.Pie(labels=kinship_tbl.index, values=kinship_tbl["count"])]
            )
            fig.update_layout(
                title_text="Identificación de la persona agresora por parte de la víctima de {}".format(
                    title.casefold()
                ),
                legend_title="¿Identificaste al agresor(a)?",
                font=dict(family="Arial", size=18, color="black"),
            )
            fig.update_traces(
                marker=dict(
                    colors=color,
                    line=dict(color="white", width=1),
                )
            )

        st.plotly_chart(fig)


def sex_of_aggressor_graph(
    df_violence: pd.DataFrame, sex: list, title: str
) -> plotly.graph_objects.Figure:
    if title != "Exclusión digital":
        tbl_sex = (
            df_violence[[s for s in df_violence.columns if "sexo_" in s][0]]
            .value_counts()
            .to_frame()
        )
        if len(tbl_sex) <= 1:
            st.write(
                "Para {} todas las personas agresoras son de sexo {}".format(
                    title.casefold(), tbl_sex.index[0]
                )
            )
        else:
            if sex == ["Mujer"] or sex != ["Hombre"]:
                color = {"Mujer": "rgb(149, 27, 129)", "Hombre": "rgb(57, 105, 172)"}
            else:
                color = {
                    "Mujer": "rgb(39, 55, 77)",
                    "Hombre": "rgb(82, 109, 130)",
                    "Un grupo de personas": "rgb(157, 178, 191)",
                }

            fig = px.pie(
                tbl_sex,
                names=tbl_sex.index,
                values=tbl_sex["count"],
                color=tbl_sex.index,
                color_discrete_map=color,
            )
            fig.update_layout(
                title_text=" ".join(
                    [
                        "Sexo de la persona agresora para",
                        title.casefold(),
                    ]
                ),
                legend_title="Sexo del agresor(a)",
                font=dict(family="Arial", size=18, color="black"),
            )
            fig.update_traces(
                marker=dict(
                    line=dict(color="white", width=1),
                )
            )

            st.plotly_chart(fig)


def social_media_violence_graph(
    df_violence: pd.DataFrame, sex: list, title: str
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
        color = "rgb(149, 27, 129)"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
        color = "rgb(39, 55, 77)"
    else:
        yaxes = "% de personas"
        color = "rgb(149, 27, 129)"
    cols = [
        s
        for s in df_violence.columns
        for n in SOCIAL_MEDIA_NAMES.keys()
        if s.startswith(n)
    ][:-1]
    df = df_violence[cols].sum()
    new_index = []
    for medio in list(df.index.values):
        new_index.append(SOCIAL_MEDIA_NAMES[medio.split("_")[0]])
    df.index = new_index
    df = df / df_violence.iloc[:, 0].sum() * 100
    df = round(df.apply(pd.to_numeric, errors="coerce").fillna(0), 2)
    fig = px.bar(
        df,
        x=df.index,
        y=df.values,
        title="Aplicación o red social por la cual la victima sufrió {}".format(
            title.casefold()
        ),
        barmode="group",
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )
    fig.update_xaxes(title="App/red social")
    fig.update_yaxes(title=yaxes)
    fig.update_traces(
        textfont_size=18,
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
        marker_color=color,
        marker_line_color="white",
        texttemplate="%{value: .4} %",
    )
    fig.update_layout(
        font=dict(
            family="Arial",
            size=18,
            color="black",
        )
    )

    st.plotly_chart(fig)


def violence_term_graph(df: pd.DataFrame) -> plotly.graph_objects.Figure:
    tbl = df.vdbg.value_counts()
    fig = go.Figure(data=[go.Pie(labels=tbl.index, values=tbl)])
    fig.update_layout(
        title_text="Conocimiento del término VDBG",
        legend_title="¿Habías escuchado antes el término <br> Violencia Digital Basada en Género?",
        font=dict(family="Arial", color="black"),
    )
    fig.update_traces(
        marker=dict(
            colors=COLORS,
            line=dict(color="white", width=1),
        )
    )

    st.plotly_chart(fig)


def knowledge_violence_graph(
    df: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    knowledge_violences_tbl = knowledge_violences(df)
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
    else:
        yaxes = "% de personas"

    fig = px.bar(
        knowledge_violences_tbl.sort_values("cantidad", ascending=False),
        y="cantidad",
        x=knowledge_violences_tbl.index,
        text_auto=True,
    )
    fig.update_layout(
        title="Conocimiento de la violencia por su nombre",
        xaxis_title="Violencia",
        yaxis_title=yaxes,
        font=dict(
            family="Arial",
            color="black",
        ),
    )
    fig.update_traces(
        textfont_size=18,
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
        marker_color=COLORS[0],
        marker_line_color="white",
        texttemplate="%{value: .4} %",
    )

    st.plotly_chart(fig)


def age_violence_graph(
    df_grouped: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
    else:
        yaxes = "% de personas"
    fig = px.bar(
        df_grouped,
        x="Edad",
        y="Porcentaje",
        color="Violencia",
        title="Tasa de incidencia por grupo etáreo según tipo de violencia",
        barmode="group",
        color_discrete_sequence=BALTLOW_100_SCRAMBLED_SWATCHES,
    )
    fig.update_layout(
        font=dict(family="Arial", size=16, color="black"),
    )
    fig.update_yaxes(title=yaxes)
    fig.update_xaxes(
        title="Rangos de edad",
        labelalias={
            "[0, 10)": "0-9",
            "[10, 15)": "10-14",
            "[15, 18)": "15-17",
            "[18, 25)": "18-24",
            "[25, 30)": "24-29",
            "[30, 40)": "30-39",
            "[40, 50)": "40-49",
            "[50, 60)": "50-59",
            "[60, 75)": "60 y más",
        },
    )
    st.plotly_chart(fig)


def social_media_violences_graph(
    data: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
    else:
        yaxes = "% de personas"
    df = social_media_violences(data)
    fig = px.bar(
        df.sort_values("Porcentaje", ascending=False),
        x="Porcentaje",
        y="Violencia",
        color="Medio",
        title="Tipo de violencia según el medio por el cual ocurrió",
        barmode="stack",
        orientation="h",
        color_discrete_sequence=BALTLOW_100_SCRAMBLED_SWATCHES,
    )
    fig.update_layout(
        font=dict(family="Arial", size=16, color="black"),
    )
    fig.update_yaxes(title="Violencia")
    fig.update_xaxes(title=yaxes)
    st.plotly_chart(fig)


def kinship_violence_graph(
    data: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
        string = "las mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
        string = "los hombres"
    else:
        yaxes = "% de personas"
        string = "las personas"
    df = kinship_violences(data)
    fig = px.bar(
        df,
        x="Violencia",
        y="Porcentaje",
        color="Parentesco",
        title="Parentesco de la persona agresora con {} que han sufrido violencias".format(
            string
        ),
        barmode="group",
        color_discrete_sequence=COLORS,
    )
    fig.update_layout(
        legend_title="Parentesco con el agresor(a):",
        font=dict(family="Arial", size=18, color="black"),
    )
    fig.update_yaxes(title=yaxes)
    st.plotly_chart(fig)


def identification_aggressor_violence_graph(
    df: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
    else:
        yaxes = "% de personas"
    fig = px.bar(
        kinship_identification_violences(df),
        x="Violencia",
        y="Porcentaje",
        color="Identificación",
        barmode="group",
        text_auto="True",
        color_discrete_map={"Sí": COLORS[3], "No": COLORS[1]},
    )
    fig.update_layout(
        title="Identificación del agresor",
        xaxis_title="Violencia",
        yaxis_title=yaxes,
        legend_title="¿Identificó al agresor?",
        font=dict(
            family="Arial",
            color="black",
        ),
    )
    fig.update_traces(
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        texttemplate="%{value} %",
    )
    st.plotly_chart(fig)


def sex_violence_graph(df: pd.DataFrame, sex: list) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
    else:
        yaxes = "% de personas"
    fig = px.bar(
        sex_aggressor_violence(df),
        x="Violencia",
        y="Porcentaje",
        color="Sexo",
        barmode="group",
        color_discrete_sequence=[COLORS[1], COLORS[0], COLORS[2:]],
        text_auto=True,
    )
    fig.update_layout(
        title="Sexo del agresor por tipo de violencia",
        xaxis_title="Violencia",
        yaxis_title=yaxes,
        legend_title="Sexo rdel agresor(a)",
        font=dict(
            family="Arial",
            size=18,
            color="black",
        ),
    )
    fig.update_traces(
        textfont_size=18,
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        texttemplate="%{value: } %",
    )
    st.plotly_chart(fig)


def sex_kinship_by_violence_graph(
    df: pd.DataFrame, selected_violence: str, title: str, sex: list
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        xaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        xaxes = "% de hombres"
    else:
        xaxes = "% de personas"
    tbl = sex_kinship_by_violence(df, selected_violence)
    if tbl is None:
        st.write(
            "Para {} no hay información asociada al parentesco.".format(
                title.casefold()
            )
        )
    else:
        tbl.sort_values("Parentesco", ascending=False, inplace=True)
        fig = go.Figure()

        # Adding Male data to the figure
        fig.add_trace(
            go.Bar(
                y=tbl.index,
                x=tbl.Hombre,
                name="Hombre",
                orientation="h",
                text=-1 * tbl.Hombre.values.astype("float"),
                marker_color="rgb(57, 105, 172)",
            )
        )

        # Adding Female data to the figure
        fig.add_trace(
            go.Bar(
                y=tbl.index,
                x=tbl.Mujer,
                name="Mujer",
                orientation="h",
                text=tbl.Mujer,
                marker_color="rgb(149, 27, 129)",
            )
        )

        # Updating the layout for our graph
        fig.update_layout(
            title=" ".join(
                [
                    "Sexo del agresor(a) y parentesco con la víctima de",
                    title.casefold(),
                ]
            ),
            legend_title="Sexo del agresor",
            title_font_size=22,
            barmode="relative",
            bargap=0.0,
            bargroupgap=0.5,
            xaxis=dict(
                title=xaxes,
                title_font_size=14,
                tickvals=[-100, -50, 0, 0, 50, 100],
                ticktext=["100", "50", "0", "0", "50", "100"],
            ),
            yaxis=dict(
                ticklabelposition="inside",
            ),
            font=dict(
                family="Arial",
                size=18,
                color="black",
            ),
        )
        fig.update_traces(
            textfont_size=10,
            textangle=0,
            textposition="outside",
            cliponaxis=False,
            texttemplate="%{text}%",
        )

        st.plotly_chart(fig)


def occupations_violences_graph(
    df: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        xaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        xaxes = "% de hombres"
    else:
        xaxes = "% de personas"
    tbl = occupations_violences(df)
    fig = px.bar(
        tbl,
        x="Porcentaje",
        y="Violencia",
        color="Ocupación",
        orientation="h",
        color_discrete_sequence=BALTLOW_100_SCRAMBLED_SWATCHES,
    )
    fig.update_layout(
        title="Ocupaciones más frecuentes por violencia sufrida",
        xaxis_title=xaxes,
        yaxis_title="Violencia",
        legend_title="Ocupaciones",
        font=dict(
            family="Arial",
            size=18,
            color="black",
        ),
    )

    st.plotly_chart(fig)


def location_violence_graph(df: pd.DataFrame, sex: list) -> plotly.graph_objects.Figure:
    tbl = location_violence(df)
    fig = px.bar(
        tbl.sort_values("Estado"),
        x="Porcentaje",
        y="Violencia",
        color="Estado",
        orientation="h",
        color_discrete_sequence=BALTLOW_100_SCRAMBLED_SWATCHES,
    )
    fig.update_layout(
        title="Ubicación de las víctimas por violencia sufrida",
        xaxis_title="% de mujeres",
        yaxis_title="Violencia",
        legend_title="Estado",
        font=dict(
            family="Arial",
            size=18,
            color="black",
        ),
    )

    st.plotly_chart(fig)


def frequency_all_violence_graph(
    df: pd.DataFrame,
    sex: list,
) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        xaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        xaxes = "% de hombres"
    else:
        xaxes = "% de personas"
    tbl = frequency_violence(df)
    fig = px.bar(
        tbl,
        y="Porcentaje",
        x="Violencia",
        color="Frecuencia",
        orientation="v",
        barmode="group",
        color_discrete_sequence=COLORS,
    )
    fig.update_layout(
        title="Cantidad de veces que la víctima reporta haber sufrido la violencia",
        xaxis_title=xaxes,
        yaxis_title="Violencia",
        legend_title="Frecuencias",
        font=dict(
            family="Arial",
            size=18,
            color="black",
        ),
    )
    fig.update_traces(
        textfont_size=18,
        textangle=0,
        cliponaxis=False,
        marker_line_color="white",
        texttemplate="%{value} %",
    )

    st.plotly_chart(fig)


def reactions_graph(df: pd.DataFrame, sex: list) -> plotly.graph_objects.Figure:
    if sex == ["Mujer"]:
        yaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        yaxes = "% de hombres"
    else:
        yaxes = "% de personas"
    tbl_reactions = principal_reactions(df, table=True)
    fig = px.bar(
        tbl_reactions.sort_values("Porcentaje", ascending=False),
        y=tbl_reactions["Porcentaje"],
        x=tbl_reactions.index,
        text_auto=True,
    )
    fig.update_layout(
        title="Reacción de la víctima al sufrir la(s) violencia(s)",
        xaxis_title="Reacciones",
        yaxis_title=yaxes,
        font=dict(
            family="Arial",
            color="black",
        ),
    )
    fig.update_traces(
        textangle=0,
        textposition="outside",
        cliponaxis=False,
        showlegend=False,
        marker_color=COLORS[0],
        marker_line_color="white",
        texttemplate="%{value:.2f} %",
    )
    st.plotly_chart(fig)


def reactions_violence_graph(
    df: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    tbl = reactions_violence(df)
    if sex == ["Mujer"]:
        xaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        xaxes = "% de hombres"
    else:
        xaxes = "% de personas"
    fig = px.bar(
        tbl,
        x="Porcentaje",
        y="Violencia",
        color="Reacciones",
        orientation="h",
        color_discrete_sequence=BALTLOW_100_SCRAMBLED_SWATCHES,
    )
    fig.update_layout(
        title="Reacciones por violencia sufrida",
        xaxis_title=xaxes,
        yaxis_title="Violencia",
        legend_title="Reacciones",
        font=dict(
            family="Arial",
            size=18,
            color="black",
        ),
    )

    st.plotly_chart(fig)


def knowledge_violences_names_graph(
    df: pd.DataFrame, sex: list
) -> plotly.graph_objects.Figure:
    tbl = knowledge_violences_names(df)
    if sex == ["Mujer"]:
        xaxes = "% de mujeres"
    elif sex == ["Hombre"]:
        xaxes = "% de hombres"
    else:
        xaxes = "% de personas"
    fig = px.bar(
        tbl,
        y="Porcentaje",
        x="Violencia",
        color="Conocimiento",
        barmode="group",
        orientation="v",
        color_discrete_sequence=COLORS,
        text_auto=True,
    )
    fig.update_layout(
        title="Conocimiento de la(s) violencia(s)",
        xaxis_title=xaxes,
        yaxis_title="Violencia",
        legend_title="Conocimiento del nombre de la violencia",
        font=dict(
            family="Arial",
            size=18,
            color="black",
        ),
    )

    fig.update_traces(
        textangle=0,
        textposition="outside",
        texttemplate="%{value:.2f} %",
    )
    st.plotly_chart(fig)
