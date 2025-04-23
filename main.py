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
        else:
            break
print("Obrigado por jogar Jokenpô!")


    
