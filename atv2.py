import time

def contagem_regressiva(tempo):
    for t in range(tempo, 0, -1):
        print(t)
        time.sleep(1)

t = int(input('Informe o tempo restante: '))

print ("infelismente nao deu tempo: ".format(contagem_regressiva(t)))



