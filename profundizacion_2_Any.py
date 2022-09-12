# Condicionales [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un programa que solicite el ingreso de tres números
enteros, y luego en cada caso informe si el número es par
o impar.
Para cada caso imprimir el resultado en pantalla.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('Ingrese un primer numero entero de 3 numeros:')
numero_1 = int(input())
print('Ingrese un segundo numero entero de 3 numeros, igual o distinto al anterior:')
numero_2 = int(input())
print('Ingrese un tercer numero entero de 3 numeros , igual o distintos a los demas:')
numero_3 = int(input())

if (numero_1 % 2) == 0:
    print('primer numero es par')
else:
    print('primer numero es impar')

if(numero_2 % 2) == 0:
    print('segundo numero es par')
else:
    print('segundo numero es impar')
if(numero_3 % 2) == 0:
    print('tercer numero es par')
else:
    print('tercer numero es impar')
###################################################
print('')
print('no se como enviarle al usuario un mensaje de error si el numero no es de 3 digitos, solo funciona cuando el usuario carga un numero correcto. Caso contario no salta mensaje')
print('ingrese un numero de 3 digitos')
numero_1 = input()
print(len(numero_1))

if len(numero_1)==3:
    print('El ingreso es valido')
elif len(numero_1)!=3:
    print('el numero ingresado no es valido.Vuelva a intertarlo',numero_1 = input())
