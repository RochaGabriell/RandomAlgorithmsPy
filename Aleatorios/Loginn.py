def verificar_senha(login, senha):
    login_c = "123"
    senha_c = "123"

    if login == login_c and senha == senha_c:
        return True
    else:
        return False

def logar_perfil():
    print("""
    Bem Vindo!
    """)

def erro_perfil():
    print("""
    Vc errou a senha!
    """)