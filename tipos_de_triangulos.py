#Programa para classificar triângulos
#Desenvolvido por Bruna Olivieri

print("+--------------------------------+")
print("|       TIPOS DE TRIÂNGULO       |")
print("+--------------------------------+")
print()

#CRIAÇÃO DAS VARIÁVEIS
lado_a = 0
lado_b = 0
lado_c = 0

#ENTRADA DOS DADOS
lado_a = int(input("Digite o tamanho do lado A: "))
lado_b = int(input("Digite o tamanho do lado B: "))
lado_c = int(input("Digite o tamanho do lado C: "))

#VERIFICAÇÃO SE A FORMA GEOMÉTRICA É UM TRIÂNGULO
if (lado_a < lado_b + lado_c) and (lado_b < lado_a + lado_c) and (lado_c < lado_a + lado_a):
    print("É um triângulo!")
    if (lado_a == lado_b) and (lado_b == lado_c):
        print("Equilátero.")
    elif (lado_a == lado_b) or (lado_a == lado_c) or (lado_b == lado_c):
        print("Isósceles.")
    else:
        print("Escaleno.")
else:
    print("Não é um triângulo!")

print("Fim do Programa.")




  
