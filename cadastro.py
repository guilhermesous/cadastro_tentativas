import os
import time
os.system('cls')
print("Bem-Vindo a tela de cadastro.\n")
login = input("Crie um login para ser cadastrado: ")
senha = input("Agora uma senha: ")
acessos = {"Login": login, "Senha": senha}
os.system('cls')
print('.')
time.sleep(1)
print('.')
time.sleep(1)
print('.')
time.sleep(1)
os.system('cls')
print("\nUsuário cadastrado!\n")
time.sleep(1)
login_2 = input("Agora digite o login novamente para acessar o sistema: ")
if login_2 == login:
    senha_2 = input("Senha: ")
    if senha_2 == senha:
        os.system('cls')
        print(f"\nBem-Vindo(a) ao nosso sistema {acessos['Login']}!\n")
        exit()
    else:
        for c in range(3, 0, -1):
            os.system('cls')
            print(f"Senha Incorreta, você possui {c} tentativas")
            senha_2 = input("Senha: ")
            if senha_2 == senha:
                os.system('cls')
                print(f"\nBem-Vindo(a) ao nosso sistema {acessos['Login']}!\n")
                exit()
        print("\nPrograma encerrado.\n")
        exit()
else:
    for c in range(5, 0, -1):
            os.system('cls')
            print(f"Usuário não encontrado, você possui {c} tentativas.")
            login_2 = input("Digite o login novamente: ")
            if login_2 == login:
                os.system('cls')
                senha_2 = input("Correto\nSenha: ")
                if senha_2 == senha:
                    os.system('cls')
                    print(f"\nBem-Vindo(a) ao nosso sistema {acessos['Login']}!\n")
                    exit()
                else:
                    for c in range(3, 0, -1):
                        os.system('cls')
                        print(f"Senha Incorreta, você possui {c} tentativas")
                        senha_2 = input("Senha: ")
                        if senha_2 == senha:
                            os.system('cls')
                            print(f"\nBem-Vindo(a) ao nosso sistema {acessos['Login']}!\n")
                            exit()
                    print("\nPrograma encerrado.\n")
                    exit()
    print("\nPrograma Encerrado.\n")
    exit()
    