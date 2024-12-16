# Neste hackaton, as equipes deverão desenvolver ferramentas de organização financeira, 
# para pessoas físicas ou empresas. Essas ferramentas devem auxiliar os usuários em tarefas 
# como previsão de gastos e rendimentos, controle de gastos, investimentos, impostos, etc. 
# Pontos importantes nos quais você deve pensar:
# - Qual problema o seu projeto se propõe a resolver? Como pretende resolver? 
# R: Controle de gastos com contas a pagar e a receber de uma pessoa física, para que a pessoa
# não gasta mais do que receba
# Identifique um problema, proponha uma solução e defina um escopo de trabalho.
# R: Pessoas costumam gastar mais do que tem a receber, primeiro ele precisa inserir a sua previsão
# de receita, no mes, para que seja acompanhado percentual que esta sendo gasto e alertar sobre
# a receita comprometida
# - Quais são as entradas e saídas do seu programa?
# R: Cadastro da pessoa, da sua estimativa de renda, de suas despesas fixas e flexissiveis
# - Como é a interface do seu programa? (CLI e GUI são aceitas)
# R: Interface gráfica GUI utilizando o STREAMLIT, com um menu de cadastro de pessoa, renda e despesas
# - Em quais tomadas de decisão o usuário será ajudado pelo seu programa?
# R: Planejamento mensal financeiro, para saber o valor que ainda resta para um investimento, e
# um alerta para que sua renda nao seja comprometida com gastos além da sua fonte.
# - Como seu projeto poderá ser aprimorado após o hackaton?
# R: Novas funcionalidade envolvendo a previsão de gastos de uma pessoa física, como opções
# que garantam o alcance de objetivos e cenários financeiros pessoais. 

import streamlit as st
# Documentação https://docs.streamlit.io/
# Montei lendo a documentaçãoe em 
# https://docs.streamlit.io/develop/tutorials/multipage/dynamic-navigation
# Realizei as adaptações para que não fosse necessários mais de um tipo de sessão de navegação

 
if "sessao" not in st.session_state:
    st.session_state.sessao = None
    # Valor para controlar o acesso ao sistema. 
    # Isso representa a função do usuário atual e autenticado.

tipos_sessao = [None, "Padrao"]
# Na documentação existe o exemplo com as seguintes sessões
# "Requester", "Responder", "Admin"
# Alterado, Uma lista de apenas dois tipos, None e Padrão

def login():
      st.header("Entrar")
      sessao = st.selectbox("Escolha seu usuário", tipos_sessao)
      # Caixa de seleção para o usuário escolher uma função
      
      if st.button("Acessar"):
        st.session_state.sessao  = sessao 
        st.rerun()
        # Caixa de seleção para o usuário escolher uma função
      
def logout():   
    st.session_state.sessao  = None # sessao para NONE si do sistema
    st.rerun()

sessao = st.session_state.sessao

logout_page = st.Page(logout, title="Sair", icon=":material/logout:")
usuario_page = st.Page(logout, title="Sair", icon=":material/logout:")
# Definir as páginas do sistema


# Definir paginas de opções de serviços do sistema
principal = st.Page(
    "paginas/principal.py", title="Principal", icon=":material/bug_report:", default=(sessao == "Padrao")
    #esta será a pagina default
)
receitas = st.Page(
    "paginas/receitas.py", title="Receitas", icon=":material/bug_report:"
)
despesas_listar = st.Page(
    "paginas/despesas_listar.py", title="Listar Despesas", icon=":material/bug_report:"
)
despesas_cadastrar = st.Page(
    "paginas/despesas_cadastrar.py", title="Cadastrar Despesas", icon=":material/bug_report:"
)

# agrupamento de paginas convenientes em lista
sistema_pages = [logout_page]
menu_pages = [principal, receitas, despesas_listar, despesas_cadastrar]



# adiciona a logotipo do aplicativo
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

# adicionario de lista de paginas em um dicionário
page_dict = {}

if st.session_state.sessao  in ["Padrao"]:
    page_dict["Padrao"] = menu_pages  


if len(page_dict) > 0:
    pg = st.navigation({"Sistema": sistema_pages} | page_dict)
else: # Retorne à página de login se o usuário não estiver conectado
    pg = st.navigation([st.Page(login)])


pg.run() ## executa a pagina
    