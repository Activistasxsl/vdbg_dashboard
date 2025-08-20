import pandas as pd

INTERNET_TIMES = [
    "No lo utilizo diariamente",
    "Menos de 2 horas",
    "2-4 horas",
    "5-7 horas",
    "Más de 7 horas",
]

AGE_CATEGORIES = [
    "14-17",
    "18-25",
    "26-40",
    "41-60",
    "Más de 60",
]

VIOLENCE_NAMES_DICT = {
    "identidad": "Duplicación de identidad",
    "ciberacoso": "Ciberacoso",
    "doxxing": "Doxxing",
    "mobbing": "Mobbing",
    "ciberdifamacion": "Ciberdifamación",
    "stalking": "Cibervigilancia (stalking)",
    "ciberextorsion": "Ciberextorsión",
    "grooming": "Grooming",
    "phishing_vs": "Phishing/Vishing/Smishing",
    "trata": "Trata de personas en línea",
    "explotacion": "Captación con fines de explotación sexual",
    "exclusion": "Exclusión digital",
    "cyberflashing": "Cyberflashing",
    "deepfake": "Deepfake",
    "clonacion": "Clonación de aplicaciones",
}

SOCIAL_MEDIA_NAMES = {
    "twitter": "Twitter",
    "facebook": "Facebook",
    "whatsapp": "WhatsApp",
    "telegram": "Telegram",
    "correo": "Correo",
    "tiktok": "TikTok",
    "sms": "SMS",
    "citas": "Apps de citas Tinder, Grindr, Bumble, etc" "Twitter",
    "videojuegos": "Videojuegos en línea",
    "estudio": "Plataformas de estudio: Teams, Zoom, Google Classroom, aulas virtuales, etc",
    "trabajo": "Plataformas de trabajo: Teams, Zoom, Meet, Slack, etc",
    "red": "Red interna del trabajo",
    "otra": "Otra",
    "instagram": "Instagram",
    "llamadas": "Llamadas telefónicas",
}

VIOLENCES = list(VIOLENCE_NAMES_DICT.keys())

KEY_VIOLENCE_NAMES = {v: k for k, v in VIOLENCE_NAMES_DICT.items()}

list_key_violence_names = sorted(KEY_VIOLENCE_NAMES.keys())

VIOLENCES_FORMAL_NAMES = list(VIOLENCE_NAMES_DICT.values())


def columns_for_violences(df: pd.DataFrame) -> list:
    """
    Get the columns for each violence

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with data

    Returns
    -------
    dict
        A dictionary with the name of the violence as key and a list of columns
        that contain this violence as value
    """
    names_columns = {}
    for i in VIOLENCES:
        names_columns[i] = [s for s in df.columns[:-32] if i in s]

    return names_columns


SOCIAL_WORK = [
    "Defensora de DDHH de las mujeres",
    "Trabajo social ",
    "Trabajador social ",
    "Trabajadora Social",
    "Trabajadora Social ",
    "Trabajadora social. Actriz militante afrofemisnita",
    "Trabajadora humanitaria",
    "Promotora Social ",
    "Trabajadora Humanitaria",
    "Trabajadora de organización internacional ",
    "Gestora de casos en VBG Y TDP ",
    "El feminismo ",
    "Defensora de Mujeres ",
    "Atención a víctimas de VBG" "Defensora de DDHH de las mujeres",
    "Atención a víctimas de VBG",
    "El feminismo ",
    "Trabajando social ) Ayuda humanista",
]

HOME_WORK = [
    "Del hogar ",
    "Crianza y cuidado del hogar ",
    "Ama de casa",
    "Trabajo on line. Trabajadora del hogar",
]

SOCIAL_MEDIA = [
    "facebook",
    "twitter",
    "instagram",
    "tiktok",
    "discord",
    "slack",
    "citas",
    "videojuegos",
    "whatsapp",
    "telegram",
    "reddit",
    "estudio",
    "linkedin",
    "twich",
    "youtube",
    "pinterest",
    "flickr",
]


REACTIONS = {
    "reaccion_ignorar": "Ignorar al agresor",
    "reaccion_contar": "Contarle a un amigo(a) o familiar",
    "reaccion_ayuda": "Acudir a un centro de ayuda o denuncia",
    "reaccion_reportar": "Reportar el perfil o publicación en la red social",
    "reaccion_internet": "Reducir el uso en internet",
    "reaccion_borrar": "Borrar la aplicación donde ocurrió",
    "reaccion_eliminar": "Eliminar la cuenta de usuario",
    "reaccion_crear": "Crear una cuenta de usuario distinta",
    "reaccion_bloquear": "Bloquear a la persona agresora",
    "reaccion_enfrentar": "Enfrentar a la persona agresora",
}


COLORS = [
    "#F29D6D",
    "#114360",
    "#FCBFD6",
    "#828231",
    "#FDB4B4",
    "#C09036",
    "#FDAEA2",
]


BALTLOW_100_SCRAMBLED_SWATCHES = [
    # "#011959",
    # "#FACCFA",
    "#828231",
    "#226061",
    "#F29D6D",
    "#4D734D",
    "#114360",
    "#C09036",
    "#FDB4B4",
    "#DD954D",
    "#356A59",
    "#FCBFD6",
    "#175262",
    "#677B3E",
    "#A18A2B",
    "#0D315D",
    "#FCA890",
    "#FBC6E8",
    "#2B655E",
    "#B18D2F",
    "#5A7745",
    "#FDAEA2",
    "#CF9340",
    "#0F3B5F",
    "#E9995C",
    "#FDBAC4",
    "#416F53",
    "#91862D",
    "#1B5962",
    "#08255B",
    "#747E38",
    "#134B61",
    "#F9A380",
    "#8A842F",
    "#0E365E",
    "#124761",
    "#154F62",
    "#E39754",
    "#7B8034",
    "#1E5D62",
    "#99882C",
    "#195662",
    "#0B2B5C",
    "#FDB7BC",
    "#C8913B",
    "#FCC3DF",
    "#EE9B64",
    "#A98C2C",
    "#FDB1AB",
    "#FDBCCD",
]
