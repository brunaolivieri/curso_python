# COMBUSTÍVEL GASTO
# Desenvolvido por Bruna Olivieri

print("-------------------------------------------------------")
print("                CONSUMO DE COMBUSTÍVEL                 ")
print("-------------------------------------------------------")
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
print("-------------------------------------------------------")
print("              RESULTADO                                ")
print("-------------------------------------------------------")
print()
print(f"Modelo do veículo: {modelo_carro}")
print(f"Autonomia do veículo: {autonomia_carro} Km/l")
print(f"Distância percorrida: {distancia_viagem} Km")
print(f"Valor do combustível: R$ {preco_combustivel}")
print()
print("-------------------------------------------------------")
print(f"Quantidade de combustível utilizado: {consumo_combustivel:.2f} l")
print(f"Total gasto com a viagem: R$ {total_gasto:.2f}")
print("-------------------------------------------------------")
