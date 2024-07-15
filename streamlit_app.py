python -m pip install streamlit

import streamlit as st
import adhesive_code
from PIL import Image


image_video = Image.open("anchor_1.jpg")

st.set_page_config(page_title="Diseño de Anclajes Adhesivos") #Establecer el título de la web page

with st.container():
    st.subheader("Anclajes Adhesivos Post-instalados (AAP)")
    st.title("Automatización del diseño de AAP bajo cargas de tensión")
    st.write("Proyecto Final de Carrera  - Universidad de Ingeniería y Tecnología")

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Variables de entrada")
        input_d = st.number_input("Diámetro del anclaje (mm):")
        input_hef = st.number_input("Longitud de embebido (mm):")
        input_ad = st.number_input("Tipo de adhesivo(0-epóxico, 1-grout, 2-cementicio):")
        input_fc_ad = st.number_input("Resistencia a la compresión del adhesivo (Mpa):")
        input_fc = st.number_input("Resistencia a la compresión del concreto (Mpa):")
        

    with right_column:
        st.image(image_video)
        input_bar = st.number_input("Tipo de anclaje (0-barra lisa, 1-barra corrugada, 2-CFRP, 3-GFRP):")
        input_fu = st.number_input("Resistencia última del anclaje (Mpa): ")
        if st.button("Predecir"):
            prediction = adhesive_code.app_adhesive(input_d, input_hef, input_ad, input_fc_ad, input_fc, input_bar, input_fu)
            st.write(f"   La predicción es: {prediction} kN")
