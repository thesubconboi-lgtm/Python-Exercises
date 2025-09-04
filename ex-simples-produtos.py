count = 0
count2 = 0
with open("produtos.txt", "r", encoding="utf-8") as file:
    products = file.readlines()
    for product in products:
        linha = product.strip()
        type, value = linha.split(", ")
        if int(value) >= 1:
            count = count + 1
        elif int(value) == 0:
            count2 = count2 + 1
print(f"Total de produtos disponiveis: {count}")
print(f"Total de produtos indisponiveis: {count2}")