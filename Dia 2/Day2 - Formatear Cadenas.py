#formar es una funcion para dar fto a strings/cadenas
# Con llaves vacias {} reemplazas las variables sin importar su tipo con el string
# este formato se modifico con las cadenas literales colocando f antes de las comillas en Python 3.6

#
x = 10
y = 5

print('mis numeros son ' + str(x) + " y " + str(y)) #usando codigo sin formateo de cadenas

print('mis numeros son {} y {}'.format(x,y)) #usando la funcion .format()

print('la suma de {} y {} es igual a {}'.format(x,y,y+x)) #usando la funcion .format() aqui incluso sumamos

#usando f (cadenas literales) ---> Esta es la mejor manera actualmente
color = 'rojo'
matricula = 541926

print(f'El Auto es {color} y su matricula es {matricula}')