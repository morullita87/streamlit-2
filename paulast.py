import streamlit as st

mensaje =":red[elige]"

st.markdown(mensaje)


opciones = ("perro","gato","oveja","serpiente")
resultado = st.radio("ANIMALES" ,opciones)
 
if resultado == opciones[0]:
	st.write("woof")
  
if resultado == opciones[1]:
 	st.balloons()
	
if resultado == opciones[2]:
	st.write("beeeee")
	
if resultado == opciones[3]:
	st.write("ssssssssss")
 
