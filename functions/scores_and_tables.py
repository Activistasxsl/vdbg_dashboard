import geopandas as gpd
import pandas as pd

from functions.constants_values import (
    REACTIONS,
    SOCIAL_MEDIA,
    SOCIAL_MEDIA_NAMES,
    VIOLENCE_NAMES_DICT,
    VIOLENCES,
    VIOLENCES_FORMAL_NAMES,
)


def table_by_sex(df: pd.DataFrame) -> pd.DataFrame:
    sex_tbl = df.sexo.value_counts()
    return sex_tbl


def violence_victims_percentages(df: pd.DataFrame) -> pd.DataFrame:
    dic = {}
    for i in VIOLENCES:
        dic[VIOLENCE_NAMES_DICT[i]] = df[[i]].value_counts().sort_index()

    number_victims = pd.DataFrame.from_dict(dic, orient="index").fillna(0)
    number_victims = number_victims.set_axis(["No", "Sí"], axis=1)
    victims_violence_percentages = round(number_victims / len(df) * 100, 2)
    return victims_violence_percentages


def average_violence(df: pd.DataFrame, number_victims: bool = False) -> int:
    pd.set_option("future.no_silent_downcasting", True)
    df[VIOLENCES] = df[VIOLENCES].replace({"No": 0, "Sí": 1})
    number_violences = pd.DataFrame(df[VIOLENCES].T.sum().value_counts()).sort_index()
    if number_victims:
        return number_violences[1:].sum().iloc[0]
    else:
        average_violences = int(
            round(
                (number_violences.index * number_violences["count"]).sum()
                / number_violences.sum().iloc[0],
                0,
            )
        )
    return average_violences


def known_violences_percentage(df: pd.DataFrame) -> float:
    tbl = round(df.vdbg.value_counts() / len(df) * 100, 2)
    percentage = tbl["Sí"]
    return percentage


def internet_use_growth_percentage(df) -> float:
    tbl = round(df.covid_aumento.value_counts() / len(df) * 100, 2)
    percentage = tbl["Sí"]
    return percentage


def known_laws_percentage(df: pd.DataFrame) -> float:
    tbl = round(df.leyes_normas.value_counts() / len(df) * 100, 2)
    percentage = tbl["Sí"]
    return percentage


def table_gender_sex(df: pd.DataFrame) -> pd.DataFrame:
    sex_tbl = df[["genero", "sexo"]].value_counts().reset_index()
    return sex_tbl


def age_tables(df: pd.DataFrame) -> pd.DataFrame:
    ages = pd.DataFrame(df.edad.value_counts()).sort_index()
    age_percentages = round(ages / ages.sum() * 100, 2)["count"].astype(str) + " %"

    return ages, age_percentages


def answers_by_state(df: pd.DataFrame) -> pd.DataFrame:
    answers_state = df.estado.value_counts()
    map_file = "./Estados_Venezuela/Estados_Venezuela.shp"
    df_mapa = gpd.read_file(map_file)
    ls_info = []
    for i in df_mapa.ESTADO:
        if i in answers_state.index:
            ls_info.append(answers_state.loc[i])
        else:
            ls_info.append(0)
    df_mapa["Personas"] = ls_info
    return df_mapa


def ten_common_occupations(df: pd.DataFrame) -> pd.DataFrame:
    df_occupations = (
        pd.DataFrame(df.ocupacion.value_counts())
        .rename_axis(index={"ocupacion": "Ocupación"})
        .rename(columns={"count": "Nº de personas"})
    )
    df_occupations["%"] = round(df_occupations / len(df) * 100, 2)
    return df_occupations.drop("Otra")[:10].reset_index().sort_values("%")


def post_covid_internet(df: pd.DataFrame) -> pd.DataFrame:
    df_covid = df.covid_aumento.value_counts()
    return df_covid


def social_media_use(df: pd.DataFrame) -> pd.DataFrame:
    dicts = {}
    for i in SOCIAL_MEDIA:
        dicts[i.capitalize()] = (
            df[[i]].value_counts().reset_index().set_index(i)["count"]
        )
    tbl_social_media = round(
        (
            pd.DataFrame.from_dict(dicts, orient="index").fillna(0)[
                [
                    "Menos de 2 horas",
                    "2-4 horas",
                    "5-7 horas",
                    "Más de 7 horas",
                    "No la utilizo",
                ]
            ]
            / len(df)
        )
        * 100,
        2,
    )
    return tbl_social_media


def incidence_table_by_violence_name(df: pd.DataFrame, selected_violence: str):
    df.loc[:, selected_violence] = df.loc[:, selected_violence].replace(
        {"No": 0, "Sí": 1},
    )
    columns = [s for s in df.columns[:-32] if selected_violence in s]
    info_selected_violence = df.query("{} == 1".format(selected_violence))[columns]
    return info_selected_violence


def knowledge_violences(df: pd.DataFrame) -> pd.DataFrame:
    columns = [s for s in df.columns if "vdbg_" in s]
    tbl = df[columns[1:]].sum().to_frame()
    tbl.index = VIOLENCES
    tbl.rename(
        index=VIOLENCE_NAMES_DICT,
        columns={
            0: "cantidad",
        },
        inplace=True,
    )
    tbl_knowledge = round(tbl / len(df) * 100, 2)
    return tbl_knowledge


def quantile_for_number_violences(df: pd.DataFrame, quantile: float = 0.75) -> int:
    columns = [s for s in df.columns if "vdbg_" in s]
    q = df[columns[1:]].sum(axis=1).quantile(quantile)
    return int(q)


def process_age_ranges(df):
    columns = [s for s in df.columns if "edad_" in s]
    df_grouped = df[columns].apply(
        lambda x: pd.cut(
            x,
            bins=[0, 10, 15, 18, 25, 30, 40, 50, 60, 75],
            right=False,
        )
        .value_counts(normalize=True)
        .mul(100)
        .round(3)
        .rename_axis("Edad")
    )

    df_grouped = df_grouped.rename(
        columns={col: col[5:] for col in df.columns},
    )
    df_grouped = (
        df_grouped.stack(future_stack=True)
        .reset_index()
        .rename(columns={0: "Porcentaje"})
    )
    df_grouped["Edad"] = df_grouped["Edad"].astype(str)

    df_grouped["Violencia"] = df_grouped.level_1.map(
        VIOLENCE_NAMES_DICT,
    )
    return df_grouped


def social_media_violences(data: pd.DataFrame) -> pd.DataFrame:
    dfs = []
    for violence in VIOLENCES:
        df_violence = incidence_table_by_violence_name(
            data,
            violence,
        )
        if df_violence.empty:
            continue
        cols = [
            s
            for s in df_violence.columns
            if any(s.startswith(n) for n in SOCIAL_MEDIA_NAMES.keys())
        ]
        cols = cols[:-1]
        df = df_violence[cols].sum()
        df.index = [
            SOCIAL_MEDIA_NAMES[medio.split("_")[0]] for medio in df.index.values
        ]
        df = df / df_violence.iloc[:, 0].sum() * 100
        df.name = VIOLENCE_NAMES_DICT[violence]
        dfs.append(df)

    social_media_violences = (
        pd.concat(dfs, axis=1)
        .melt(
            ignore_index=False,
        )
        .reset_index()
    )
    social_media_violences.rename(
        columns={
            "index": "Medio",
            "variable": "Violencia",
            "value": "Porcentaje",
        },
        inplace=True,
    )
    return round(social_media_violences.fillna(0), 2)


def kinship_violences(df: pd.DataFrame, decimal: bool = True) -> pd.DataFrame:
    dfs = []
    kinship_violences_list = [
        "identidad",
        "ciberacoso",
        "doxxing",
        "ciberdifamacion",
        "stalking",
        "ciberextorsion",
        "explotacion",
        "cyberflashing",
        "deepfake",
        "clonacion",
    ]
    for violence in kinship_violences_list:
        df_violence = incidence_table_by_violence_name(
            df,
            violence,
        )
        tbl = (
            df_violence[
                [
                    s
                    for s in df_violence.columns
                    if "parentesco_" in s or "identificacion_" in s
                ][0]
            ]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
            .to_frame()
        )
        ls_index = [VIOLENCE_NAMES_DICT[violence]] * len(tbl)
        tbl["Violencia"] = ls_index
        dfs.append(tbl)

    kinship_violences_tbl = pd.concat(dfs)
    kinship_violences_tbl = kinship_violences_tbl.reset_index()
    kinship_violences_tbl.rename(
        columns={
            "index": "Parentesco",
            "proportion": "Porcentaje",
        },
        inplace=True,
    )
    if decimal:
        return round(kinship_violences_tbl, 2)
    else:
        return kinship_violences_tbl


def kinship_identification_violences(df: pd.DataFrame) -> pd.DataFrame:
    kinship_tbl = kinship_violences(df, False)
    dfs = []
    kinship_lost_violences_list = [
        "grooming",
        "phishing_vs",
        "trata",
    ]
    for violence in kinship_lost_violences_list:
        df_violence = incidence_table_by_violence_name(
            df,
            violence,
        )
        tbl = (
            df_violence[
                [
                    s
                    for s in df_violence.columns
                    if "parentesco_" in s or "identificacion_" in s
                ][0]
            ]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
            .to_frame()
        )
        ls_index = [VIOLENCE_NAMES_DICT[violence]] * len(tbl)
        tbl["Violencia"] = ls_index
        dfs.append(tbl)
    kinship_violences_tbl = pd.concat(dfs)
    kinship_violences_tbl = kinship_violences_tbl.reset_index()
    kinship_violences_tbl.rename(
        columns={
            "index": "Identificación",
            "proportion": "Porcentaje",
        },
        inplace=True,
    )
    kinship_identification = [
        "Fue mi ex-pareja en ese momento",
        "Fue mi pareja",
        "Fue un compañero(a) de trabajo",
        "Fue un familiar",
        "No conocía a quien me agredió, pero le identifiqué",
        "Teníamos una amistad",
    ]
    kinship_tbl["Identificación"] = kinship_tbl["Parentesco"].apply(
        lambda x: "Sí" if x in kinship_identification else "No"
    )
    kinship_identification_violences_tbl = (
        kinship_tbl.drop("Parentesco", axis=1)
        .groupby(["Violencia", "Identificación"])
        .sum()
    ).reset_index()

    ki_tbl = pd.concat(
        [kinship_identification_violences_tbl, kinship_violences_tbl],
        axis=0,
    ).reset_index(drop=True)
    return round(ki_tbl, 2)


def sex_aggressor_violence(df: pd.DataFrame) -> pd.DataFrame:
    columns = [s for s in df.columns if "sexo_" in s]
    dfs_list = []
    keys = []
    for col in columns:
        dfs_list.append(df[col].value_counts(normalize=True).mul(100).round(2))
        key = next(
            (
                name
                for name in VIOLENCES_FORMAL_NAMES
                if col.split("_")[1][:7] in name.casefold()
            ),
            None,
        )
        if key:
            keys.append(key)
    tbl_sex_violences = pd.concat(
        dfs_list,
        join="outer",
        keys=keys,
    )
    tbl_sex_violences.index.set_names(["Violencia", "Sexo"], inplace=True)
    tbl_sex_violences = tbl_sex_violences.reset_index()
    tbl_sex_violences.rename(columns={"proportion": "Porcentaje"}, inplace=True)
    return tbl_sex_violences


def sex_kinship_by_violence(df: pd.DataFrame, selected_violence: str) -> pd.DataFrame:
    df_violence = incidence_table_by_violence_name(df, selected_violence)
    cols = [
        s
        for s in df_violence.columns
        if s.startswith("sexo_") or s.startswith("parentesco_")
    ]
    if len(cols) < 2:
        return None
    else:
        df_sex_kinship = (
            df_violence[cols].value_counts(normalize=True).mul(100).round(2)
        )
        df_sex_kinship.index.names = ["Parentesco", "Sexo"]
        df_sex_kinship = df_sex_kinship.reset_index()
        tbl = df_sex_kinship.pivot(
            index="Parentesco", columns="Sexo", values="proportion"
        ).fillna(0)
        tbl.Hombre = tbl.Hombre * -1
    return tbl


def occupations_violences(occupation_violence_df: pd.DataFrame) -> pd.DataFrame:
    initial_df = occupation_violence_df[occupation_violence_df["ocupacion"] != "Otra"]
    keys = []
    dfs = []
    for violence in VIOLENCES:
        keys.append(VIOLENCE_NAMES_DICT[violence])
        occupation_violence_df = (
            initial_df[initial_df[violence] == 1]["ocupacion"]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )
        dfs.append(occupation_violence_df.sort_values(ascending=False)[:10])
    occupations_violences_tbl = pd.concat(
        dfs, keys=keys, names=["Violencia"]
    ).reset_index()
    occupations_violences_tbl.rename(
        columns={"ocupacion": "Ocupación", "proportion": "Porcentaje"}, inplace=True
    )
    return occupations_violences_tbl


def location_violence(df: pd.DataFrame) -> pd.DataFrame:
    keys = []
    dfs = []
    for violence in VIOLENCES:
        keys.append(VIOLENCE_NAMES_DICT[violence])
        state_df = (
            df[df[violence] == 1]["estado"]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )
        dfs.append(state_df)
    state_tbl = pd.concat(dfs, keys=keys, names=["Violencia"]).reset_index()
    state_tbl.rename(
        columns={"estado": "Estado", "proportion": "Porcentaje"}, inplace=True
    )
    return state_tbl


def frequency_violence(df: pd.DataFrame) -> pd.DataFrame:
    dfs = []
    keys = []
    freq_cols = [col for col in df.columns if "veces_" in col]
    for i in freq_cols:
        key = next(
            (
                name
                for name in VIOLENCES_FORMAL_NAMES
                if i.split("_")[1][:7] in name.casefold()
            ),
            None,
        )
        if key:
            keys.append(key)
        tbl = df[i].value_counts(normalize=True).mul(100).round(2)
        dfs.append(tbl)
    tbl = pd.concat(dfs, keys=keys, names=["Violencia", "Frecuencia"]).reset_index()
    tbl.rename(
        columns={"index": "Frecuencia", "proportion": "Porcentaje"}, inplace=True
    )
    return tbl


def principal_reactions(df: pd.DataFrame, table: bool = False) -> pd.DataFrame:
    num_victims = average_violence(df, number_victims=True)
    cols = [s for s in df.columns if "reaccion_" in s]
    tbl = df[cols].sum().sort_values(ascending=False).to_frame()
    tbl.rename(index=REACTIONS, inplace=True)
    tbl["Porcentaje"] = tbl.div(num_victims).mul(100).round(2)
    if table:
        return tbl
    else:
        return (
            tbl.iloc[0].name,
            round(tbl.iloc[0].Porcentaje, 2),
            tbl.iloc[1].name,
            round(tbl.iloc[1].Porcentaje, 2),
        )


def reactions_violence(df: pd.DataFrame) -> pd.DataFrame:
    dfs = []
    keys = []
    cols = [s for s in df.columns if "reaccion_" in s]
    df[VIOLENCES] = df[VIOLENCES].replace({"No": 0, "Sí": 1, "Si": 1})
    for violence in VIOLENCES:
        keys.append(VIOLENCE_NAMES_DICT[violence])
        info_selected_violence = df.query("{} == 1".format(violence))[cols]
        info_selected_violence = info_selected_violence.apply(
            pd.to_numeric, errors="coerce"
        ).fillna(0)
        if info_selected_violence.empty:
            continue
        tbl = round(
            info_selected_violence.sum().mul(100 / len(info_selected_violence)), 2
        )
        tbl.rename(index=REACTIONS, inplace=True)
        dfs.append(tbl)
    tbl_reactions_violence = pd.concat(
        dfs, keys=keys, names=["Violencia", "Reacciones"]
    )
    tbl_reactions_violence = tbl_reactions_violence.reset_index().rename(
        columns={0: "Porcentaje"}
    )
    return tbl_reactions_violence


def knowledge_violences_names(df: pd.DataFrame) -> pd.DataFrame:
    dfs = []
    keys = []
    for violence in VIOLENCES:
        keys.append(VIOLENCE_NAMES_DICT[violence])
        info_violence = (
            df.query("{} == 1".format(violence))["vdbg"]
            .value_counts(normalize=True)
            .mul(100)
            .round(2)
        )
        dfs.append(info_violence)
    tbl_ = pd.concat(dfs, keys=keys, names=["Violencia", "Conocimiento"])
    tbl_ = tbl_.reset_index().rename(columns={"proportion": "Porcentaje"})
    return tbl_


def ocupation_violence_medio(df: pd.DataFrame, ocupation: str) -> pd.DataFrame:
    df_filtered = df[df["ocupacion"] == ocupation].copy()
    individuals = len(df_filtered)

    if df_filtered.empty:
        return pd.DataFrame()

    dfs = []

    for violence in VIOLENCES:
        df_filtered.loc[:, violence] = df_filtered.loc[:, violence].replace(
            {"No": 0, "Sí": 1}
        )
        columns = [s for s in df_filtered.columns[:-32] if violence in s]

        info_selected_violence = df_filtered[df_filtered[violence] == 1][columns]

        if info_selected_violence.empty:
            continue

        cols = [
            s
            for s in info_selected_violence.columns
            if any(s.startswith(n) for n in SOCIAL_MEDIA_NAMES.keys())
        ]
        cols = cols[:-1]

        df_violence = info_selected_violence[cols].astype(int)

        violence_sum = df_violence.sum().to_frame().T
        violence_sum.rename(
            columns={
                s: SOCIAL_MEDIA_NAMES[s.split("_")[0]] for s in violence_sum.columns
            },
            inplace=True,
        )
        violence_sum["Violencia"] = VIOLENCE_NAMES_DICT[violence]
        dfs.append(violence_sum)

    if not dfs:
        return pd.DataFrame()

    result = pd.concat(dfs, ignore_index=True)
    result = result.melt(id_vars=["Violencia"], var_name="Medio")
    result.dropna(inplace=True)
    result = result[result.value > 0]
    result["Porcentaje"] = (result["value"] / individuals * 100).round(2)

    return result
