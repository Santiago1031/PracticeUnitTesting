import unittest

import credit_card_payment as ccp


class CreditCard(unittest.TestCase):

    def test_normal_case(self):
        amount = 200000
        interest_rate = 0.031
        payments = 36
        monthly_fee = (amount * interest_rate)/(1-((1+interest_rate)**(-payments)))
        total_interest_test = 134726.53

        total_interest = round(ccp.calculate_interest(monthly_fee, payments, amount, interest_rate), 2)

        self.assertEqual(total_interest_test, total_interest)

    def test_normal_case2(self):
        amount = 850000
        interest_rate = 0.034
        payments = 24
        monthly_fee = (amount * interest_rate)/(1-((1+interest_rate)**(-payments)))
        total_interest_test = 407059.97

        total_interest = round(ccp.calculate_interest(monthly_fee, payments, amount, interest_rate), 2)

        self.assertEqual(total_interest_test, total_interest)

    def test_zero_rate(self):
        amount = 480000
        interest_rate = 0.0
        payments = 48
        monthly_fee = amount / payments
        total_interest_test = 0

        total_interest = round(ccp.calculate_interest(monthly_fee, payments, amount, interest_rate), 2)

        self.assertEqual(total_interest_test, total_interest)

    def test_usura(self):
        amount = 50000
        interest_rate = 0.124
        payments = 60
        monthly_fee = (amount * interest_rate) / (1 - ((1 + interest_rate) ** (-payments)))

        try:
            total_interest = ccp.calculate_interest(monthly_fee, payments, amount, interest_rate)

            self.assertEqual(total_interest, 0)
        except ccp.ExcessiveRate:
            pass

    def test_single_fee(self):
        amount = 90000
        interest_rate = 0.024
        payments = 1
        monthly_fee = 90000
        total_interest_test = 0

        total_interest = round(ccp.calculate_interest(monthly_fee, payments, amount, interest_rate), 2)

        self.assertEqual(total_interest_test, total_interest)

    def test_purchase_error(self):
        amount = 0
        interest_rate = 0.024
        payments = 60
        monthly_fee = (amount * interest_rate)/(1-((1+interest_rate)**(-payments)))

        try:
            ccp.calculate_interest(monthly_fee, payments, amount, interest_rate)

            self.assertEqual(amount, 1)

        except ccp.NoAmount:
            pass

    def test_negative_error(self):
        amount = 50000
        interest_rate = 0.01
        payments = -10
        monthly_fee = (amount * interest_rate)/(1-((1+interest_rate)**(-payments)))

        try:
            ccp.calculate_interest(monthly_fee, payments, amount, interest_rate)

            self.assertEqual(payments, -1)

        except ccp.PaymentNegative:
            pass


if __name__ == '__main__':
    unittest.main()
