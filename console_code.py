"""
import pago_con_intereses as pg

La interfaz de usuario del programa debe separarse del modulo 
que contiene la lógica.

En este caso, la interfaz de usuario queda en CreditCardConsole.py
y la lógica queda en Payment.py


print("Este programa le permite calcular la cuota a pagar por una compra con tarjeta de credito")
monto = float(input("Monto de la compra:"))
tasa_intereses = float(input("Tasa de interés de la tarjeta:"))
cuotas = float(input("Numero de cuotas en que va a diferir la compra:"))

print(pg.calcular_intereses(monto, tasa_intereses, cuotas))
"""