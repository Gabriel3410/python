import jogos.forca as forca
import jogos.adivinhacao as adivinhacao

print("***********************************")
print(" ***Escolha o seu jogo!***")
print("***********************************")

print("(1) Forca (2) Adivinhação")

jogo= int(input("Qual jogo ?"))
if(jogo == 1):
    print("Jogo da forca ")
    forca.jogar()
elif(jogo == 2):
    print("Jogo da adivinhação")
    adivinhacao.jogar()
else:
    print("Escolha somente os números 1 ou 2")
