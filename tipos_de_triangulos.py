#Programa para classificar triângulos
#Desenvolvido por Bruna Olivieri

#CRIAÇÃO DAS VARIÁVEIS

lado_a_triangulo = 0.0
lado_b_triangulo = 0.0
lado_c_triangulo = 0.0

#ENTRADA DOS DADOS
lado_a_triangulo = float(input("Digite o valor do lado A do triângulo: "))
lado_b_triangulo = float(input("Digite o valor do lado B do triângulo: "))
lado_c_triangulo = float(input("Digite o valor do lado C do triângulo: "))

#VERIFICAÇÃO SE A FORMA GEOMÉTRICA É UM TRIÂNGULO
if (lado_a_triangulo < lado_b_triangulo + lado_c_triangulo) and (lado_b_triangulo < lado_a_triangulo + lado_c_triangulo) and (lado_c_triangulo < lado_a_triangulo + lado_a_triangulo):
    print("É um triângulo!")
    if (lado_a_triangulo == lado_b_triangulo) and (lado_b_triangulo == lado_c_triangulo):
        print("Triângulo Equilátero.")
    elif (lado_a_triangulo == lado_b_triangulo) or (lado_a_triangulo == lado_c_triangulo) or (lado_b_triangulo == lado_c_triangulo):
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Não é um triângulo!")




  
