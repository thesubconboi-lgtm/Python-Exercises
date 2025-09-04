n1 = int(input('Insira um valor: '))
n2 = int(input('Insira outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {}, a divisão é {:.3f}'.format(s, m, d), end=' >>> ')
print(f'Divisão inteira é {di} e potencia é {e}')