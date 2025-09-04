n1 = int(input('Quantos KMs foram percorridos pelo carro?: '))
n2 = int(input('Por quantos dias ele foi alugado?: '))
km = n1 * 0.15
days = n2 * 60
total = km + days
print(f'Valor a pagar por KM: {km} Valor a pagar por dias: {days} Total: {total}')