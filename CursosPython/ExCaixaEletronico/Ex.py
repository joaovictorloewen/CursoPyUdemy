saldo = 0.0

while True:

    print("Caixa Eletrônico")
    print("1 - Verificar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Sair")

    opcao = int(input("Escolha uma opção:"))

    if opcao == 1:
        
        print("Seu saldo é: ", saldo)
    
    elif opcao == 2:

        adicao = float(input("Quanto você deseja adicionar em seu saldo? "))

        print(f"Você adicionou {adicao} reais")

        saldo = saldo + adicao

    elif opcao == 3:

        remocao = float(input("Quanto você deseja sacar de seu saldo? "))

        print(f"Você sacou {remocao} reais")

        saldo = saldo - remocao
    
    elif opcao == 4:

        break

    else:

        print("Digite um número Valido!")

print("Você saiu do sistema!")
