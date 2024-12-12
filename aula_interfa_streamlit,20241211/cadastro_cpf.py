import streamlit as st

st.write('# CADASTRO DE PESSOAS')

if "dicionario_pessoas" not in st.session_state:
    st.session_state.dicionario_pessoas = {}

cpf = st.number_input('CPF')
nome = st.text_input('Nome')
processa=st.button('➕',use_container_width=True)

if processa:
    st.session_state.dicionario_pessoas[cpf] = nome
    st.table(st.session_state.dicionario_pessoas)



