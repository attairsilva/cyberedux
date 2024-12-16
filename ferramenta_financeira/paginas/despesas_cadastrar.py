import streamlit as st
# necessidade de recursos do panda para abrir e grava em um CSV
import pandas as pd

st.header("CADASTRAR DESPESAS")

def inserir_despesa():
  codigo = str(st.number_input('Código da despesa',format="%0.0f"))
  despesa = st.text_input('Descrição da despesa')
  valor = str(st.number_input('Valor da Despesa'))
  processa=st.button('SALVAR',use_container_width=True)
  if "dicionario_despesa" not in st.session_state:
        st.session_state.dicionario_despesa= {}
  if processa:
        st.session_state.dicionario_despesa[codigo]= despesa
        st.session_state.dicionario_despesa[codigo]= valor
        df = pd.read_csv('dados_csv/despesas.csv')
        
      
 
inserir_despesa()

  