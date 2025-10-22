entrada_user = str(input("Digite seu nome de usuário! "))
entrada_pass = str(input("Digite sua senha, mas que seja diferente do nome usuário! "))

var1 = entrada_user
var2 = entrada_pass

if var1 == var2:
    print("Usuário e senha iguais! Digite com informações!")
    
elif var1 != var2:
    print("Usuário e senha aceitos! Cadastro concluído!")