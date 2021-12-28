import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101) # 0.0 1.0
    total_de_tentativas = 3
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível:"))

    if  (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas) )
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if(chute > 1 or chute < 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou     = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontosx))
            break
        else:
            if(chute_maior):
                print("Você errou! Seu chute foi maior que o número secreto")
            elif(chute_menor):
                print("Você errou! Seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

        rodada = rodada + 1


    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()