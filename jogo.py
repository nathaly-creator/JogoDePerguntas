# Início do jogo
pontos = 0

print("Bom diaa!")  
print("Bem-vindo(a) ao Jogo das Perguntas!")
print("Acerte o máximo de perguntas possíveis!!")

# Perguntas iniciais
nome = input("Qual é o seu nome? ")
idade = input("Quantos anos você tem? ")

print("Legal,",nome,"! Agora vamos para as perguntas!")

# Pergunta 1
capital = input("Qual é a capital do Brasil? ").strip().lower()
if capital == "brasília" or capital == "brasilia":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Pergunta 2
animal = input("Qual é o animal terrestre mais rápido do mundo? ").strip().lower()
if animal == "guepardo":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Pergunta 3
hello = input("O que a palavra 'hello' significa em português? ").strip().lower()
if hello == "oi" or hello == "olá" or hello == "ola":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Pergunta 4
cálculo = input("Quanto é 12 x 3? ").strip().lower()
if cálculo == "36" or cálculo == "trinta e seis":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Pergunta 5
trevo = input("Quantas folhas tem um trevo da sorte? ").strip().lower()
if trevo == "quatro" or trevo == "4":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Pergunta 6
língua = input("Qual a língua oficial da China? ").strip().lower()
if língua == "mandarim":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Pergunta 7
ano = input("Em que ano começou a primira guerra mundial? ")
if ano == "1914":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Pergunta 8
metal = input("Qual foi o primeiro metal usado pelo homem? ").strip().lower()
if metal == "cobre":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")
    
# Pergunta 9
regiões = input("Quantas regiões tem no Brasil? ").strip().lower()
if regiões == "5" or língua == "cinco" :
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")
    
# Pergunta 10
esporte = input("Qual é o esporte mais popular no Brasil? ").strip().lower()
if esporte == "futebol":
    print("🥳 Parabéns, você acertou!")
    pontos += 1
else:
    print("😢 Que pena, você não acertou.")

# Resultado final
print("chegamos ao final do jogo,",nome,"! Você fez",pontos," ponto(s). 🎯")
