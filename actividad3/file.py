# def ui_divider(): 
#     print('----------------------------------')
    
# def check_valid_number(value):
#     while True:
#         try:
#             return float(value)
#         except ValueError:
#             value = input('Entrada no válida. Por favor, ingrese un número válido: \n')
    
# def addition(input1, input2):
#     return input1 + input2

# def subtraction(input1, input2):
#     return input1 - input2

# def multiplication(input1, input2):
#     return input1 * input2

# def division(input1, input2):
#     if input2 == 0:
#         print('No se puede dividir por cero.')
#         return division(input1, check_valid_number(input('Ingrese un número válido para el divisor: \n')))
#     return input1 / input2

# def power(input1, input2):
#     return input1 ** input2

# runProgram = True
# while(runProgram):
#     print()
#     option = input('Seleccione una opcion: \n'
#         '1. Sumar dos números.\n'
#         '2. Restar dos números\n'
#         '3. Multiplicar dos números\n'
#         '4. Dividir dos números\n'
#         '5. Elevar un número a la potencia de otro número de tu elección.\n'
#         '6. Salir\n')
#     match(option):
#         case '1':
#             ui_divider()
#             print('Suma de dos números\n')
#             num1 = check_valid_number(input('Ingrese el primer número: \n'))
#             num2 = check_valid_number(input('Ingrese el segundo número: \n'))
#             print(f'El resultado de la suma es: {addition(num1, num2)}\n')
#         case '2':
#             ui_divider()
#             print('Resta de dos números\n')
#             num1 = check_valid_number(input('Ingrese el primer número: \n'))
#             num2 = check_valid_number(input('Ingrese el segundo número: \n'))
#             print(f'El resultado de la resta es: {subtraction(num1, num2)}\n')
#         case '3':
#             ui_divider()
#             print('Multiplicación de dos números\n')
#             num1 = check_valid_number(input('Ingrese el primer número: \n'))
#             num2 = check_valid_number(input('Ingrese el segundo número: \n'))
#             print(f'El resultado de la multiplicación es: {multiplication(num1, num2)}\n')
#         case '4':
#             ui_divider()
#             print('División de dos números\n')
#             num1 = check_valid_number(input('Ingrese el primer número: \n'))
#             num2 = check_valid_number(input('Ingrese el segundo número: \n'))
#             print(f'El resultado de la división es: {division(num1, num2)}\n')
#         case '5':
#             ui_divider()
#             print('Potencia de un número elevado a otro número\n')
#             num1 = check_valid_number(input('Ingrese el número base: \n'))
#             num2 = check_valid_number(input('Ingrese el número exponente: \n'))
#             print(f'El resultado de {num1} elevado a la potencia de {num2} es: {power(num1, num2)}\n')
#         case '6':
#             print('Saliendo del programa.\n')
#             runProgram = False
#         case _:
#             print('Opción no válida. Por favor, seleccione una opción del 1 al 6.\n')
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def average(numbers):
    return sum(numbers) / len(numbers)

def max(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    return maximum

def min(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum

def analizar_numeros(numeros):
    """
    Analiza una lista de números y retorna estadísticas básicas.
    """
    return {
        'suma': sum(numeros),
        'promedio': sum(numeros) / len(numeros),
        'maximo': max(numeros),
        'minimo': min(numeros)
    }

datos = [10, 25, 15, 30, 20]
print(analizar_numeros(datos))