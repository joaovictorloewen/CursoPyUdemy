numero = 1

while numero < 5:
    
    print(numero)
    numero += 1


print()

numero2 = 10

while numero2 >= 1:
    
    print(numero2)
    numero2 -= 1

print()

contador = 10

while contador >= 0:
    
    print(contador)
    contador -= 2

print()

contador2 = 0

while contador2 < 10:
    
    contador2 += 1
    print("Número:", contador2)

else:
    print("Contador chegou a 10")

print()

numero3 = 1

while numero3 < 100:
    
    print(numero3)
    
    if numero3 == 5:

        break
    numero3 += 1
    
print()

linha = 0

while linha < 3:

    coluna = 0

    while coluna < 3:
        print("Linha:", linha, "Coluna:", coluna)
        coluna += 1
    linha += 1


print()

numeroInicial = 1

numeroFinal = int(input("Digite um número maior que 1: "))

while numeroInicial <= numeroFinal:

    print(numeroInicial)

    numeroInicial += 1

print()

numero4 = 1

max = int(input("Digite um inteiro maior que 1: "))

print("Números pares entre 1 e", max, ":")

while numero4 <= max:

    if numero4 %2 == 0:

        print(numero4, end=" ")

    numero4 += 1

print()

while True:

    usuario  = input("Digite 'sair' encerrar: ")

    if usuario == 'sair':

        break

print()


