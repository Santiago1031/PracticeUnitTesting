
import pago_tarjeta_credito as ptc

""""
La interfaz de usuario del programa debe separarse del modulo 
que contiene la lógica.

En este caso, la interfaz de usuario queda en casos_de_prueba_intereses.py
y la lógica queda en pago_tarjeta_credito.py
"""

print("Este programa le permite calcular la cuota a pagar por una compra con tarjeta de crédito")
monto = float(input("Monto de la compra: "))
tasa_intereses = float(input("Tasa de interés de la tarjeta: "))
cuotas = float(input("Número de cuotas en que va a diferir la compra: "))

print(ptc.calcular_intereses(monto, tasa_intereses, cuotas))
