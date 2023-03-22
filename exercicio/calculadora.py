
print("Calculadora simples ")
print("Digite dois números nas sequências e depois coloque a opeção que desejar ")

primeiro_numero = int(input("primeiro número:"))
operacao = input("escolha as operações simples como /, *,  -,  +: ")
segundo_numero = int(input("segundo número:"))

if(operacao == "+"):
    soma= primeiro_numero + segundo_numero
    print("{} + {} = {}".format(primeiro_numero, segundo_numero, soma))

elif(operacao == "-"):
    subtracao= primeiro_numero - segundo_numero
    print("{} - {} = {}".format(primeiro_numero, segundo_numero, subtracao))
elif(operacao == "*" ):
    multiplicacao=primeiro_numero * segundo_numero
    print("{} * {} = {}".format(primeiro_numero, segundo_numero, multiplicacao))
elif(operacao == "/"):
    divisao= primeiro_numero / segundo_numero
    print("{} / {} = {}".format(primeiro_numero, segundo_numero, divisao))
else:
    print("Somente operações simples")
