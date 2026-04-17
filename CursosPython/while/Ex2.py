numeroDigitado = int(input("Digite um número: "))

somaNumerosDigitados = 0

while numeroDigitado != 0:

    print("Tente novamente!")

    somaNumerosDigitados += numeroDigitado

    numeroDigitado = int(input("Digite outro: "))

print(f"Parábens você acertou o 0, a soma de todos os números digitados foi {somaNumerosDigitados}!")
