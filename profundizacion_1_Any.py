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
Realice un programa que solicite por consola 2 números
Calcule la diferencia entre ellos e informe por pantalla
si el resultado es positivo, negativo o cero.
'''

print('Ejercicios de práctica con números')
# Empezar aquí la resolución del ejercicio
print('Ingrese un numero:')
numero_1 = int(input())
print('Ingrese otro numero igual o diferente al anterior:')
numero_2 = int(input())
diferencia =numero_1-numero_2
if diferencia > 0:
    print('el resultado es es positivo')
elif diferencia < 0:
    print('el resultado es es negativo')
else:
    print('el resultado es cero')



#ver, queria intentar todas las combinaciones con un for y un range

for i in range(0,10):
    diferencia =numero_1-numero_2
    if diferencia > 0:
        print('el resultado es es positivo')
    elif diferencia < 0:
        print('el resultado es es negativo')
    else:
        print('el resultado es cero')

#ver, queria intentar todas las combinaciones con un for y un diccionario
numero_1 = {0,1,2,3,4,5,6,7,8,9}
numero_2 = {0,1,2,3,4,5,6,7,8,9}

for i in int(numero_2,numero_1):
    diferencia =numero_1-numero_2
    if diferencia > 0:
        print('el resultado es es positivo')
    elif diferencia < 0:
        print('el resultado es es negativo')
    else:
        print('el resultado es cero')
