import Aleatorio.Loginn as Loginn

login = str(input("Login: "))
senha = str(input("Senha: "))

resultado = Loginn.verificar_senha(login, senha)

if resultado:
    Loginn.logar_perfil()
else:
    Loginn.erro_perfil()
