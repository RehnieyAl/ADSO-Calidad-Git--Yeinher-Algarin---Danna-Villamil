## fucnion de restar con validacion de valores
def restar(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        raise ValueError("Los valores ingresados deben ser números.")
    return num1 - num2