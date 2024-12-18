import streamlit as st
from datetime import datetime


st.header("DESPESAS")

def cadastrar_despesa(dicionario):
    cont=0
    for i in enumerate(dicionario):
      cont+=1
    codigo= cont+1
    
   
    categoria=['fixa','variavel']
    tipo = st.selectbox(
      "Tipo da despesa?",
      ("Fixa", "Variavel"),  
    )
    categoria = st.selectbox(
      "Categoria?",
      ("Moradia", "Lazer", "Saude", "Transporte"),  
    )
    descricao = st.text_input(f'Descrição da despesa - ID {codigo}')
    valor = str(st.number_input('Valor da Despesa'))
    data = st.date_input("Data da despesa", format="DD/MM/YYYY")
   
    
    
    col1, col2  = st.columns(2)
    processa=col1.button('SALVAR',use_container_width=True)
    apagar=col2.button('APAGAR',use_container_width=True)
    
    if processa:
      despesa = {}
      despesa['descricao']=descricao
      despesa['tipo']=tipo
      despesa['categoria']=categoria
      despesa['valor']=valor
      despesa['data']=data
      dicionario[codigo]=despesa
      
    if apagar:
      dicionario.clear()
    
    

      

if "dicionario_despesa" not in st.session_state:
        st.session_state.dicionario_despesa= {}
           
cont=0
for i in enumerate(st.session_state.dicionario_despesa):
    cont+=1

cadastrar_despesa(st.session_state.dicionario_despesa)

st.write(f'## GASTOS POR CATEGORIA')
st.write(f'### POR PERÍODO')

entrada = st.session_state.dicionario_despesa.values()
    
dataInicio = st.date_input("Data de Inicio", datetime(2024, 1, 1).date())
dataFim = st.date_input("Data Final ", datetime(2024, 12, 31).date())

filtro = lambda x: dataInicio <= x["data"] <= dataFim
filtrados = list(filter(filtro, entrada))
st.table(filtrados)



  