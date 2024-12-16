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
