from dbconfig.dbconfig import conexao

if not conexao():
    print("Erro de conexão com o banco de dados.")

while True:
    print("\n PROJETO CATRINA 1.0")
    print("Login:")
    print("A - Entrar \nB - Cadastrar \nC - Sair")

    opc = input("Escolha uma opção: ").lower()

    match opc:
        case 'a':
            nome = input("Nome: ")
            sobrenome = input("Sobrenome: ")
            nome_usuario = input("Nome de usuário: ")
            senha = input("Senha: ")
            break
        case 'b':
            nome_usuario = input("Nome de usuário: ")
            senha = input("Senha: ")
        case 'c':
            print("Saindo...")
            break
        case _:
            print("Opção inválida.")
            break