import streamlit as st
import pandas as pd
# necessario importar biblioteca panda para criar o datafram do grafico
from datetime import datetime

st.header("DASHBOARDS")


entrada = st.session_state.dicionario_despesa.values()
    
dataInicio = st.date_input("Data de Inicio", datetime(2024, 1, 1).date())
dataFim = st.date_input("Data Final ", datetime(2024, 12, 31).date())

filtro = lambda x: dataInicio <= x["data"] <= dataFim
filtrados = list(filter(filtro, entrada))

moradia=0
saude=0
lazer=0
transporte=0

for  valor in filtrados:
    if valor['categoria']=="Moradia":
        val=float(moradia) + float(valor['valor'])
        moradia=str(val)
    elif valor['categoria']=="Saude":
        val=float(saude) + float(valor['valor'])
        saude=str(val)
    elif valor['categoria']=="Lazer":
        val=float(lazer) + float(valor['valor'])
        lazer=str(val)
    elif valor['categoria']=="Transporte":
        val=float(transporte) + float(valor['valor'])
        transporte=str(val)
st.write(f'### DESPESAS POR CATEGORIA')
col1, col2, col3, col4, col5= st.columns(5)
col1.write(f'Moradia =  R$ {float(moradia):,.2f}')
col2.write(f'Saude =  R$ {float(saude):,.2f}')
col3.write(f'Lazer =  R$ {float(lazer):,.2f}')
col4.write(f'Transporte =  R$ {float(transporte):,.2f}')
totaldespesas=float(transporte)+float(lazer)+float(saude)+float(moradia)
col5.write(f'TOTAL =  R$ {totaldespesas:,.2f}')
#Grafico Despesas
top_categorias = (
    pd.DataFrame(
        {
            "name": ["Moradia", "Saude", "Lazer", "Transpote"],
            "views": [float(moradia), float(saude), float(lazer), float(transporte)],
        }
    )
    .sort_values(by="views", ascending=True)
    .reset_index(drop=True)
)
st.bar_chart(top_categorias, y="views", x="name")

st.write(f'#### TOTAL DE DESPESAS = R$ {totaldespesas:,.2f}')

entradaReceita = st.session_state.dicionario_receita.values()

filtroReceita = lambda x: dataInicio <= x["data"] <= dataFim
filtradosReceitas = list(filter(filtroReceita, entradaReceita))

moradia=0
saude=0
lazer=0
transporte=0
totaldereceitas=0
for  valor in filtradosReceitas:
        totaldereceitas+=float(valor['valor'])
        
st.write(f'#### TOTAL DE RECEITAS = R$ {totaldereceitas:,.2f}')

diferenca = totaldespesas - totaldereceitas

st.write(f'#### SOBRAS PARA O PERÍODO = R$ {diferenca:,.2f}')
#Grafico Despesas