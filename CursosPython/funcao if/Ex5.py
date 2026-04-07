pergunta1 = input("Você tem um convite vip? (sim/não): ")
pergunta2 = input("Você está na lista de convidados? (sim/não): ")
pergunta3 = input("Você é um membro do clube? (sim/não): ")

if pergunta1 == "sim" or pergunta2 == "sim" or pergunta3 == "sim":
    print("Bem-vindo(a) ao evento!")
else:
    print("Desculpe, você não pode entrar no evento.")