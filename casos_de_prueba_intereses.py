import unittest

import pago_tarjeta_credito as ptc


class TarjetaCredito(unittest.TestCase):

    def test_caso_normal(self):
        monto = 200000
        tasa_intereses = 0.031
        cuotas = 36
        cuota_mensual = (monto * tasa_intereses)/(1-((1+tasa_intereses)**(-cuotas)))
        prueba_total_intereses = 134726.53

        total_intereses = round(ptc.calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses), 2)

        self.assertEqual(prueba_total_intereses, total_intereses)

    def test_caso_normal2(self):
        monto = 850000
        tasa_intereses = 0.034
        cuotas = 24
        cuota_mensual = (monto * tasa_intereses)/(1-((1+tasa_intereses)**(-cuotas)))
        prueba_total_intereses = 407059.97

        total_intereses = round(ptc.calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses), 2)

        self.assertEqual(prueba_total_intereses, total_intereses)

    def test_tasa_cero(self):
        monto = 480000
        tasa_intereses = 0.0
        cuotas = 48
        cuota_mensual = monto / cuotas
        prueba_total_intereses = 0

        total_intereses = round(ptc.calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses), 2)

        self.assertEqual(prueba_total_intereses, total_intereses)

    def test_usura(self):
        monto = 50000
        tasa_intereses = 0.124
        cuotas = 60
        cuota_mensual = (monto * tasa_intereses) / (1 - ((1 + tasa_intereses) ** (-cuotas)))

        try:
            total_intereses = ptc.calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses)

            self.assertEqual(total_intereses, 0)
        except ptc.TasaExcesiva:
            pass

    def test_cuota_unica(self):
        monto = 90000
        tasa_intereses = 0.024
        cuotas = 1
        cuota_mensual = 90000
        prueba_total_intereses = 0

        total_intereses = round(ptc.calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses), 2)

        self.assertEqual(prueba_total_intereses, total_intereses)

    def test_error_compra(self):
        monto = 0
        tasa_intereses = 0.024
        cuotas = 60
        cuota_mensual = (monto * tasa_intereses)/(1-((1+tasa_intereses)**(-cuotas)))

        try:
            ptc.calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses)

            self.assertEqual(monto, 1)

        except ptc.NoTieneMonto:
            pass

    def test_error_negativo(self):
        monto = 50000
        tasa_intereses = 0.01
        cuotas = -10
        cuota_mensual = (monto * tasa_intereses)/(1-((1+tasa_intereses)**(-cuotas)))

        try:
            ptc.calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses)

            self.assertEqual(cuotas, -1)

        except ptc.CuotasNegativas:
            pass


if __name__ == '__main__':
    unittest.main()
