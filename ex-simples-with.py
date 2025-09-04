count = 0
with open("transactions.txt", "r", encoding="utf-8") as file:
    transactions = file.readlines()
    for transaction in transactions:
            count = count + 1
print(f"Número de transações: {count}")