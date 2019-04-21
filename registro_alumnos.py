
# Registro de Estudiantes

def menu():
    print('\nGrado de Estudiante: \n')
    print('1. Grado A')
    print('2. Grado B')
    print('3. Grado C')
    print('4. Salir')
    print('\n')
    


while True:
    menu()
    opcion=int(input('Digite opcion de grado a Validar: '))
    if opcion==4:
        exit()
    elif opcion==1:
        print('Grado A')
    elif opcion==2:
        print('Grado B')
    elif opcion==3:
        print('Grado C')
    else:
        print('Opcion Invalida')