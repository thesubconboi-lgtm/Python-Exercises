def check_temperatura():
    temperatura = int(input("Insira uma temperatura:"))
    if (temperatura >= 30):
        return ("Está quente.")
    else:
        return ("Clima ameno")
print (check_temperatura())
