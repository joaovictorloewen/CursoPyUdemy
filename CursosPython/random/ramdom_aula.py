import random

#Numeros aleatórios de 1 a 99
print(random.randrange(1,100))

#Numeros quebrados
print(random.random())

#Gera um numero aleatório de 1 a 100
print(random.randint(1,100))

#Escolhe um item da lista aleatório
frutas = ["maça", "banana", "cereja"]
print(random.choice(frutas))

#Embaralha a lista aleatóriamente
numeros = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(numeros)
print(numeros)

#Gera um numero aleatório entre o intervalo específico
print(random.uniform(5.5, 9.5))