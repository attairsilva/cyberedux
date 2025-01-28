import json  
# Importa o módulo JSON para manipular arquivos no formato JSON

def main():
    cadastros = []  
    # Lista para armazenar os cadastros realizados

    def menu():
        # Exibe o menu de opções para o usuário
        print("\nMenu de Opções:")
        print("1. Cadastrar pessoa")  # Opção para cadastrar uma nova pessoa
        print("2. Listar cadastros")  # Opção para exibir os cadastros realizados
        print("3. Salvar cadastros")  # Opção para salvar os cadastros em um arquivo JSON
        print("4. Carregar cadastros")  # Opção para carregar cadastros de um arquivo JSON
        print("5. Sair")  # Opção para sair do programa
        return input("Escolha uma opção: ")  # Retorna a escolha do usuário

    def cadastrar_pessoa():
        # Função para cadastrar uma nova pessoa
        nome = input("Digite o nome da pessoa: ")  # Solicita o nome da pessoa
        cpf = input("Digite o CPF da pessoa: ")  # Solicita o CPF da pessoa
        cadastros.append({"nome": nome, "cpf": cpf})  # Adiciona o cadastro à lista
        print("Cadastro realizado com sucesso!")  # Confirmação de cadastro

    def listar_cadastros():
        # Função para listar todos os cadastros realizados
        if not cadastros:  # Verifica se a lista de cadastros está vazia
            print("Nenhum cadastro encontrado.") 
            # Mensagem se não houver cadastros
        else:
            print("\nCadastros:")  # Título da listagem
            for idx, pessoa in enumerate(cadastros, start=1):  
                # Enumera os cadastros para exibição
                print(f"{idx}. Nome: {pessoa['nome']}, CPF: {pessoa['cpf']}")  # Exibe cada cadastro

    def salvar_cadastros():
        # Função para salvar os cadastros em um arquivo JSON
        try:
            with open("cadastros.json", "w") as arquivo:  
                # Abre o arquivo para escrita
                json.dump(cadastros, arquivo, indent=4)  
                # Salva a lista de cadastros no arquivo
            print("Cadastros salvos com sucesso!")  
            # Confirmação de salvamento
        except Exception as e:
            print(f"Erro ao salvar cadastros: {e}")  
            # Exibe mensagem de erro caso algo dê errado

    def carregar_cadastros():
        # Função para carregar cadastros de um arquivo JSON
        nonlocal cadastros  
        # Permite modificar a variável 'cadastros' definida fora da função
        try:
            with open("cadastros.json", "r") as arquivo: 
                # Abre o arquivo para leitura
                cadastros = json.load(arquivo)  
                # Carrega os dados do arquivo para a lista
            print("Cadastros carregados com sucesso!")  
            # Confirmação de carregamento
        except FileNotFoundError:
            print("Nenhum arquivo de cadastros encontrado.") 
            # Mensagem se o arquivo não existir
        except json.JSONDecodeError:
            print("Erro ao carregar cadastros: Arquivo corrompido ou vazio.")  
            # Mensagem se houver erro no arquivo

    while True:
        # Loop principal do programa
        opcao = menu()  
        # Exibe o menu e recebe a opção escolhida pelo usuário

        if opcao == "1":
            cadastrar_pessoa()  # Chama a função para cadastrar pessoa
        elif opcao == "2":
            listar_cadastros()  # Chama a função para listar os cadastros
        elif opcao == "3":
            salvar_cadastros()  # Chama a função para salvar os cadastros
        elif opcao == "4":
            carregar_cadastros()  # Chama a função para carregar os cadastros
        elif opcao == "5":
            print("Saindo do programa. Até mais!")  # Mensagem de saída
            break  # Encerra o loop e finaliza o programa
        else:
            print("Opção inválida. Tente novamente.") 
            # Mensagem para opções inválidas

if __name__ == "__main__":
    main()  # Executa a função principal ao iniciar o programa
