def calculate_bmi(heigh, weight):
    return float(weight) / (float(heigh) ** 2)

def calculate_bmi_category(bmi):
    if bmi < 18.5:
        return 'Bajo peso'
    elif 18.5 <= bmi <= 24.9:
        return 'Peso normal'
    elif 25 <= bmi <= 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

try:
    heigh, weight = map(float, input('Ingrese su altura en metros y su peso en kg para continuar\n').split())
    bmi = calculate_bmi(heigh, weight)
    print(f'Su indice de masa corporal es {bmi}\n')
    print(f'Categoría de IMC: {calculate_bmi_category(bmi)}')
except ValueError:
    print('Por favor, ingrese números válidos para la altura y el peso.')