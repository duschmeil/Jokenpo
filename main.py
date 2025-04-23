from random import randint
import random
from time import sleep

print("Bem vindo ao Jokenpô!")
print("Escolha uma opção")
print("1 - Jogar contra o computador")
print("2 - Jogar contra outro jogador")
print("3 - Ver 2 computadores jogando")
print("0 - Sair")
escolha = int(input("Digite sua escolha: "))
continuar = 1

if escolha == 1:
    print("Você escolheu jogar contra o computador!")
    contadorp = 0
    contadorpc = 0
    while True:
        if continuar == 1:
            pedra = 1
            papel = 2
            tesoura = 3
            computador = randint(1, 3)
            print("1. Pedra")
            print("2. Papel")
            print("3. Tesoura")
            choose = int(input("Digite a jogada: "))
            print(f"Computador jogou {computador}")
            if choose == 1:
                if computador == 1 and pedra == 1:
                    print("Empate! Ambos jogaram pedra")
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
                if computador == 2 and pedra == 1:
                    print("Computador vence! Computador jogou papel e jogador jogou pedra ")
                    contadorpc += 1
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
                if computador == 3 and pedra == 1:
                    print("Jogador vence! Computador jogou tesoura e jogador jogou pedra")
                    contadorp += 1
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
            if choose == 2:
                if computador == 1 and papel == 2:
                    print("Jogador vence! Computador jogou pedra e jogador jogou papel")
                    contadorp += 1
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
                if computador == 2 and papel == 2:
                    print("Empate! Ambos jogaram papel ")
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
                if computador == 3 and papel == 2:
                    print("Computador vence! Computador jogou tesoura e jogador jogou papel")
                    contadorpc += 1
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
            if choose == 3:
                if computador == 1 and tesoura == 3:
                    print("Computador vence! Computador jogou pedra e jogador jogou tesoura")
                    contadorpc += 1
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
                if computador == 2 and tesoura == 3:
                    print("Jogador vence! Computador jogou papel e jogador jogou tesoura")
                    contadorp += 1
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
                if computador == 3 and tesoura == 3:
                    print("Empate! Ambos jogaram tesoura")
                    print("PLACAR GERAL: ")
                    print(f" P1 |  PC")
                    print(f"{contadorp:>3} | {contadorpc:>3}")
        else:
            break
        print("Você quer jogar novamente? ")
        print("1 - SIM \n2 - NÃO")
        continuar = int(input("Digiter sua escolha: "))
if escolha == 2:
    print("Você escolheu jogar contra outro jogador!")
    contadorp1 = 0
    contadorp2 = 0
    while True:
        if continuar == 1:
            escolha_player1 = int(input("Jogador 1 - Escolha qual você deseja: "))
            escolha_player2 = int(input("Jogador 2 - Escolha qual você deseja: "))
            
            opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

            if escolha_player1 == escolha_player2:
                print("Empate")
                print(f"Ambos escolheram {opcoes[escolha_player1]}.")
                print("PLACAR GERAL: ")
                print(f" P1 |  P2")
                print(f"{contadorp1:>3} | {contadorp2:>3}")
            if escolha_player1 == 1 and escolha_player2 == 2:
                print()
                print("Jogador 2 ganhou!")
                print("Papel vence Pedra. Jogador 2 com Papel ganhou de Jogador 1 com Pedra.")
                contadorp2 += 1
                print("PLACAR GERAL: ")
                print(f" P1 |  P2")
                print(f"{contadorp1:>3} | {contadorp2:>3}")
            if escolha_player1 == 2 and escolha_player2 == 1:
                print()
                print("Jogador 1 ganhou!")
                print("Papel vence Pedra. Jogador 1 com Papel ganhou de Jogador 2 com Pedra.")
                contadorp1 += 1
                print("PLACAR GERAL: ")
                print(f" P1 |  P2")
                print(f"{contadorp1:>3} | {contadorp2:>3}")
            if escolha_player1 == 2 and escolha_player2 == 3:
                print()
                print("Jogador 2 ganhou!")
                print("Tesoura vence Papel. Jogador 2 com Tesoura ganhou de Jogador 1 com Papel.")
                contadorp2 += 1
                print("PLACAR GERAL: ")
                print(f" P1 |  P2")
                print(f"{contadorp1:>3} | {contadorp2:>3}")
            if escolha_player1 == 3 and escolha_player2 == 2:
                print()
                print("Jogador 1 ganhou!")
                print("Tesoura vence Papel. Jogador 1 com Tesoura ganhou de Jogador 2 com Papel.")
                contadorp1 += 1
                print("PLACAR GERAL: ")
                print(f" P1 |  P2")
                print(f"{contadorp1:>3} | {contadorp2:>3}")
            if escolha_player1 == 1 and escolha_player2 == 3:
                print()
                print("Jogador 1 ganhou!")
                print("Pedra vence Tesoura. Jogador 1 com Pedra ganhou de Jogador 2 com Tesoura.")
                contadorp1 += 1
                print("PLACAR GERAL: ")
                print(f" P1 |  P2")
                print(f"{contadorp1:>3} | {contadorp2:>3}")
            if escolha_player1 == 3 and escolha_player2 == 1:
                print()
                print("Jogador 2 ganhou!")
                print("Pedra vence Tesoura. Jogador 2 com Pedra ganhou de Jogador 1 com Tesoura.")
                contadorp2 += 1
                print("PLACAR GERAL: ")
                print(f" P1 |  P2")
                print(f"{contadorp1:>3} | {contadorp2:>3}")
            
        else:
            break
        print("Você quer jogar novamente? ")
        print("1 - SIM \n2 - NÃO")
        continuar = int(input("Digiter sua escolha: "))
if escolha == 3:
    print("Você escolheu ver 2 computadores jogando!")
    contadorpc1 = 0
    contadorpc2 = 0
    while True:
        if continuar == 1:
            pc1 = random.randint(1, 3)
            pc2 = random.randint(1, 3)
            if pc1 == 1:
                print("O computador número 1 escolheu Pedra")
            if pc1 == 2:
                print("O computador número 1 escolheu Papel")
            if pc1 == 3:
                print("O computador número 1 escolheu Tesoura")
            sleep(1)
            if pc2 == 1:
                print("O computador número 2 escolheu Pedra")
            if pc2 == 2:
                print("O computador número 2 escolheu Papel")
            if pc2 == 3:
                print("O computador número 2 escolheu Tesoura")  
            sleep(1)
            if pc1 == pc2:
                print("EMPATE!!")       
            elif (pc1 == 1 and pc2 == 3) or (pc1 == 2 and pc2 == 1) or (pc1 == 3 and pc2 == 2):
                print("O computador número 1 GANHOU!!")
                sleep(1)
            else:
                print("O computador número 2 GANHOU!!")
                sleep(1) 
                contadorpc2 += 1
                print("PLACAR GERAL: ")
                print(f"PC1 | PC2")
                print(f"{contadorpc1:>3} | {contadorpc2:>3}")
        else:
            break
        print("Você quer jogar novamente? ")
        print("1 - SIM \n2 - NÃO")
        continuar = int(input("Digiter sua escolha: "))
print("Obrigado por jogar Jokenpô!")


        
