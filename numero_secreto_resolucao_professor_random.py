import random # sempre é o primeiro item do programa

numero_secreto = int(random.random() * 10)
tentativas = 3
rodada = 1
resposta = "s"

while resposta == "s":
    rodada = 1
    numero_secreto = int(random.random() * 10)
    
    while rodada <= tentativas:

        print(f"Tentativa {rodada}")

        escolha = int(input("Qual o número secreto? "))

        if escolha == numero_secreto:
            print("Parabéns, você acertou.")
            break

        rodada = rodada + 1

        if escolha < numero_secreto:
            print("O número secreto é maior.")

        else:
            print("O número secreto é menor.")

        if rodada > tentativas:
            print("Tentativas esgotadas. Você perdeu.")
            print(f"O número secreto é: {numero_secreto}.")

        continuar = input("Deseja continuar? s/n")

        if continuar == "n":
            break
        

    print("FIM.")
