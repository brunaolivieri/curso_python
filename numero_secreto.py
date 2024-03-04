# Desenvolvido por Bruna Olivieri

numero_secreto = 19
tentativas = 3
voltas = 0

print("Você tem 3 tentativas para acertar o número secreto.")

while voltas < tentativas:
    numero_usuario = int(input("Insira um número entre 1 e 100: "))
    
    if numero_secreto == numero_usuario:
        print("Parabéns! Você acertou.")
        print("Fim.")
        break
          
    else:
        print("Você errou!")
        voltas = voltas + 1
        print(f"Tentativa {voltas}.")

    if voltas == tentativas:
        print("Fim das tentativas.")




