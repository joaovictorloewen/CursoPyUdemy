import random

numero_secreto = random.randint(1, 100)
tentativas = 0

#print(numero_secreto)

while True:

    palpite = int(input("Digite o seu palpite: "))
    tentativas += 1

    if palpite < numero_secreto:

        print("O número secreto é maior, tente novamente!")

    elif palpite > numero_secreto:

        print("O número secreto é menor, tente novamente!")

    else:

        print(f"Parabéns, você acertou o {numero_secreto} em {tentativas} tentativas!")

        break
