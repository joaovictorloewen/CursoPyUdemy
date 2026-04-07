#Posição da letra
posicaoLetra = "Python"
print(posicaoLetra[0])
print(posicaoLetra[1])
print(posicaoLetra[2])
print(posicaoLetra[3])
print(posicaoLetra[4])

print("")

frase1 = "Olá, Mundo!"

parte = frase1[4:8]
print(parte)#saida mun

primeiros = frase1[:5]
print(primeiros)#saida Olá,

ultimos = frase1[-6:]
print(ultimos)#saida Mundo!

print("")

frase2 = "O módulo de python é muito legal!"
#verifica a palavra na frase
print("python" in frase2)

print("")

frase3 = "O módulo de python é muito legal!"
#verifica a palavra na frase
if "python" in frase3:
    print("Sim, está na frase")

print("")

frase4 = "       O módulo de python é muito legal!       "
#Remove espaços em branco no inicio e no final
print(frase4.strip())

print("")

frase5 = "Olá, como vai você?"
#Divide a frase em espaços.
palavras = frase5.split()

print(palavras)

print("")

palavras = ['Olá,', 'como', 'vai', 'você?']
#Divide a frase em espaços.
frase6 = ' '.join(palavras)

print(frase6)

print("")

texto = "       Olá!        "
texto_strip = texto.strip()
print(texto_strip)

print("")

texto = "*******Olá!*******"
texto_strip = texto.strip('*')
print(texto_strip)




