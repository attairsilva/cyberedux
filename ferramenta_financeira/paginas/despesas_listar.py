import streamlit as st
# necessidade de recursos do panda para abrir e grava em um CSV
import pandas as pd

st.header("DESPESAS CADASTRADAS")

def logout():   
    st.session_state.sessao  = None # sessao para NONE si do sistema
    st.rerun()

def inserir_despesa():
  despesa = st.text_input('Descrição da despesa')
  valor = st.number_input('Valor da Despesa')
  df = pd.DataFrame(
         [
             {"despesa": despesa, "valor": valor }
         ]
  )

def exibir_despesa():
    df = pd.read_csv('dados_csv/despesas.csv')
    if len(df ) == 0:
        st.write("Data frame de despesas está vazio.") 
    else:
        table = st.dataframe(df)
    

exibir_despesa()
  
