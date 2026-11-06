import streamlit as st #Biblioteca para criar a interface web
import pandas as pd #leitura e manipulaçção de dados
import json #trabalhar com arquivos JSON

#Importa o vetorizador q transforma texto em valores num 
from sklearn.feature_extraction.text import TfidfVectorizer
 
#Importa o algoritmo de classificação supervisionada
from sklearn.linear_model import LogisticRegression

#Importa op Pipeline p organizar etapas do modelo 
from sklearn.pipeline import Pipeline

#1 Configuração do STREAMILIT
st.set_page_config(
        page_title= "Chatbot Operadora cartão", #Titulo aba 
        page_icon="💳", #icone aba 
        layout="centered", #centralizar conteudo 
)
#Exibir titulo principal da aplicação
st.title("🤖 Chatbot Atendimento - Operadora Cartão" )
