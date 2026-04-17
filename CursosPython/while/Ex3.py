maiorNumero = -1

numeroDigitado = int(input("Digite um número inteiro e maior que zero: "))

while numeroDigitado >= 0:

    if numeroDigitado > maiorNumero:

        maiorNumero = numeroDigitado
    
    numeroDigitado = int(input("Digite um número inteiro e maior que zero: "))

    print("Maior número: ", maiorNumero)