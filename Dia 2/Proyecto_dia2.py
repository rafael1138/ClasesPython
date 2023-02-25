#Proyecto de dia 2
#De hacerse un programa que le pregunte al vendedor su nombre, monto de ventas, y le debe decir
#la comision ganada calculada al 13%

nombre = input('Dime tu Nombre: ')
ventas = input('Cuanto has vendido hoy?: ') #en el curso ellos luego hacen venta=int(venta) y asi no hay que cambiar luego
total = int(ventas) * 13/100

print(f'{nombre} tu comision es {round(total)} (redondeada), exacto es {total =} que viene a ser el 13% de {ventas}')