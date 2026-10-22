# suma.py
def sumar(a, b):
    try:
        return float(a) + float(b)
    except ValueError:
        return "Error: Ingrese numeros validos"