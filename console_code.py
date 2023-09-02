
import credit_card_payment as ccp

def main():
    print("This program allows you to calculate the installment to pay for a credit card purchase")
    amount = float(input("Purchase amount: "))
    interest_rate = float(input("Credit card interest rate: "))
    payments = int(input("Number of installments to defer the purchase: "))

    try:
        # Calculate interest according to R1
        # Calcular el interés según R1

        total_interest = ccp.calculate_interest(amount, payments, amount, interest_rate)
        print(f"Total interest to be paid: {total_interest:.2f}")

        # Calculate amortization plan according to R2
        # Calcular plan de amortización según R2

        amortization_plan = ccp.calculate_amortization_plan(amount, payments, interest_rate)
        print("\nAmortization Plan:")
        print("Month | Monthly Payment | Principal | Interest")
        for month, monthly_payment, monthly_principal, monthly_interest in amortization_plan:
            print(f"{month}\t{monthly_payment:.2f}\t{monthly_principal:.2f}\t{monthly_interest:.2f}")

        # Extra payment according to R3
        # Pago extra según R3

        extra_payment = float(input("\nExtra Payment (optional): "))
        extra_payment_month = int(input("Month in which the extra payment will be applied (optional): "))
        if extra_payment > 0 and 1 <= extra_payment_month <= payments:

            # Calculate the new amortization plan with the extra payment
            # Calcula el nuevo plan de amortización con el pago extra

            amortization_plan = ccp.calculate_amortization_plan(amount, payments, interest_rate, extra_payment, extra_payment_month)
            print("\nNew Amortization Plan with Extra Payment:")
            print("Month | Monthly Payment | Principal | Interest")
            for month, monthly_payment, monthly_principal, monthly_interest in amortization_plan:
                print(f"{month}\t{monthly_payment:.2f}\t{monthly_principal:.2f}\t{monthly_interest:.2f}")
    except (ccp.ExcessiveRate, ccp.NoAmount, ccp.PaymentNegative) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
