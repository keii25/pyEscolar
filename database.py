from firebase import firebase
import json

firebase = firebase.FirebaseApplication('https://pyescolar.firebaseio.com/', None) 


#codigo_estudiante = int(input('Ingrese codigo de Estudiante: '))
#ver_estudiante = firebase.get('/registro_alumnos_matematica/grados/grado_A/', codigo_estudiante)
#datos = (json.dumps(ver_estudiante, indent=4))

#print(datos['Notas'])




#Datos
codigo = int(input('Codigo de Estudiante: '))
nombre = str(input('Nombre: '))
apellido = str(input('Apellido: '))
sexo = str(input('Sexo: '))

#Notas
nota_1 = float(input('Nota 1: '))
nota_2 = float(input('Nota 2: '))
nota_3 = float(input('Nota 3: '))
definitiva = (int(nota_1 + nota_2 + nota_3) / 3)
print('La nota definitiva es: ', definitiva)

#Estado de Estudiante
if definitiva >= 3:
    estado_estudiante = "Aprobado"
    print(estado_estudiante)
else:
    estado_estudiante = "Reprobado"
    print(estado_estudiante)


data = {   
        'Notas':
            {'nota_1': nota_1,
            'nota_2': nota_2,
            'nota_3': nota_3,
            'definitiva': definitiva,
        }, 'Datos':{
        'nombre': nombre,
        'apellido': apellido,
        'sexo': sexo,
        'estado_estudiante' : estado_estudiante
    }}
        


result = firebase.put('/registro_alumnos_matematica/grados/grado_C', codigo, data)
print('Datos Enviados')

