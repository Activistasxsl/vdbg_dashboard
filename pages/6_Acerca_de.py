import streamlit as st

from functions.widgets import menu


st.set_page_config(
    page_title="Datos demográficos - Dashboard de VDBG",
    page_icon="static/LOGO 6.png",
    layout="wide",
)

menu()

st.markdown(
    """
    # Violencias Digitales Basadas en Género - Dashboard (vdbg_dashboard)

    Aplicación web interactiva desarrollada con Streamlit para visualizar los
    datos del estudio sobre violencias digitales basadas en género para
    Venezuela, años 2023 y 2024.

    La aplicación fue implementada por Anavelyz Pérez
    ([@anavelyz](https://github.com/Anavelyz)) y Yurely Camacho
    ([@yurely](https://github.com/YurelyCamacho)) quienes también son
    responsables del análisis exploratorio de datos, la limpieza y los
    resultados presentados.

    Además de Streamlit, se utilizaron bibliotecas de Python como Pandas para el
    manejo de datos, Plotly y Matplotlib para crear gráficos, y Geopandas para
    análisis geográfico. La aplicación se encuentra desplegada gracias al
    servicio de Streamlit Cloud.

    ## Metodología de la encuesta base de la información

    Se aplicó un cuestionario, en el año 2023 y 2024, disponible en línea entre
    los meses de mayo y octubre de cada año. El cuestionario aplicado constó de
    27 preguntas, agrupadas en 3 secciones, y fue validado por activistas
    feministas de nuestro país. Algunas de estas preguntas cuentan, a su vez,
    con preguntas anidadas. Cada participante dispuso de un texto informativo a
    modo de consentimiento informado, donde se le explicó el uso que se daría a
    los datos recolectados.

    Las tres secciones de la encuesta comprendieron una sección de contexto, en
    la que buscamos conocer ubicación geográfica, edad, género con el que se
    identificaba la persona encuestada, ocupación, uso de Internet, así como si
    su uso de Internet se había incrementado luego de la pandemia por COVID-19.

    La segunda sección comprendió preguntas situacionales en las que abordamos
    descripciones de escenarios de distintas violencias digitales, buscando su
    identificación por parte de las personas encuestadas, así como poder relevar
    información de interés acerca de frecuencia, relación con la persona
    agresora, medio digital a través del cual ocurrió, y edad aproximada en la
    que sucedió, entre otras cosas.

    Finalmente, la tercera sección, comprendió preguntas que nos permitieron
    indagar sobre la información que tenían las personas encuestadas sobre las
    violencias digitales, el marco legal vigente en nuestro país, así como
    conocer qué hicieron como respuesta al vivir estas violencias y si conocían
    a otras mujeres que hubieran vivido también violencias digitales.

    El tipo de muestreo utilizado determina que los resultados obtenidos sean de
    carácter descriptivo. en este sentido, la metodología del análisis realizado
    incluye:

    1. Auditoría y limpieza de datos.
    2. Análisis tabular y gráfico
    3. Conclusiones

    El proceso de auditoría y limpieza de datos incluyó un análisis de las
    variables operacionalizadas, con el propósito de elaborar una descripción y
    renombrado de éstas. Posteriormente se procedió a verificar e interpretar la
    falta de respuesta en algunas preguntas y, finalmente se realizó una
    estandarización de las respuestas a preguntas abiertas o de tipeo.

    Las tareas de descripción y análisis de resultados se realizó utilizando
    software libre y apoyándonos en el lenguaje de programación Python, con la
    ayuda de algunos de sus paquetes y bibliotecas: Pandas - Python Data
    Analysis Library, NumPy, Matplotlib, Plotly. Se utilizó Jupyter-lab como
    entorno de desarrollo interactivo donde se puede manejar, al mismo tiempo,
    código y texto.

    Finalmente, debemos dejar establecida nuestra perspectiva feminista sobre el
    tema de las violencias digitales basadas en género. Por tanto, aunque
    buscamos que el diseño de la encuesta recogiera información relativa al
    género con el que se identifica la persona que respondía, quienes
    participaron se identificaron de forma significativa con el género femenino.
    Por esta razón, se encuentran ambos resultados tabulados, y pueden
    consultarse por separado seleccionando la opción correspondiente en el menú
    lateral de la aplicación.

    """
)
