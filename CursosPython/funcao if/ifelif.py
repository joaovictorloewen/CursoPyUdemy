numero1 = 90
numero2 = 12

if numero1 > numero2:
    print("O número 1 é maior que o número 2")

print("")

numero3 = 6
numero4 = 6

if numero3 > numero4:
    print("O número 3 é maior que o número 4 ")
elif numero3 == numero4:
    print("O numero 3 é igual ao número 4")

print("")

numero5 = 2
numero6 = 6

if numero5 > numero6:
    print(f"O {numero5} é maior que o {numero6}")
elif numero5 == numero6:
    print(f"O {numero5} é igual ao {numero6}")
else:
    print(f"O {numero5} é menor que o {numero6}")

print("")

#and - E

numero7 = 50
numero8 = 21
numero9 = 200

if numero7 > numero8 and numero9 > numero1:
    print("As duas condições são verdadeiras.")

print("")

#if... or
numero10 = 19
numero11 = 150
numero12 = 18

if numero10 > numero11 or numero10 > numero12:
    print(f"O {numero10} é maior que {numero11} ou o {numero10} é maior que {numero12}")

print("")