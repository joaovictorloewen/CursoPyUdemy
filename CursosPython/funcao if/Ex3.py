nota = int(input("Qual a sua nota (0-100): "))

if nota >= 90 and nota <= 100:
    print("Sua nota está escelente")
elif nota >= 70 and nota < 90:
    print("Sua nota está boa")
elif nota >= 50 and nota < 70:
    print("Sua nota está satisfatória")
elif nota >= 0 and nota < 50:
    print("Sua nota está insuficiente")
else:
    print("Não pode existir uma nota menor que 0 e maior que 100")

