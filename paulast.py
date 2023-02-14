import streamlit as st

mensaje =":red[elige]"

st.markdown(mensaje)


opciones = ("perro","gato","oveja","serpiente")
resultado = st.radio("ANIMALES" ,opciones)
 
if opciones == resultado[0]:
	st.write("woof")
  
if opciones == resultado[1]:
 	st.balloons()
	
if opciones == resultado[2]:
	st.write("beeeee")
	
if opciones == resultado[3]:
	st.write("ssssssssss")
 
