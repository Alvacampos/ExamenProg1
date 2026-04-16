def ui_divider(): 
    print('----------------------------------')
    
def check_valid_number(value):
    while True:
        try:
            return float(value)
        except ValueError:
            value = input('Entrada no válida. Por favor, ingrese un número válido: \n')

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    return max(numbers)

def find_minimum(numbers):
    return min(numbers)

def find_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

def find_odd_numbers(numbers):
    return [num for num in numbers if num % 2 != 0]

number_array = []
while(True):
    single_input = check_valid_number(input('Ingrese un numero, si ingresa 0 se deja de pedir numeros\n'))
    if single_input == 0:
        break
    number_array.append(single_input)
    ui_divider()
    
runProgram = True
while(runProgram):
    options = input('Seleccione una opcion: \n'
        '1. Calcular el promedio de los números ingresados.\n'
        '2. Encontrar el número máximo.\n'
        '3. Mínimo entre los números ingresados.\n'
        '4. Contar cuántos números pares.\n'
        '5. Contar cuántos números impares se han ingresado.\n'
        '6. Salir\n')
    ui_divider()
    match(options):
        case '1':
            print(f'El promedio de los números ingresados es: {calculate_average(number_array)}\n')
            ui_divider()
        case '2':
            print(f'El número máximo es: {find_maximum(number_array)}\n')
            ui_divider()
        case '3':
            print(f'El número mínimo es: {find_minimum(number_array)}\n')
            ui_divider()
        case '4':
            print(f'Los números pares ingresados son: {find_even_numbers(number_array)}\n')
            ui_divider()
        case '5':
            print(f'Los números impares ingresados son: {find_odd_numbers(number_array)}\n')
            ui_divider()
        case '6':
            print('Saliendo del programa.\n')
            runProgram = False