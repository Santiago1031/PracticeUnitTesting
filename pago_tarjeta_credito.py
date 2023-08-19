# En caso de tener un problema en particular se usara la excepción.

# R1


class ErrorCase(Exception):
    pass


class TasaExcesiva(Exception):
    pass


class NoTieneMonto(Exception):
    pass


class CuotasNegativas(Exception):
    pass


def calcular_intereses(cuota_mensual, cuotas, monto, tasa_intereses):

    if tasa_intereses*12 > 1:
        raise TasaExcesiva("La tasa anual de interes supera el 100%")

    if monto == 0:
        raise NoTieneMonto("El monto debe ser superior a cero")

    if cuotas < 0:
        raise CuotasNegativas("El número de cuotas debe ser mayor a cero")

    else:
        return (cuota_mensual * cuotas) - monto

# R2


def calcular_plan_amortizacion(monto, tasa_intereses, cuotas):

    r = tasa_intereses / 100 / 12
    cuota_inicial = monto * r
    saldo_pendiente = monto

    plan_amortizacion = []

    for cuota in range(1, cuotas + 1):
        pago_intereses = saldo_pendiente * r
        abono_capital = cuota_inicial - pago_intereses
        saldo_pendiente -= abono_capital
        plan_amortizacion.append((cuota, pago_intereses, abono_capital, saldo_pendiente))

    return plan_amortizacion


def imprimir_plan_amortizacion():
    print("Cuota\tPago Interés\tAbono Capital\tSaldo")
    for cuota, pago_interes, abono_capital, saldo in plan:
        print(f"{cuota}\t{pago_interes:.2f}\t\t{abono_capital:.2f}\t\t{saldo:.2f}")

# Ejemplos de uso

monto_compra = 200000
tasa_interes = 3.10
numero_cuotas = 12

plan = calcular_plan_amortizacion(monto_compra, tasa_interes, numero_cuotas)
imprimir_plan_amortizacion()
