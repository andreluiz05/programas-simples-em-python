entrada_user = input("Digite seu nome de usuário: ")
entrada_pass = input("Digite sua senha, mas que seja diferente do nome de usuário: ")

var1 = entrada_user
var2 = entrada_pass

if var1 == var2:
    print("Usuário e senha iguais! Digite com com informações!")
   
 while var2 == var1:
        var2 = input("Digite uma senha diferente do nome usuário: ")

elif var1 != var2:
    print("Usuário e senha aceitos! Cadastro concluído!")