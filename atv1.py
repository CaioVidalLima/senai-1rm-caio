lar = float(input("informe a largura: "))
com = float(input("informe o comprimento: "))

def area(largura, comprimento):
    total = largura * comprimento
    return total

print("a area do terreno e {}m2".format(area(lar, com)))