import streamlit as st 

st.write('# Calculador da IMC') 

peso=st.number_input('Peso: ')

altura=st.number_input('Altura: ')
 

if altura > 0:
    imc = peso / altura ** 2
    st.write(f'## Seu IMC = {round(imc,2)}')
 