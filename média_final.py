# Programa para calcular Média
# Desenvolvido por Bruna Olivieri

print("*****************************************************")
print("                        MÉDIA                        ")
print("*****************************************************")
print()

# CRIAÇÃO DAS VARIÁVEIS
nome_aluno = ""
nota_bim_1 = 0.0
nota_bim_2 = 0.0
nota_bim_3 = 0.0
nota_bim_4 = 0.0
media_final = 0.0

# ENTRADA DOS DADOS
nome_aluno = input("Nome do aluno: ")
nota_bim_1 = float(input("Nota do bimestre 1: "))
nota_bim_2 = float(input("Nota do bimestre 2: "))
nota_bim_3 = float(input("Nota do bimestre 3: "))
nota_bim_4 = float(input("Nota do bimestre 4: "))

# PROCESSAR OS VALORES PARA OBTER A MÉDIA
media_final = (nota_bim_1 + nota_bim_2 + nota_bim_3 + nota_bim_4) / 4

#SAÍDA DO PROCESSAMENTO
print()
print("------------------------------------------------------")
print()
print(nome_aluno + ", a sua nota final é " + str(media_final))
print()
print("------------------------------------------------------")
