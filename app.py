import streamlit as st 

st.title("Mi aplicación")
st.sidebar.header("Esta aplicación es solo un demo")
st.sidebar.image("http://fcq.uach.mx/images/notas/IQ/IQ.jpg")

boton = st.button("Globos")
if boton:
  st.balloons()
  st.snow()

