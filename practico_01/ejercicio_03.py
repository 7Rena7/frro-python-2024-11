"""Único return vs múltiples return."""

from typing import Union

from helpers import check_int_or_float_parameters


def operacion_basica(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Toma dos números (a, b) y un booleano (multiplicar):
        - Si multiplicar es True: devuelve la multiplicación entre a y b.
        - Si multiplicar es False: devuelve la division entre a y b.
        - Si multiplicar es False y b es cero: devuelve "Operación no válida".

    Restricciones:
        - Utilizar un único return.
        - No utilizar AND ni OR.
    """
    check_int_or_float_parameters(a, b)
    resultado = 0
    if multiplicar:
        resultado = a * b
    if not multiplicar:
        if b == 0:
            resultado = "Operación no válida"
        else:
            resultado = a / b

    return resultado


# NO MODIFICAR - INICIO
assert operacion_basica(1, 1, True) == 1
assert operacion_basica(1, 1, False) == 1
assert operacion_basica(25, 5, True) == 125
assert operacion_basica(25, 5, False) == 5
assert operacion_basica(0, 5, True) == 0
assert operacion_basica(0, 5, False) == 0
assert operacion_basica(1, 0, True) == 0
assert operacion_basica(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN


###############################################################################


def operacion_multiple(a: float, b: float, multiplicar: bool) -> Union[float, str]:
    """Re-Escribir utilizando tres returns."""
    check_int_or_float_parameters(a, b)
    if multiplicar:
        return a * b
    if not multiplicar:
        if b == 0:
            return "Operación no válida"
        return a / b


# NO MODIFICAR - INICIO
assert operacion_multiple(1, 1, True) == 1
assert operacion_multiple(1, 1, False) == 1
assert operacion_multiple(25, 5, True) == 125
assert operacion_multiple(25, 5, False) == 5
assert operacion_multiple(0, 5, True) == 0
assert operacion_multiple(0, 5, False) == 0
assert operacion_multiple(1, 0, True) == 0
assert operacion_multiple(1, 0, False) == "Operación no válida"
# NO MODIFICAR - FIN
