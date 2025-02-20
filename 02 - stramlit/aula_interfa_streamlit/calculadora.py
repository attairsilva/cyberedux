import streamlit as st 

st.write('# Calculador') 

numa=st.number_input('Operador A')
numb=st.number_input('Operador B')
 

operador = st.selectbox(
    "Operação",
    ("Somar", "Multiplicar", "Subtrair", "Dividir"),
)

if operador == "Somar":
    resultado = numa + numb
if operador == "Multiplicar":
    resultado = numa * numb
if operador == "Subtrair":
    resultado = numa - numb
if operador == "Dividir":
    if numb != 0:
     resultado = numa / numb
    else:
     resultado = numa
     st.write("## Não é possível realizar divisão por zero")

st.write(f"## Resultado", resultado)