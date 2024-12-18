
import streamlit as st
# Documentação https://docs.streamlit.io/
# Montei lendo a documentaçãoe em 
# https://docs.streamlit.io/develop/tutorials/multipage/dynamic-navigation
# Realizei as adaptações para que não fosse necessários mais de um tipo de sessão de navegação
# Icones - Documentação https://docs.streamlit.io/develop/api-reference/text/st.markdown
# Busquei icones em https://gist.github.com/rxaviers/7360908
 
if "sessao" not in st.session_state:
    st.session_state.sessao = None
    # Valor para controlar o acesso ao sistema. 
    # Isso representa a função do usuário atual e autenticado.

tipos_sessao = [None, "Padrao"]
# Na documentação existe o exemplo com as seguintes sessões
# "Requester", "Responder", "Admin"
# Alterado, Uma lista de apenas dois tipos, None e Padrão

def financeiro():
      st.header(":moneybag: Sistema Financeiro")
      
      st.write("### Curso Python - Conhecendo Interfaces com Streamlit")
      container1 = st.container(border=True)
      container1.write("###### :computer: Hackaton: Desenvolver ferramentas de organização financeira")
      container2 = st.container(border=True)
 
      container2.write("#### :fast_forward: Problema que propõe a resolver")
      container2.write("Controle de entrada de receita e saída de despesas")
      container2.write("#### :fast_forward: Solução e defina")
      container2.write("Registro da despesa, e da receita dentro do período ")
      container2.write("#### :fast_forward: Entradas e Saídas")
      container2.write("Entrada de renda: Descrição, Nome da Font, Valor e Data")
      container2.write("Entrada de despesa: Descrição, Categoria, Tipo de despesa, Valor e data")
      container2.write("Saída: Gráfico de despesas, renda total, e sobras para o período informado")
      container2.write("#### :fast_forward: Inteface GUI")
      container2.write("Interface GUI, com páginas de apresentação, grafico, receita e respesa")
      container2.write("#### :fast_forward: Auxilio na Tomada de Decisão")
      container2.write("Quanto ainda tem para ser gasto no período, avaliar se é possível ter nova despesa")
      container2.write("#### :fast_forward: O projeto pode ser aprimorado")
      container2.write("Sugestões para mudança no GitHub")
      container2.write("https://github.com/attairsilva/cyberedux/tree/main/ferramenta_financeira")


      sessao = st.selectbox("Escolha a sessão Padrão para Entrar", tipos_sessao)
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

# Definir paginas de opções de serviços do sistema
principal = st.Page(
    "paginas/principal.py", title="Principal", icon=":material/star:", default=(sessao == "Padrao")
    #esta será a pagina default
)
dashboards = st.Page(
    "paginas/dashboards.py", title="Dashboards", icon=":material/star:"
)
receitas = st.Page(
    "paginas/receitas.py", title="Receitas", icon=":material/star:"
)
despesas  = st.Page(
    "paginas/despesas.py", title="Despesas", icon=":material/star:"
)
 
# agrupamento de paginas convenientes em lista
sistema_pages = [logout_page]
menu_pages = [principal, dashboards, receitas, despesas]



# adiciona a logotipo do aplicativo
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

# adicionario de lista de paginas em um dicionário
page_dict = {}

if st.session_state.sessao  in ["Padrao"]:
    page_dict["Padrao"] = menu_pages  


if len(page_dict) > 0:
    pg = st.navigation({"Sistema": sistema_pages} | page_dict)
else: # Retorne à página de login se o usuário não estiver conectado
    pg = st.navigation([st.Page(financeiro)])


pg.run() ## executa a pagina
    