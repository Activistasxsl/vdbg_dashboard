import os

import pandas as pd

from functions.constants_values import (
    AGE_CATEGORIES,
    HOME_WORK,
    INTERNET_TIMES,
    SOCIAL_WORK,
    VIOLENCES,
)


def get_data(
    period: list,
    sex: list,
) -> pd.DataFrame:
    """
    Get data from csv file

    Parameters
    ----------
    sex : list
        List of sex
    period : list
        List of period

    Returns
    -------
    pd.DataFrame
        Dataframe with data
    """
    if os.path.exists("data/clean_data.pkl"):
        df = pd.read_pickle("data/clean_data.pkl")
    else:
        df = pd.read_pickle("/raw/datos_23_24.pkl")

        # Convert data types
        parentesco_lista = [
            s for s in df.columns if "parentesco_" in s or "identificacion_" in s
        ]
        df.loc[:, parentesco_lista] = df[parentesco_lista].astype("category")

        df.edad = df.edad.astype("category").cat.set_categories(
            AGE_CATEGORIES, ordered=True
        )
        df.horas_internet = df.horas_internet.astype("category").cat.set_categories(
            INTERNET_TIMES,
            ordered=True,
        )
        df.loc[:, "telegram"] = df.telegram.apply(str.strip)
        for i in VIOLENCES:
            df.loc[:, i] = df[i].apply(str.strip).apply(str.capitalize)
        for i in SOCIAL_WORK:
            df.loc[df["ocupacionO"] == i, "ocupacion"] = "Trabajo social"
        for i in HOME_WORK:
            df.loc[df["ocupacionO"] == i, "ocupacion"] = "Ama de casa"
        df.loc[df["ocupacionO"] == "Abogado", "ocupacion"] = "Abogado(a)"
        df.loc[df["ocupacionO"] == "Psicologa ", "ocupacion"] = "Psicólogo(a)"

        sex_list = [s for s in df.columns if "sexo_" in s]
        for i in sex_list:
            df.loc[:, i] = (
                df[i]
                .astype("category")
                .cat.set_categories(["Mujer", "Hombre", "Un grupo de personas"])
            )

        df.to_pickle("data/clean_data.pkl")

    # Filter by period (if necessary)
    if len(period) == 1:
        df = df.query("YEAR == @period[0]")

    # Filter by sex (if necessary)
    if len(sex) == 1:
        df = df.query("sexo == @sex[0]")

    return df


# def get_data_by_violence(df: pd.DataFrame, violence: list) -> pd.DataFrame:
#     """
#     Get data by violence

#     Parameters
#     ----------
#     df : pd.DataFrame
#         Dataframe with data
#     violence : list
#         List of violence

#     Returns
#     -------
#     pd.DataFrame
#         Dataframe with data
#     """
#     df = df.copy()
#     for i in violence:
#         df.loc[:, i] = df[i].apply(str.strip).apply(str.capitalize)
#     return df
