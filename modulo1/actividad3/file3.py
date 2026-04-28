# Ejercicio 3: Validador de datos
# Escriban un programa que solicite al usuario su edad, altura (en metros) y correo electrónico. El programa debe validar cada dato según los siguientes criterios:

# La edad debe ser un número positivo.
# La altura debe estar entre 0.5 y 2.5 metros.
# El email debe contener "@" y al menos un punto después del "@".
# Si algún dato es inválido, el programa debe solicitar que se ingrese nuevamente hasta que sea correcto. Al final, debe mostrar todos los datos ingresados confirmando que son válidos.

def check_valid_number(value, type):
    while True:
        print(value)
        try:
            return float(value)
        except ValueError:
            value = input(f'Entrada no válida para {type}. Por favor, ingrese un número válido: \n')

def age_validation(age):
    while True:
        if age > 0:
            return age
        else:
            age = check_valid_number(input('Edad no válida. Por favor, ingrese una edad positiva: \n'), "edad")

def height_validation(height):
    while True:
        try:
            height = float(height)
            if 0.5 <= height <= 2.5:
                return height
            else:
                height = check_valid_number(input('Altura no válida. Por favor, ingrese una altura entre 0.5 y 2.5 metros: \n'), "altura")
        except ValueError:
            height = check_valid_number(input('Entrada no válida. Por favor, ingrese un número válido: \n'), "altura")

def email_validation(email):
    while "@" not in email or "." not in email.split("@")[-1]:
        email = input('Correo electrónico no válido. Por favor, ingrese un correo electrónico válido: \n')
    return email

age, height, email = input('Ingrese su edad, altura (en metros) y correo electrónico.\n').split()
age = age_validation(age)
height = height_validation(height)
email = email_validation(email)
print(f'Los datos ingresados son válidos:\nEdad: {age}\nAltura: {height} metros\nCorreo electrónico: {email}')