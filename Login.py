print("Bem-vindo a tela de cadastro")
print("1 - Cadastrar usuário")
print("2 - Fazer login")
print("3 - Sair")

# Escolha do usuário
opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print("Abrindo cadastro...")
    case 2:
        print("Abrindo login...")
    case 3:
        print("Saindo do sistema...")
    case _:
        print("Opção inválida!")
        
# Dados do usuário
while True:
    nome = input("Digite seu nome: ")

    if nome != "":
        break
    else:
        print("Preencha seu nome novamente!")
        
email = input("Digite seu email: ")
senha = input("Digite seu senha: ")

while True:
    confirmeSenha = input("Digite sua senha novamente: ")

    if senha == confirmeSenha:
        print("\nCadastro realizado com sucesso!")
        break
    else:
        print("Acesso negado! Senhas diferentes.")

# Tela de login
print("Bem-vindo a tela de cadastro")


tentativas = 0

while tentativas < 3:
    emailDigitado = input("Digite seu email: ")
    senhaDigitada = input("Digite sua senha: ")

    if emailDigitado == email and senhaDigitada == senha:
        print("\nAcesso liberado!")
        print(f"Bem-vindo ao sistema, ", nome, "!")
        break
    else:
        tentativas += 1
        print("Dados incorretos!")
        print(f"Tentativas restantes: " 3 - tentativas}")

if tentativas == 3:
    print("Acesso bloqueado!")
    print("Número máximo de tentativas atingido.")


        
    
    
