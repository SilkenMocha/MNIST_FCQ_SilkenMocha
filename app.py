import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np


st.title("Aplicación de Reconocimiento de tipo de generación de Pokemones")

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  
  if label == 0:
    st.subheader ("Es de primera generación")

  if label == 1:
    st.subheader ("Es de segunda generación")

  if label == 2:
    st.subheader ("Es de tercera generación")

  if label == 3:
    st.subheader ("Es de cuarta generación")

  if label == 4:
    st.subheader ("Es de quinta generación")

  if label == 5:
    st.subheader ("Es de sexta generación")
  
  st.write(label)
  #st.snow()
  #st.sidebar.image(uploaded_file)
  st.image(uploaded_file)
