
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
      # Caixa de seleção para o usuário escolher uma sessao
      
      if st.button("Acessar"):
        st.session_state.sessao  = sessao 
        st.rerun()
        # salva sessao selecionada

def logout():   
    st.session_state.sessao  = None # sessao para NONE si do sistema
    # salva a sessao como None para sair
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
despesas  = st.Page(
    "paginas/despesas.py", title="Despesas", icon=":material/bug_report:"
)
 
# agrupamento de paginas convenientes em lista
sistema_pages = [logout_page]
menu_pages = [principal, receitas, despesas]



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
    