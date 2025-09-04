def habilitação():
    cnh = input("Você possui CNH? ")
    idade = int(input("Qual sua idade? "))
    if cnh == "sim" and idade >= 18:
        return("Pode dirigir.")
    else:
        return("Não habilitado.")
print(habilitação())