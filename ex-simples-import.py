withdraw = 0
deposit = 0
totalWithdraw = 0
totalDeposit = 0

with open("transactions.txt", "r", encoding="utf-8") as file:
    transactions = file.readlines()
    for transaction in transactions:

      line = transaction.strip()
      value, type = line.split(", ")
      if type == "deposito":
          deposit += 1
          totalDeposit = totalDeposit + int(value)
      elif type == "saque":
          withdraw += 1
          totalWithdraw = totalWithdraw + int(value)

print(f"Total de depósitos: {deposit}, valor total: {totalDeposit}")
print(f"Total de saques: {withdraw}, valor total: {totalWithdraw}")