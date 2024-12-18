import streamlit as st
from datetime import datetime

# necessidade do vega_datasetse panda para recursos graficos, documentação do streamlit
# https://docs.streamlit.io/develop/api-reference/charts/st.bar_chart

st.header("RECEITAS")

def cadastrar_receita(dicionario):
    cont=0
    for i in enumerate(dicionario):
      cont+=1
    codigo= cont+1
    
    descricao = st.text_input(f'Descrição da receita - ID {codigo}')
    valor = str(st.number_input('Valor da receita'))
    data = st.date_input("Data da receita", format="DD/MM/YYYY")
   
    
    
    col1, col2  = st.columns(2)
    processa=col1.button('SALVAR',use_container_width=True)
    apagar=col2.button('APAGAR',use_container_width=True)
    
    if processa:
      receita = {}
      receita['descricao']=descricao
      receita['valor']=valor
      receita['data']=data
      dicionario[codigo]=receita
      
    if apagar:
      dicionario.clear()
    
    

      

if "dicionario_receita" not in st.session_state:
        st.session_state.dicionario_receita= {}
           
cont=0
for i in enumerate(st.session_state.dicionario_receita):
    cont+=1

cadastrar_receita(st.session_state.dicionario_receita)

st.write(f'## RECEITAS')

# dataInicio = st.date_input("Data de Inicio", format="DD/MM/YYYY")
# dataFim = st.date_input("Data Final", format="DD/MM/YYYY")
dataInicio = st.date_input("Data de Inicio", datetime(2024, 1, 1).date())
dataFim = st.date_input("Data Final ", datetime(2024, 12, 31).date())

entrada = st.session_state.dicionario_receita.values()

filtro = lambda x: dataInicio <= x["data"] <= dataFim
filtrados = list(filter(filtro, entrada))
st.table(filtrados)

