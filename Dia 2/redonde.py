#redondeo: Los floats tienen decimales, pero si se quiere redondeo usando la funcion round indicando el numero de decimales
#round(elnumero,numerodecimales)
#round(10.523,2) resulta en 10.52

print(90/7,0)
print(round(90/7,0))

resultado = round(90/7)
print(resultado)

valor = 95.66666666666666

print(round(valor))

#curiosidad #Si redondeamos en la variable se modifica a int, fuera de la variable va mantener float
print(type(valor))