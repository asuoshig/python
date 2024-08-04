import sys
import math


a = int(input())  # Salário 
b = int(input())  # quatro semanas
c = int(input())  # Outras quatro semanas


horas_dia = 6
dias_semana = 5
semana = 4
total_income = a * horas_dia * dias_semana * semana

# Cálculo das despesas totais por quatro semanas
total_expenses = b + c

# Verificação se ele pode pagar o apartamento e outras despesas
if total_income >= total_expenses:
    print("true")
else:
    print("false")
