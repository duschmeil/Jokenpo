import random

print("Bem vindo ao Jokenpô!")
print("Escolha uma opção")
print("1 - Jogar contra o computador")
print("2 - Jogar contra outro jogador")
print("3 - Ver 2 computadores jogando")
print("0 - Sair")
escolha = int(input("Digite sua escolha: "))

if escolha == 1:
    print("Você escolheu jogar contra o computador!")
    while True:
        print("Você deseja continuar ou sair?")
        print("1 - Continuar")
        print("0 - Sair")
        continuar = int(input("Digite sua escolha: "))
        if continuar == 1:
            print("Escolha")
        else:
            break
if escolha == 2:
    print("Você escolheu jogar contra outro jogador!")
    while True:
        print("Você deseja continuar ou sair?")
        print("1 - Continuar")
        print("0 - Sair")
        continuar = int(input("Digite sua escolha: "))
        if continuar == 1:
            print("Escolha")
        else:
            break
if escolha == 3:
    print("Você escolheu ver 2 computadores jogando!")
    while True:
        print("Você deseja continuar ou sair?")
        print("1 - Continuar")
        print("0 - Sair")
        continuar = int(input("Digite sua escolha: "))
        if continuar == 1:
            print("Escolha")
        else:
            break
print("Obrigado por jogar Jokenpô!")
print("boravesesalva")

    
