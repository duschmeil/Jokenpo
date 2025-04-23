import random
from time import sleep

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
        print()
        print("Você deseja continuar ou sair?")
        print("1 - Continuar")
        print("0 - Sair")
        continuar = int(input("Digite sua escolha: "))
        if continuar == 1:
            escolha_player1 = int(input("Jogador 1 - Escolha qual você deseja: "))
            escolha_player2 = int(input("Jogador 2 - Escolha qual você deseja: "))
            
            opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

            if escolha_player1 == escolha_player2:
                print("Empate")
                print(f"Ambos escolheram {opcoes[escolha_player1]}.")
            if escolha_player1 == 1 and escolha_player2 == 2:
                print()
                print("Jogador 2 ganhou!")
                print("Papel vence Pedra. Jogador 2 com Papel ganhou de Jogador 1 com Pedra.")
            if escolha_player1 == 2 and escolha_player2 == 1:
                print()
                print("Jogador 1 ganhou!")
                print("Papel vence Pedra. Jogador 1 com Papel ganhou de Jogador 2 com Pedra.")
            if escolha_player1 == 2 and escolha_player2 == 3:
                print()
                print("Jogador 2 ganhou!")
                print("Tesoura vence Papel. Jogador 2 com Tesoura ganhou de Jogador 1 com Papel.")
            if escolha_player1 == 3 and escolha_player2 == 2:
                print()
                print("Jogador 1 ganhou!")
                print("Tesoura vence Papel. Jogador 1 com Tesoura ganhou de Jogador 2 com Papel.")
            if escolha_player1 == 1 and escolha_player2 == 3:
                print()
                print("Jogador 1 ganhou!")
                print("Pedra vence Tesoura. Jogador 1 com Pedra ganhou de Jogador 2 com Tesoura.")
            if escolha_player1 == 3 and escolha_player2 == 1:
                print()
                print("Jogador 2 ganhou!")
                print("Pedra vence Tesoura. Jogador 2 com Pedra ganhou de Jogador 1 com Tesoura.")
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


        
