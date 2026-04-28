def calculate_age_stage(age):
    if age < 0:
        return 'Edad no válida'
    elif age <= 12:
        return 'Niño'
    elif age <= 19:
        return 'Adolescente'
    elif age <= 59:
        return 'Adulto'
    else:
        return 'Adulto mayor'

try:
    age = int(input("Ingrese su edad: "))
    print(f"Etapa de vida: {calculate_age_stage(age)}")
except ValueError:
    print("Por favor, ingrese un número válido para la edad.")
