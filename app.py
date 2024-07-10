import streamlit as st
#Se define la API Key de Google y el modelo de Gemini a utilizar
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Se carga las variables de entorno desde el archivo .env
load_dotenv()

# Se obtiene la API Key de las variables de entorno
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash',generation_config={"response_mime_type": "application/json"})

#Función que recibe como parámetro el contexto y el prompt y devuelve la respuesta
def consultaTelefonoMovil(context, prompt):
  try:
    response = model.generate_content(context + prompt)
    return response.text
  except Exception as e:
    print("Se ha producido un error",e.args[0])
    st.write("Se ha producido un error", e.args[0])


st.title('BuscaMovil')
#Se genera un contenedor para el header y el input de la aplicación
c=st.container()
c.subheader('Introduce el modelo de teléfono celular para obtener sus características técnicas en formato JSON')
#c.subheader('Como funciona: Ingresa el modelo de celular y presiona el botón Submit')
context="Como asistente de búsqueda de teléfonos celulares, necesito que obtengas las características técnicas de un modelo de teléfono celular y las organices en formato JSON. Si el modelo ingresado no es encontrado en 15 segundos, el asistente mostrará un mensaje indicando al usuario que no se encontró el modelo. El modelo de teléfono celular es: "
mobile_model = c.text_input('Modelo de celular')
submit = c.button('Submit')
#Se ejecuta la función si se ha pulsado el botón de Submit
if submit:
    if mobile_model:
       #La respuesta del modelo es formateada en JSON
       response=consultaTelefonoMovil(context, mobile_model)
       response_formatted=st.json(response)
    else:
       c.write('Por favor ingresa el modelo de celular')

