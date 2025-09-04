def autenticar():
    usuario_autenticado = input("True or False 1: ")
    if usuario_autenticado == "False":
        return("Acesso negado")
        breakpoint
    token_valido = input("True or False 2: ")
    if usuario_autenticado and token_valido == "True":
        return("Acesso permitido.")
    if usuario_autenticado == "True" and token_valido == "False":
        return("Token invalido")
print(autenticar())