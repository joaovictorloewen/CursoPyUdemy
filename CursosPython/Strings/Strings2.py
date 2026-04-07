nome = "Alice"
idade = "25"
altura = 1.65

mensagem = f"Olá, meu nome é {nome}. Tenho {idade} anos e minha altura é {altura:.2f} metros"
print(mensagem)

print("")

texto = "OLá mundo!"

texto_upper = texto.upper()
print(texto_upper)

texto_lower = texto.lower()
print(texto_lower)

texto_capitalize = texto.capitalize() #apenas a 1° fica maiuscula
print(texto_capitalize)

ocorrencias = texto.count("o")
print(ocorrencias)

texto_substituido = texto.replace("mundo", "amigo")
print(texto_substituido)

print("")

#Exercicio1:

nome = "Maria"
sobrenome = "Silva"
idade = "30"

nome_completo = f"{nome} {sobrenome}"
print(nome_completo)

mensagem = f"Olá, me chamo {nome_completo} e tenho {idade} anos"
#mensagem = "Olá, me chamo {nome_completo} e tenho {idade} anos".format(nome_completo, idade)
print(mensagem)

print("")

#Exercicio2:

frase = "Python é uma Linguagem de programação poderosa e versátil."

tamanho_frase = len(frase)
print("Tamanho da frase: ", tamanho_frase)

palavra = frase.split()[0]
print("Primeira palavra: ", palavra)

frase_maiuscula = palavra.upper()
print(frase_maiuscula)

frase_subistituida = frase.replace("poderosa", "incrivel")
print(frase_subistituida)

print("")

#Exercicio3:
nome_completo = "Maria de Freitas Cardoso"
# 1. Exiba o nome do usuário em letras maiúsculas
nome_maiusculo = nome_completo.upper()
print(nome_maiusculo)

# 2. Exiba o nome do usuário em letras minúsculas
nome_minusculo = nome_completo.lower()
print(nome_minusculo)

# 3. Conte e exiba quantas letras (sem considerar espaços) o nome do usuário tem
quantidade_letras = len(nome_completo.replace(" ", ""))
print("Quantidade de letras:", quantidade_letras)

# 4. Exiba o primeiro nome do usuário
nome = nome_completo.split()[0]
print("Primeiro nome: ", nome)


# 5. Exiba o último nome do usuário
nome2 = nome_completo.split()[-1]
print("Ultimo nome: ", nome2)