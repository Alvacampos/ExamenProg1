def calculate_when_to_have_century_old(age):
    return 100 - int(age)
    
name, age = input('Ingrese su nombre y su edad para continuar\n').split()
print(f'Hola {name.capitalize()}, cumpliras 100 años en el año {calculate_when_to_have_century_old(age)}\n')
