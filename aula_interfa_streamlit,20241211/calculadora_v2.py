import streamlit as st 

st.write('# Calculador') 

numa=st.number_input('Operador A')
numb=st.number_input('Operador B')
 
col1, col2, col3, col4 = st.columns(4)
somar=col1.button('➕',use_container_width=True)
div=col2.button('➗',use_container_width=True)
sub=col3.button('➖',use_container_width=True)
mult=col4.button('✖️',use_container_width=True)

resultado=0
if somar:
    resultado = numa + numb
if mult:
    resultado = numa * numb
if sub:
    resultado = numa - numb
if div:
    if numb != 0:
     resultado = numa / numb
    else:
     resultado = numa
     st.write("## Não é possível realizar divisão por zero")

st.write(f"## Resultado", resultado)