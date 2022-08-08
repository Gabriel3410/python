import random
def jogar():
    print("***********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("***********************************")

    numero_secreto=random.randrange(1, 101)
    total_de_tentativas=0
    pontos=1000

    print("Qual nível de dificuladade", numero_secreto)
    print("(1) Fácil (2) Médio (3)Difícil ")

    nivel=int(input("Defina o nível: "))

    if (nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas= 5

    for rodadas in range(1, total_de_tentativas + 1):
        print("Tentativas {} de {}". format(rodadas, total_de_tentativas) )

        chute_str=input("Digite o seu número entre 1 e 100: ")
        print("Você digitou", chute_str)
        chute= int(chute_str)

        if(chute < 1 or chute >100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        chute_maior = chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print ("Você acertou! e fez {} pontos".format(pontos))
            break
        else:
            if(chute_maior):
                print("Você errou! o seu chute foi maior do que o número secreto ")
            elif(chute_menor):
                print("Você errou! o seu chute foi menor do que o número secreto")
            pontos_perdidos= abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    print("fim do jogo")

