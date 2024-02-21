# Programa para calcular IMC
# Desenvolvido por Bruna Olivieri

print("*****************************************")
print("*          CALCULADORA DE IMC           *")
print("*****************************************")
print() # imprime uma linha em branco


# CRIAÇÃO DAS VARIÁVEIS
nome = ""
peso = 0
altura = 0.0
imc = 0.0

# ENTRADA DOS DADOS
nome = input("Digite o seu nome: ")
peso = int(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

# PROCESSAR OS VALORES PARA OBTER O IMC
imc = peso / altura ** 2

#SITUAÇÃO DO IMC
situacao_imc = ""

if (imc < 18.5):
    situacao_imc = "Abaixo do Peso"
if (imc >= 18.5) and (imc < 25):
    situacao_imc = "Peso Normal"
elif (imc >= 25) and (imc < 30):
    situacao_imc = "Sobrepeso"
elif (imc >= 30) and (imc < 35):
    situacao_imc = "Obesidade Grau I"
elif (imc >= 35) and (imc < 40):
    situacao_imc = "Obesidade Grau II"
else:
    situacao_imc = "Obesidade Grau III ou Mórbida"

# SAÍDA DO PROCESSAMENTO
print()
print("*****************************************")
print("*              RESULTADO                 ")
print("*****************************************")
print("*                                       *")
print(f"NOME: {nome}")
print(f"PESO: {peso}Kg")
print(f"ALTURA: {altura}m")
print(f"IMC: {imc:.2f}")
print(f"SITUAÇÃO: {situacao_imc}")      

