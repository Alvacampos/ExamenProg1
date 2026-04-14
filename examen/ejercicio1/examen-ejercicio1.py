import math

# ── UTILS FUNCTIONS ──────────────────────────────────────────────────────

def print_line_break():
    print('\n' + '=' * 30 + '\n')

def input_ledger():
    while True:
        getLedger = True
        while getLedger:
            print_line_break()
            ledger = input('Ingrese el legajo del alumno: \n')
            if ledger.isdigit():
                return ledger
            else:
                print_line_break()
                print('Legajo inválido, por favor ingrese solo números.')

def add_student(name, ledger, studentsList, ledgerList):
    if(ledger in ledgerList):
        print('El legajo ya existe, por favor ingrese un legajo diferente\n')
        print_line_break()
        return
    studentsList.append({
        'name': name,
        'ledger': ledger,
        'grades': [],
        'gpa': 0
    })
    ledgerList.append(ledger)
    print(f'Alumno {name} agregado correctamente\n')
    print_line_break()
    
def check_grades():
    input_str = input('Ingrese las calificaciones del alumno separadas por espacio: ')
    try:
        grades = list(map(int, input_str.split()))
    except ValueError:
        print('Por favor, ingrese solo números enteros separados por espacio.')
        print_line_break()
        return None
    for grade in grades:
        if grade < 0 or grade > 10:
            print('Calificación inválida, por favor ingrese un número entre 0 y 10.')
            print_line_break()
            return None
    print_line_break()
    return grades

def add_grade_to_student(student):
    grades = check_grades()
    if grades is None:
        return
    student['grades'].extend(grades)
    gpa = sum(student['grades']) / len(student['grades'])
    student['gpa'] = math.trunc(gpa * 100) / 100
    print(f'El GPA del alumno es: {student["gpa"]}\n')

def show_students(students, option):
    if(len(students) == 0):
        print('No hay estudiantes registrados\n')
        return
    match(option):
        case '1':
            for student in students:
                print(f"Nombre: {student['name']}, Legajo: {student['ledger']}\n")
        case '2':
            for student in students:
                print(f"Nombre: {student['name']}, Legajo: {student['ledger']}, Cantidad de calificaciones: {len(student['grades'])}, GPA: {student['gpa']}\n")
    print_line_break()
        
def search_student(ledger, studentsList):
    for student in studentsList:
        if(student['ledger'] == ledger):
            return studentsList.index(student)
    print('Alumno no encontrado\n')
    return None

def show_first_in_queue(queryQueue):
    if(len(queryQueue) == 0):
        print('No hay consultas en la cola\n')
        return
    ledger = queryQueue.pop(0)
    student_index = search_student(ledger, studentsList)
    if student_index is not None:
        student = studentsList[student_index]
        print(f'Alumno consultado:\n Nombre: {student["name"]},\n Legajo: {student["ledger"]}\n GPA: {student["gpa"]}\n Calificaciones: {student["grades"]}\n')
    
def calculate_subjects_average(studentsList):
    if(len(studentsList) == 0):
        print('No hay estudiantes registrados\n')
        return 0
    total_gpa = sum(student['gpa'] for student in studentsList)
    average_gpa = total_gpa / len(studentsList)
    return average_gpa

def best_and_worst_student(studentsList):
    if(len(studentsList) == 0):
        print('No hay estudiantes registrados\n')
        return None, None
    best_student = max(studentsList, key=lambda student: student['gpa'])
    worst_student = min(studentsList, key=lambda student: student['gpa'])
    return best_student, worst_student

# ── MAIN MENU ────────────────────────────────────────────────────────────

print('Bienvenido al menu para gestion de alumnos\n')
runProgram = True
studentsList = []
ledgerList = []
queryQueue = []

while (runProgram):
    print('1. Registrar nuevo estudiante.\n')
    print('2. Registrar calificación de un estudiante.\n')
    print('3. Agregar estudiante a la cola de consultas.\n')
    print('4. Atender siguiente consulta.\n')
    print('5. Ver todos los estudiantes y sus promedios.\n')
    print('6. Ver estadísticas generales.\n')
    print('7. Salir\n')
    
    option = input('Seleccione una opcion: ')
    
    match(option):
        case '1':
            print_line_break()
            name = input('Ingrese el nombre del alumno: \n').capitalize()
            ledger = input_ledger()
            add_student(name, ledger, studentsList, ledgerList)
            
        case '2':
            print_line_break()
            show_students(studentsList, '1')
            ledger = input_ledger()
            student_index = search_student(ledger, studentsList)
            if student_index is not None:
                add_grade_to_student(studentsList[student_index])
                
        case '3':
            print_line_break()
            ledger = input_ledger()
            student_index = search_student(ledger, studentsList)
            if student_index is not None:
                queryQueue.append(ledger)
                print(f'Alumno {studentsList[student_index]["name"]},  agregado a la cola de consultas correctamente\n')
                
        case '4':
            print_line_break()
            show_first_in_queue(queryQueue)
            
        case '5':
            print_line_break()
            print('Mostrando todos los estudiantes y sus promedios...\n')
            show_students(studentsList, '2')
            
        case '6':
            print_line_break()
            print('Mostrando estadísticas generales...\n')
            print(f'Cantidad de estudiantes registrados: {len(studentsList)}\n')
            show_students(studentsList, '2')
            average_gpa = calculate_subjects_average(studentsList)
            print(f'Promedio general de GPA: {average_gpa}\n')
            best_student, worst_student = best_and_worst_student(studentsList)
            if best_student:
                print(f'Mejor estudiante: {best_student["name"]} con GPA {best_student["gpa"]}\n')
            if worst_student:
                print(f'Peor estudiante: {worst_student["name"]} con GPA {worst_student["gpa"]}\n')
            waiting_query_count = len(queryQueue)
            print(f'Cantidad de consultas en espera: {waiting_query_count}\n')
            print_line_break()
            
        case '7':
            print_line_break()
            print('Saliendo del programa...')
            runProgram = False
            
        case _:
            print_line_break()
            print('Opcion no valida, por favor intente nuevamente.')
            print_line_break()
            
