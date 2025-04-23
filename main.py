from random import randint
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
                    print("Empate!")
                if computador == 2 and pedra == 1:
                    print("Computador vence!")
                if computador == 3 and pedra == 1:
                    print("Jogador vence!")
            if choose == 2:
                if computador == 1 and papel == 2:
                    print("Jogador vence!")
                if computador == 2 and papel == 2:
                    print("Empate!")
                if computador == 3 and papel == 2:
                    print("Computador vence!")
            if choose == 3:
                if computador == 1 and tesoura == 3:
                    print("Computador vence!")
                if computador == 2 and tesoura == 3:
                    print("Jogador vence!")
                if computador == 3 and tesoura == 3:
                    print("Empate!")
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


    
