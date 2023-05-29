nota1 = float(input('Informe minha nota 1: '))
nota2 = float(input('Informe minha nota 2: '))
nota3 = float(input('Informe minha nota 3: '))

nota = ((nota1 + nota2 + nota3)/3)

if nota >= 6:
    print("Sua media foi {:.1f}, voce foi aprovado".format(nota))
elif nota >= 5:
    print("Passou pelo conselho porque tirou {:.1f}".format(nota))
else:
    print("Sua media foi {:.1f}, voce foi reprovado seu trouxa".format(nota))