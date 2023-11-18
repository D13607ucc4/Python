
#Calculador de propina

import math

cost = float(input("¿Cual es la factura total de hoy, por favor? "))

percent = int(input("¿Cuanto porcentaje desea dejar? (18%, 20% o 25%) "))

if percent != 18 and percent != 20 and percent != 25:
    percent = int(input("¿Cuanto porcentaje desea dejar? (18%, 20% o 25%) "))


if percent == 18:
    tax_rate = round(cost * 0.18, 2)
    totalCost = round(tax_rate + cost, 2)
    print("La propina es de: $", tax_rate)
elif percent == 20:
    tax_rate = round(cost * 0.20, 2)
    totalCost = round(tax_rate + cost, 2)
    print("La propina es de: $", tax_rate)
else:
    tax_rate = round(cost * 0.25)
    totalCost = round(tax_rate + cost, 2)
    print("La propina es de: $", tax_rate)

print(f"La propina aplicando el {percent}% es {tax_rate}, que contabiliza un tatal de ${totalCost}")




