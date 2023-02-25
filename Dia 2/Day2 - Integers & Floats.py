#Integers numeros enteros
#floats numeros con decimales
'''
mi_numero = 1.10
print(mi_numero + mi_numero)
#aqui el mas suma no une

print(type(mi_numero))
'''
#toda variable que se genere con un input es un str no un int
El siguiente codigo va a dar error, para que funcione hay que hacer una conversion de tipos.
edad = input('Hola, me dices tu edad?: ')
print('o que bien, tu edad es ' + edad)

nueva_edad = 10 + edad
print('en 10 anios vas a tener ' + nueva_edad + 'anios')