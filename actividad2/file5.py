def grading(score):
    if score > 0 and score < 59:
        return 'Insuficiente'
    elif score >= 60 and score <= 69:
        return 'Aprobado'
    elif score >= 70 and score <= 84:
        return 'Notable'
    elif score >= 85 and score <= 100:
        if score >= 95:
            print("Felicitaciones!")
        return 'Sobresaliente'
    else:
        return 'Puntaje inválido'
    
result = grading(int(input('Ingrese su puntaje para conocer su calificación\n')))
print(f'Su calificación es: {result}')