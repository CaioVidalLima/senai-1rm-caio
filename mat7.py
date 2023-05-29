salario = float(input('Informe o salario: '))
if salario >= 8250.00:
    superiores = salario + salario *0.10
    print ("Como superior seu salario de {}R$ foi pra {:.2f}R$".format(salario,superiores))
else:
    inferiores = salario + salario *0.15
    print ("Como um inferior seu salario de {}R$ foi pra {:.2f}R$".format(salario,inferiores))
