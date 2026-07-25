# Scipt para calcular el Índice de Masa Corporal // Diego Alejandro Salcido Pérez...
#24/07/26

peso = float(input("Escribe tu peso en kilogramos: "))
altura = float(input("Escribe tu altura en metros: "))


imc = peso / (
    altura ** 2)

print("__Su IMC es__", 
      imc)
