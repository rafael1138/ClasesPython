#El siguiente codigo va a dar error, para que funcione hay que hacer una conversion de tipos.
#Convertir se llama Casting. implicita es cuando python lo hace, Explicita es cuando por codigo forzamos

#Este codigo es con error
'''
edad = input('Hola, me dices tu edad?: ')
print('o que bien, tu edad es ' + edad)

nueva_edad = 10 + edad
print('en 10 anios vas a tener ' + nueva_edad + 'anios')
'''

#Conversiones Implicitas

num1 = 20 #int
num2 = 30.5 #float

num1 = num1 + num2 #al hacer esta suma, num1 se transforma implicitamente en un float por el .5 de num2

print(type(num1))
print(type(num2))

#Conversiones Explicitas

num1 = 5.8 #es un float
print(num1)
print(type(num1))

num2 = int(num1) #aqui le decimos que num2 es num 1 pero int asi que elimina, no rendonde, el decimal.
print(num2)
print(type(num2))

#Ahora si se puede sumar 1 al input de edad debido a que lo convertimos a int.
edad = input('Dime tu edad: ')
edad = int(edad)
nueva_edad = edad + 1
print(' tu nueva edad es ' + nueva_edad) #no se puede concatenar porque tiene texto str y nueva_edad que es int
print(type(edad))