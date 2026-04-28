def ui_divider(): 
    print('----------------------------------')
    
def check_valid_number(input_str):
    try:
        number = float(input_str)
        return number
    except ValueError:
        print('Por favor, ingrese un número válido.')
        return None
    
def math_helper(a, b, option):
    match(option):
        case 'sum':
            return a + b
        case 'subtract':
            return a - b
        case 'multiply':
            return a * b
        case 'divide':
            if b == 0:
                print('No se puede dividir por cero.')
                return None
            return a / b
        case 'modulo':
            if b == 0:
                print('No se puede calcular el resto de una división por cero.')
                return None
            return a % b

runProgram = True
while(runProgram):
    print('Seleccione una opcion: \n')
    option = input('1. Sumar dos números de su elección..\n'
          '2. Restar dos números de su elección.\n'
          '3. Multiplicar dos números de su elección.\n'
          '4. Dividir dos números de su elección.\n'
          '5. Calcular el resto de una division entre dos numeros de su elección.\n')
    ui_divider()
    
    match(option):
        case '1':
            print('Suma de dos números\n')
            num1 = check_valid_number(input('Ingrese el primer número: \n'))
            num2 = check_valid_number(input('Ingrese el segundo número: \n'))
            print(f'El resultado de la suma es: {math_helper(num1, num2, "sum")}\n')
        case '2':
            print('Resta de dos números\n')
            num1 = check_valid_number(input('Ingrese el primer número: \n'))
            num2 = check_valid_number(input('Ingrese el segundo número: \n'))
            print(f'El resultado de la resta es: {math_helper(num1, num2, "subtract")}\n')
        case '3':
            print('Multiplicación de dos números\n')
            num1 = check_valid_number(input('Ingrese el primer número: \n'))
            num2 = check_valid_number(input('Ingrese el segundo número: \n'))
            print(f'El resultado de la multiplicación es: {math_helper(num1, num2, "multiply")}\n')
        case '4':
            print('División de dos números\n')
            num1 = check_valid_number(input('Ingrese el primer número: \n'))
            num2 = check_valid_number(input('Ingrese el segundo número: \n'))
            result = math_helper(num1, num2, "divide")
            if result is not None:
                print(f'El resultado de la división es: {result}\n')
        case '5':
            print('Resto de una división entre dos números\n')
            num1 = check_valid_number(input('Ingrese el primer número: \n'))
            num2 = check_valid_number(input('Ingrese el segundo número: \n'))
            result = math_helper(num1, num2, "modulo")
            if result is not None:
                print(f'El resultado del resto de la división es: {result}\n')
        case _:
            print('Opción inválida, por favor seleccione una opción del 1 al 5.\n')
    ui_divider()