def check():
    itens = ["espada", "escudo", "pocao", "mapa"]
    item = input("Digite um item para usar: ")
    if item in itens:
        return f"Agora usando {item}!"
    else:
        return("Item não encontrado...")
print(check())