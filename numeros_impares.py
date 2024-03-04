#Listar números ímpares

menor_valor = int(input("Insira o menor valor: "))
maior_valor = int(input("Insira o maior valor: "))

if maior_valor < menor_valor:
    troca = maior_valor
    maior_valor = menor_valor
    menor_valor = troca
    
while menor_valor <= maior_valor:
    if menor_valor % 2 == 1:
        print(f"ÍMPAR -> {menor_valor}")

    print(f"{menor_valor}")    
    menor_valor = menor_valor + 1   


        

        
