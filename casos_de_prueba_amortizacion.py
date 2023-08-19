import unittest

import pago_tarjeta_credito as ptc


class TarjetaCredito1(unittest.TestCase):

    def test_cuota_unica(self):
        monto = 90000
        cuotas = 1
        tasa_intereses = 0.024

        amortizacion = round(ptc.calcular_plan_amortizacion(monto, cuotas, tasa_intereses), 2)

        self.assertEqual(prueba_amortizacion, amortizacion)

    def test_caso_normal(self):
        monto = 200000
        tasa_intereses = 0.031
        cuotas = 36
        cuota_mensual = (monto * tasa_intereses)/(1-((1+tasa_intereses)**(-cuotas)))
        prueba_amortizacion = 134726.53

        amortizacion = round(ptc.calcular_plan_amortizacion(cuota_mensual, cuotas, monto, tasa_intereses), 2)

        self.assertEqual(prueba_amortizacion, amortizacion)

    def test_caso_normal2(self):
        monto = 850000
        tasa_intereses = 0.034
        cuotas = 24
        cuota_mensual = (monto * tasa_intereses)/(1-((1+tasa_intereses)**(-cuotas)))
        prueba_amortizacion = 407059.97

        amortizacion = round(ptc.calcular_plan_amortizacion(cuota_mensual, cuotas, monto, tasa_intereses), 2)

        self.assertEqual(prueba_amortizacion, amortizacion)

    def test_tasa_cero(self):
        monto = 480000
        tasa_intereses = 0.0
        cuotas = 48
        cuota_mensual = monto / cuotas
        prueba_amortizacion = 0

        amortizacion = round(ptc.calcular_plan_amortizacion(cuota_mensual, cuotas, monto, tasa_intereses), 2)

        self.assertEqual(prueba_amortizacion, amortizacion)

    def test_usura(self):
        monto = 50000
        tasa_intereses = 0.124
        cuotas = 60
        cuota_mensual = (monto * tasa_intereses) / (1 - ((1 + tasa_intereses) ** (-cuotas)))

        try:
            amortizacion = ptc.calcular_plan_amortizacion(cuota_mensual, cuotas, monto, tasa_intereses)

            self.assertEqual(amortizacion, 0)
        except ptc.TasaExcesiva:
            pass
