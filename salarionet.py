# Scipt para calcular el salario neto // Diego Alejandro Salcido Pérez...
# 24/07/26

salario_bruto = float(input("Escribe el salario bruto: "))
impuestos = float(input("Escribe el porcentaje % de impuestos: "))
deducciones = float(input("Escribe  las deducciones: "))


salario_neto = salario_bruto - (salario_bruto * impuestos / 100)
- deducciones


print("__El salario neto es__", 
      salario_neto)
