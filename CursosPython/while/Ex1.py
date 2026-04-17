senhaSistema = "123"

senhaPessoa = int(input("Digite a senha para sair do exercicio: "))


while senhaSistema != senhaPessoa:
    
    print("Tente novamente!")

    senhaPessoa = int(input("Digite novamente: "))

print("Muito bem!!!")