import random

def jogo_adivinhacao():
    numero_secreto = random.randint(0, 100)
    tentativas = 0
    pontuacao = 1000

    print("Bem-vindo ao jogo da adivinhação!")
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (10 tentativas)")
    print("2 - Médio (5 tentativas)")
    print("3 - Difícil (3 tentativas)")
    nivel = int(input("Digite o número do nível desejado: "))

    if nivel == 1:
        tentativas = 10
    elif nivel == 2:
        tentativas = 5
    elif nivel == 3:
        tentativas = 3
    else:
        print("Nível inválido. Reinicie o jogo.")
        return

    for jogadas in range(tentativas):
        palpite = int(input("Digite um número entre 0 e 100: "))
        
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            print("Pontuação final: ", pontuacao)
            return
        else:
            pontuacao -= abs(palpite - numero_secreto)
            if palpite < numero_secreto:
                print("Tente um número maior!")
            else:
                print("Tente um número menor!")

    print("Suas tentativas acabaram!")
    print("O número secreto era:", numero_secreto)
    print("Pontuação final: ", pontuacao)

jogo_adivinhacao()
