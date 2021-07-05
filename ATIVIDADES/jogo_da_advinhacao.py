#!/usr/bin/env python3

import random

nome = input("Ola! Qual o seu nome?")
print("Ok, " + nome + "Tente adivinhar um numero entre 1 e 20.")
numeroSecreto = random.randint(1, 20)

for tentativas in range(1, 7):  # 6 tentativas
    guess = int(input("Tente adivinhar o número: "))

    if guess < numeroSecreto:
        print("Numero muito baixo")
    elif guess > numeroSecreto:
        print("Numero muito alto.")
    else: break # caso tenha acertado

if guess == numeroSecreto:
    print("Parabéns! " + nome + " Voce acertou o numero secreto "
                              "em {}".format(tentativas), " tentativas")
else:
    print("Nao, nao. O numero sercreto é: {}".format(numeroSecreto))
    #print("Nao, nao. O numero sercreto é: " + str(numeroSecreto))
