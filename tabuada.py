#Programa desenvolvido por Bruna Olivieri
#Tabuada

multiplicando = int(input("Qual é o multiplicando? "))
minimo_multiplicador = int(input("Qual é o mínimo multiplicador? "))
maximo_multiplicador = int(input("Qual é o máximo multiplicador? "))

print()
print("----------------------------")
print(f"Tabuada do {multiplicando}")
print("----------------------------")
print()

while minimo_multiplicador <= maximo_multiplicador: #ou while minimo_multiplicador < maximo_multiplicador + 1:
    tabuada = multiplicando * minimo_multiplicador
    print(f"{multiplicando} X {minimo_multiplicador} = {tabuada}")
    minimo_multiplicador = minimo_multiplicador + 1

print()   
print("FIM")
print("----------------------------")
    
