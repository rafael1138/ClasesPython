#Funcion Print. Si es texto dentro de comillas.
print('"Hola" Mundo')
print(100)
print(100+50)

#Strings, es una sucesion o varias de caracteres, van a estar dentro de comillas.
print('Hola' + ' ' + 'Rafa')
print("Me llamo \"Rafa\"") #la barra invertidad \ le dice a python que el proximo caracter no va ser tomado como carcter sino textual.
print("Esta es una linea\ny esta es otra linea") # \n es un caracter que le dice a python que lo siguiente sea generado en otra linea
print("Esta es la 3ra linea")
print("\tEsta linea tiene tabluador usando barra t") # \t esto le dice a python que cree un tab

print('This isn\'t a number') #ejemplo apostrofe en ingles

print('Este signo \ es una barra invertida')

#INPUT, este comando le dice a python que debe esperar data ingresada por el usuario. Ejecuta desde adentro hacia afuera,
# pide el input lurgo lo imprime como el ejemplo de abajo
#print(input('Dime tu Nombre: '))
#print(input('Dime tu apellido: '))
#Aqui se nota el ejemplo con mejor logica
print('Tu Nombre es ' + input('Dime tu Nombre: ') + ' ' + input('Dime tu Apellido: '))

