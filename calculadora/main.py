import os
from src.suma import sumar
from src.dividir import dividir
from src.restar import restar

while True:

    # Limpiar pantalla según el sistema operativo
    os.system("cls" if os.name == "nt" else "clear")

    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == '1':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = sumar(num1, num2)
        print(f"El resultado de la suma es: {resultado}")

    elif opcion == '2':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = restar(num1, num2)
        print(f"El resultado de la resta es: {resultado}")

    elif opcion == '4':
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = dividir(num1, num2)
        print(f"El resultado de la división es: {resultado}")

    elif opcion == '5':
        print("Saliendo de la calculadora...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        
    input("Presione Enter para continuar...")