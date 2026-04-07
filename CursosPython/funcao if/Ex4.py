valor = float(input("Digite qual o valor da sua compra: "))

if valor > 1000:
    desconto = 0.20 * valor
    valor_final = valor - desconto
    print(f"Você recebera 20% de desconto, o desconto será de {desconto:.2f} reais")
    print(f"Sua conpra ficou de {valor_final:.2f} reais")
elif valor >= 500 and valor <= 1000:
    desconto = 0.10 * valor
    valor_final = valor - desconto
    print(f"Você recebera 10% de desconto, o descontoi será de {desconto:.2f} reais")
    print(f"Sua conpra ficou de {valor_final:.2f} reais")
else:
    print("Você não está apto ao desconto")