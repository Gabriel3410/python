import forca
import adivicao

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
    adivicao.jogar()
else:
    print("Escolha somente os números 1 ou 2")
