idade = 25  # Altere esse valor para testar diferentes faixas etárias


# Escreva sua estrutura condicional abaixo

if idade >= 60:
    print("Idoso.")
elif idade >= 18 and idade < 60:
    print("Adulto.")
elif idade >= 13 and idade < 18:
    print("Adolescente.")
elif idade >= 0 and idade < 13:
    print("Infantil.")
else:
    print("Não pode ter alguém menor que 0 anos.")