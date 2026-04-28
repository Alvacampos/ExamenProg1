def check_password_strength(password):
    if len(password) < 8:
        print('La contraseña debe tener al menos 8 caracteres.\n')
        return False
    if (password.find(' ') != -1):
        print('La contraseña no debe contener espacios.\n')
        return False
    print('Contraseña válida.\n')
    return True

password = input('Ingrese su contraseña para continuar\n')
check_password_strength(password)