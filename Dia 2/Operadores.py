x = 6
y = 2
z = 7

print(f'{x} mas {y} es igual a {x + y}')
print(f'{x} menos {y} es igual a {x - y}')
print(f'{x} por {y} es igual a {x * y}')
print(f'{x} entre {y} es igual a {x / y}') #Las divisiones en python son siempre floats

#division al piso, divide y el resultado decimal lo elimina

print(f'{z} divido al piso de {y} es igual a {z//y}') #Va a devolver 3, no 3.5

#El modulo. Cuando haces una division, si algo sobra ese es el modulo. 6/3=2 Modulo es 0 -- 7/2 genera un modulo 1

print(f'{z} modulo de {y} es igual a {z%y}') #resultado es 1. Se usa para saber si algo es par o impar.

#la potencia
print(f'{x} elevado a la {y} es igual a {x**y}') #6*6 es 36

#raiz cuadrada
print(f'La raiz cuadrada de {x} el resultado es {x**0.5}') #siempre ** por 0.5 es raiz cuadrado
