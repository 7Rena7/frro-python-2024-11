# The function should raise a TypeError if any parameter is not a float or an int.
def check_int_or_float_parameters(*args) -> None:
    for arg in args:
        if type(arg) not in [int, float]:
            raise TypeError("Los parámetros deben ser de tipo int o float")
