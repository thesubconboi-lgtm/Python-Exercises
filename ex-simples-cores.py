def color():
    cores = ['vermelho', 'verde', 'azul']
    escolha = input("Escolha uma cor: ")
    if escolha in cores:
        return("Encontrada")
    if escolha is "":
        return("Nenhuma cor selecionada.")
print(color())