#En caso de tener un problema en particular se usara la excepción.

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





