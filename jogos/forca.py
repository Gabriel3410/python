import random

def jogar():

    imprimir_mensagem_abertura()
    palavra_secreta= gerar_palavras_secretas()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = pedir_chute()

        if (chute in palavra_secreta):
            marcacao_de_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)


    if(acertou):
        imprimir_mensagem_vencendor()
    else:
        imprimir_mensagem_perdedor()


def imprimir_mensagem_abertura():
    print("**********************************")
    print("*** Bem vindo ao jogo da forca ***")
    print("**********************************")

def gerar_palavras_secretas():
    arquivo=open("palavras.txt", "r")
    palavras=[]

    for linha in arquivo:
        linha= linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero=random.randrange(0,len(palavras))
    palavra_secreta=palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
   return ["_" for letra in palavra]

def pedir_chute():
    chute= input("Qual é a letra:")
    chute = chute.strip().upper()
    return chute

def marcacao_de_chute_correto(chute,letras_acertadas,palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra
        index += 1

def imprimir_mensagem_vencendor():
    print("Você ganhou !!")

def imprimir_mensagem_perdedor():
    print("Você perdou!!")

if (__name__ == "__main__"):
    jogar()
