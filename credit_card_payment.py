
# In case of having a particular problem, the exception will be used.
# En caso de tener un problema en particular se usara la excepción.

class ErrorCase(Exception):
    pass


class ExcessiveRate(Exception):
    pass


class NoAmount(Exception):
    pass


class PaymentNegative(Exception):
    pass


def calculate_interest(monthly_fee, payments, amount, interest_rate):

    if interest_rate*12 > 1:
        raise ExcessiveRate("The annual interest rate exceeds 100%")

    if amount == 0:
        raise NoAmount("The amount must be greater than zero")

    if payments < 0:
        raise PaymentNegative("The number of installments must be greater than zero")

    else:
        return (monthly_fee * payments) - amount

def calculate_amortization_plan(amount, payments, interest_rate, extra_payment=None, extra_payment_month=None):
    if interest_rate * 12 > 1:
        raise ExcessiveRate("The annual interest rate exceeds 100%")

    if amount == 0:
        raise NoAmount("The amount must be greater than zero")

    if payments < 0:
        raise PaymentNegative("The number of installments must be greater than zero")

    amortization_plan = []

    if payments == 1:

        # Special case: a single installment
        # Caso especial: una sola cuota

        monthly_payment = amount
        monthly_interest = 0
        monthly_principal = amount
        amortization_plan.append((1, monthly_payment, monthly_principal, monthly_interest))
    else:

        # Calculate the fixed monthly fee
        # Calcular la cuota fija mensual

        monthly_interest_rate = interest_rate / 12
        monthly_payment = amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -payments))
        balance = amount

        for month in range(1, payments + 1):
            if extra_payment and extra_payment_month == month:

                # Apply extraordinary fertilizer
                # Aplicar abono extraordinario

                balance -= extra_payment

            monthly_interest = balance * monthly_interest_rate
            monthly_principal = monthly_payment - monthly_interest
            balance -= monthly_principal

            amortization_plan.append((month, monthly_payment, monthly_principal, monthly_interest))

    return amortization_plan
