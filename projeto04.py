#Jogo de Adivinhação:
#Implemente um jogo onde o computador escolhe um número aleatório e o jogador deve adivinhar qual é. Use um laço de repetição for para limitar o número de tentativas.

import random

# Define o intervalo de números possíveis para o jogo
numero_minimo = 1
numero_maximo = 100

# Gera um número aleatório que o jogador deve adivinhar
numero_secreto = random.randint(numero_minimo, numero_maximo)

# Define o número máximo de tentativas
max_tentativas = 10

print("Bem-vindo ao jogo de adivinhação!")
print(f"O número secreto está entre {numero_minimo} e {numero_maximo}.")

# Laço de repetição for para limitar o número de tentativas
for tentativa in range(1, max_tentativas + 1):
    # Solicita ao jogador que faça uma tentativa
    palpite = int(input(f"Tentativa {tentativa}/{max_tentativas}. Faça seu palpite: "))
    
    # Verifica se o palpite do jogador está correto
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativa} tentativas.")
        break
    elif palpite < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")
else:
    print(f"Você excedeu o número máximo de tentativas. O número secreto era {numero_secreto}.")

#Neste código, o computador escolhe um número aleatório dentro de um intervalo definido. O jogador tem um número limitado de tentativas para adivinhar o número secreto. Após cada tentativa, o programa informa se o palpite do jogador é maior ou menor que o número secreto. Se o jogador adivinhar corretamente dentro do número máximo de tentativas, ele vence o jogo. Se exceder o número máximo de tentativas, ele perde.