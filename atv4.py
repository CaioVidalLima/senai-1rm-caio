nu1 = int(input('seu numero: '))
nu2 = int(input('seu numero: '))
nu3 = int(input('seu numero: '))

def verificar_par(num):
    if num % 2 == 0:
        return True
    else:
        return False
numero1 = nu1
resultado1 = verificar_par(numero1)
print(f"O número {numero1} é par? {resultado1}")

numero2 = nu2
resultado2 = verificar_par(numero2)
print(f"O número {numero2} é par? {resultado2}")

numero3 = nu3
resultado3 = verificar_par(numero3)
print(f"O número {numero3} é par? {resultado3}")