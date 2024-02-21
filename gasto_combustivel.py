# COMBUSTÍVEL GASTO
# Desenvolvido por Bruna Olivieri

print("----------------------------------------")
print("          CONSUMO DE COMBUSTÍVEL        ")
print("----------------------------------------")
print()

# CRIAÇÃO DAS VARIÁVEIS
modelo_carro = ""
autonomia_carro = 0
distancia_viagem = 0
preco_combustivel = 0.0
consumo_combustivel = 0.0
total_gasto = 0.0

# ENTRADA DOS DADOS
modelo_carro = input("Modelo do veículo? ")
autonomia_carro = int(input("Autonomia do veículo? "))
distancia_viagem = int(input("Distância da viagem? "))
preco_combustivel = float(input("Preço do combustível? "))

# PROCESSAR OS VALORES PARA OBTER O CONSUMO DE COMBUSTÍVEL
consumo_combustivel = distancia_viagem / autonomia_carro
total_gasto = consumo_combustivel * preco_combustivel

# SAÍDA DO PROCESSAMENTO
print()
print("-----------------------------------------")
print("              RESULTADO                  ")
print("-----------------------------------------")
print()
print("Modelo do veículo: " + modelo_carro)
print("Autonomia do veículo: " + str(autonomia_carro) + "Km/l")
print("Distância percorrida: " + str(distancia_viagem) + "Km")
print("Valor do combustível: R$" + str(preco_combustivel))
print()
print("-----------------------------------------")
print("Quantidade de combustível utilizado: " + str(consumo_combustivel) + "l")
print("Total gasto com a viagem: R$" + str(total_gasto))
print("-----------------------------------------")


      
