Kmh = float(input('Informe sua velocidade: '))
if Kmh >= 81:
    print("Voce ficou acima de 80km/h. Voce foi multado")
elif Kmh <= 79:
    print("Voce ficou abaixo de 80km/h. Voce nao foi multado")
elif Kmh == 80:
    print("Voce esta exatamente a 80Km/h. Voce nao foi multado")