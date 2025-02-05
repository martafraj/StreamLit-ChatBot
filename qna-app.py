import streamlit as st
from dotenv import load_dotenv
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient

def get_answer(question):
    load_dotenv()
    ai_endpoint = os.getenv('AI_SERVICE_ENDPOINT')
    ai_key = os.getenv('AI_SERVICE_KEY')
    ai_project_name = os.getenv('QA_PROJECT_NAME')
    ai_deployment_name = os.getenv('QA_DEPLOYMENT_NAME')

    credential = AzureKeyCredential(ai_key)
    ai_client = QuestionAnsweringClient(endpoint=ai_endpoint, credential=credential)
    response = ai_client.get_answers(question=question, project_name=ai_project_name, deployment_name=ai_deployment_name)
    
    if response.answers:
        return response.answers[0].answer
    else:
        return "No se encontró respuesta."

st.set_page_config(page_title="Chatbot AI", page_icon="🪚", layout="centered")

# Estilos CSS para un diseño oscuro completamente nuevo
st.markdown("""
    <style>
        body {
            background-color: #e33b0e;  /* Fondo gris muy oscuro */
            color: #F2F2F2;  /* Texto muy claro */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        .stTextInput, .stTextArea {
            border: none !important;
            border-radius: 20px;
            padding: 15px;
            background-color: #664942;
            color: #E6E6E6;
            font-size: 16px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
        }
        .stTextInput:focus, .stTextArea:focus {
            outline: none;
            box-shadow: 0 0 10px 2px rgba(255, 105, 180, 0.7);
            background-color: #333333;
        }
        .stButton>button {
            background-color: #664942;  /* Color de botón ajustado a #663300 */
            color: #FFFFFF;
            border-radius: 25px;
            padding: 14px 30px;
            font-size: 18px;
            font-weight: bold;
            transition: background-color 0.3s ease, transform 0.2s ease;
            box-shadow: 0 5px 15px rgba(102, 51, 0, 0.3);
        }
        .stButton>button:hover {
            background-color: #362824;  /* Un tono ligeramente más oscuro */
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(102, 51, 0, 0.5);
        }
        .chat-container {
            background-color: #232323;
            padding: 40px;
            border-radius: 25px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.5);
            max-width: 600px;
            margin: 20px auto;
        }
        h1 {
            font-size: 36px;
            text-align: center;
            margin-bottom: 20px;
        }
        .stTextInput, .stTextArea {
            margin-bottom: 20px;
        }
        .logo-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Logo centrado
st.markdown('<div class="logo-container"><img src="https://www.zarla.com/images/zarla-magia-madera-1x1-2400x2400-20210809-r63gxcvytyvwbmtxxt6m.png?crop=1:1,smart&width=250&dpr=2" width="250" /></div>', unsafe_allow_html=True)

st.title("🪚 Chatbot Carpentry")

# Solicitar al usuario que ingrese su pregunta
user_input = st.text_input("Write your question here (English only):")

if st.button("Enviar"):
    if user_input:
        answer = get_answer(user_input)
        st.write(f"**Response: ** {answer}")
    else:
        st.warning("Please write a question before submitting")
st.markdown("</div>", unsafe_allow_html=True)
